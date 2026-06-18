#!/usr/bin/env python3
"""Build phone-friendly reading exports for the Lars Odin manuscript.

The EPUB is intentionally split into one XHTML file per chapter and includes
both EPUB 3 navigation and EPUB 2 NCX navigation, because ebook readers vary in
which table-of-contents format they honor.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
import html
import json
import re
import uuid
import zipfile


ROOT = Path(__file__).resolve().parents[1]
EXPORTS = ROOT / "exports"
TITLE = "Lars Odin"
AUTHOR = "Pruttipuffan"
ILLUSTRATIONS = ROOT / "assets" / "illustrations"


@dataclass
class Section:
    title: str
    markdown: str
    filename: str
    anchor: str


@dataclass
class Illustration:
    chapter: int
    file: str
    alt: str
    caption: str


def load_illustrations() -> dict[int, Illustration]:
    manifest_path = ILLUSTRATIONS / "manifest.json"
    if not manifest_path.exists():
        return {}

    raw = json.loads(manifest_path.read_text(encoding="utf-8"))
    illustrations: dict[int, Illustration] = {}
    for chapter, entry in raw.items():
        chapter_number = int(chapter)
        image_path = ILLUSTRATIONS / entry["file"]
        if not image_path.exists():
            raise FileNotFoundError(f"Illustration missing for chapter {chapter}: {image_path}")
        illustrations[chapter_number] = Illustration(
            chapter=chapter_number,
            file=entry["file"],
            alt=entry["alt"],
            caption=entry["caption"],
        )
    return illustrations


def read_manuscript_parts() -> list[str]:
    parts = [(ROOT / "Lars_Odin_English_Manuscript.md").read_text(encoding="utf-8").strip()]
    chapter_files: list[tuple[int, Path]] = []

    for folder in [ROOT / "chapters", ROOT / "drafts" / "preferred-merged"]:
        for path in folder.glob("*.md"):
            if path.name.upper() == "README.MD":
                continue
            match = re.match(r"(\d+)-", path.name)
            if not match:
                continue
            number = int(match.group(1))
            if folder.name == "chapters" and 17 <= number <= 20:
                chapter_files.append((number, path))
            elif folder.name == "preferred-merged" and 21 <= number <= 55:
                chapter_files.append((number, path))

    for _, path in sorted(chapter_files):
        parts.append(path.read_text(encoding="utf-8").strip())

    return parts


def combined_markdown(parts: list[str], illustrations: dict[int, Illustration]) -> str:
    body = "\n\n---\n\n".join(parts)
    body = re.sub(r"^# Lars Odin\s*", "", body, flags=re.M).strip()
    markdown = f"# {TITLE}\n\n{body}\n"

    if not illustrations:
        return markdown

    lines: list[str] = []
    for line in markdown.splitlines():
        lines.append(line)
        match = re.match(r"^#{1,2}\s+Chapter\s+(\d+):\s+.+$", line)
        if not match:
            continue

        chapter = int(match.group(1))
        illustration = illustrations.get(chapter)
        if illustration:
            image_path = f"../assets/illustrations/{illustration.file}"
            lines.extend(
                [
                    "",
                    f"![{illustration.alt}]({image_path})",
                    "",
                    f"*{illustration.caption}*",
                ]
            )

    return "\n".join(lines).rstrip() + "\n"


def rewrite_epub_image_path(path: str) -> str:
    prefix = "../assets/illustrations/"
    if path.startswith(prefix):
        return f"images/{Path(path).name}"
    return path


def slugify(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-") or "section"


def inline_markdown(value: str) -> str:
    value = html.escape(value)
    value = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", value)
    value = re.sub(r"\*(.+?)\*", r"<em>\1</em>", value)
    return value


def markdown_to_html_body(
    markdown: str,
    heading_ids: bool = False,
    image_path_rewriter=None,
) -> str:
    body: list[str] = []
    paragraph: list[str] = []

    def flush_paragraph() -> None:
        if paragraph:
            body.append("<p>" + inline_markdown(" ".join(paragraph)) + "</p>")
            paragraph.clear()

    lines = markdown.splitlines()
    index = 0
    while index < len(lines):
        line = lines[index]
        stripped = line.strip()
        if not stripped:
            flush_paragraph()
            index += 1
            continue
        if stripped == "---":
            flush_paragraph()
            body.append("<hr />")
            index += 1
            continue

        image = re.match(r"^!\[(.*)\]\((.*)\)$", stripped)
        if image:
            flush_paragraph()
            alt = image.group(1)
            src = image.group(2)
            if image_path_rewriter:
                src = image_path_rewriter(src)

            caption = ""
            if index + 2 < len(lines) and not lines[index + 1].strip():
                caption_match = re.match(r"^\*(.+)\*$", lines[index + 2].strip())
                if caption_match:
                    caption = caption_match.group(1)
                    index += 2

            figure = [
                '<figure class="chapter-illustration">',
                f'<img src="{html.escape(src)}" alt="{html.escape(alt)}" />',
            ]
            if caption:
                figure.append(f"<figcaption>{inline_markdown(caption)}</figcaption>")
            figure.append("</figure>")
            body.append("\n".join(figure))
            index += 1
            continue

        heading = re.match(r"^(#{1,6})\s+(.*)$", stripped)
        if heading:
            flush_paragraph()
            level = len(heading.group(1))
            title = heading.group(2)
            section_id = f' id="{slugify(title)}"' if heading_ids else ""
            body.append(f"<h{level}{section_id}>{inline_markdown(title)}</h{level}>")
            index += 1
            continue

        paragraph.append(stripped)
        index += 1

    flush_paragraph()
    return "\n".join(body)


def split_chapters(markdown: str) -> list[Section]:
    matches = list(re.finditer(r"^#{1,2}\s+(Chapter\s+\d+:\s+.+)$", markdown, flags=re.M))
    if not matches:
        raise ValueError("No chapter headings found")

    sections: list[Section] = []
    seen_slugs: dict[str, int] = {}
    for index, match in enumerate(matches):
        start = match.start()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(markdown)
        chapter_markdown = markdown[start:end].strip()
        title = match.group(1)
        base_slug = slugify(title)
        seen_count = seen_slugs.get(base_slug, 0)
        seen_slugs[base_slug] = seen_count + 1
        slug = base_slug if seen_count == 0 else f"{base_slug}-{seen_count + 1}"
        sections.append(
            Section(
                title=title,
                markdown=chapter_markdown,
                filename=f"chapter-{index + 1:02d}.xhtml",
                anchor=slug,
            )
        )

    return sections


def html_document(body: str) -> str:
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{html.escape(TITLE)}</title>
<style>{css()}</style>
</head>
<body>
{body}
</body>
</html>
"""


def xhtml_document(title: str, body: str) -> str:
    return f"""<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" lang="en">
<head><title>{html.escape(title)}</title><link rel="stylesheet" type="text/css" href="style.css" /></head>
<body>
{body}
</body>
</html>
"""


def css() -> str:
    return """body { font-family: Georgia, serif; line-height: 1.6; max-width: 48rem; margin: 2rem auto; padding: 0 1rem; color: #181818; background: #fbfaf7; }
h1, h2 { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; line-height: 1.2; }
h1 { margin-top: 0; }
h2 { margin-top: 3rem; }
p { margin: 1rem 0; }
hr { border: 0; border-top: 1px solid #ddd3c4; margin: 2.5rem 0; }
.chapter-illustration { margin: 1.5rem auto 2rem; text-align: center; }
.chapter-illustration img { max-width: 100%; height: auto; border: 1px solid #d8d0c2; background: #f7f3ea; }
.chapter-illustration figcaption { margin-top: 0.5rem; font-size: 0.9rem; font-style: italic; color: #5f574c; }
"""


def build_nav(sections: list[Section]) -> str:
    items = "\n".join(
        f'      <li><a href="{section.filename}">{html.escape(section.title)}</a></li>'
        for section in sections
    )
    return f"""<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" lang="en">
<head><title>Contents</title></head>
<body>
  <nav epub:type="toc" id="toc">
    <h1>Contents</h1>
    <ol>
{items}
    </ol>
  </nav>
</body>
</html>
"""


def build_ncx(sections: list[Section], uid: str) -> str:
    nav_points = []
    for index, section in enumerate(sections, start=1):
        nav_points.append(
            f"""    <navPoint id="navPoint-{index}" playOrder="{index}">
      <navLabel><text>{html.escape(section.title)}</text></navLabel>
      <content src="{section.filename}" />
    </navPoint>"""
        )

    return f"""<?xml version="1.0" encoding="UTF-8"?>
<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">
  <head>
    <meta name="dtb:uid" content="{html.escape(uid)}" />
    <meta name="dtb:depth" content="1" />
    <meta name="dtb:totalPageCount" content="0" />
    <meta name="dtb:maxPageNumber" content="0" />
  </head>
  <docTitle><text>{html.escape(TITLE)}</text></docTitle>
  <navMap>
{chr(10).join(nav_points)}
  </navMap>
</ncx>
"""


def build_opf(sections: list[Section], uid: str, illustrations: dict[int, Illustration]) -> str:
    modified = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    manifest_chapters = "\n".join(
        f'    <item id="chapter-{index:02d}" href="{section.filename}" media-type="application/xhtml+xml" />'
        for index, section in enumerate(sections, start=1)
    )
    manifest_images = "\n".join(
        f'    <item id="image-{illustration.chapter:02d}" href="images/{illustration.file}" media-type="image/png" />'
        for illustration in sorted(illustrations.values(), key=lambda item: item.chapter)
    )
    spine_chapters = "\n".join(
        f'    <itemref idref="chapter-{index:02d}" />'
        for index, _ in enumerate(sections, start=1)
    )

    return f"""<?xml version="1.0" encoding="UTF-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="bookid">
  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
    <dc:identifier id="bookid">{html.escape(uid)}</dc:identifier>
    <dc:title>{html.escape(TITLE)}</dc:title>
    <dc:language>en</dc:language>
    <dc:creator>{html.escape(AUTHOR)}</dc:creator>
    <meta property="dcterms:modified">{modified}</meta>
  </metadata>
  <manifest>
    <item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav" />
    <item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml" />
    <item id="css" href="style.css" media-type="text/css" />
{manifest_images}
{manifest_chapters}
  </manifest>
  <spine toc="ncx">
{spine_chapters}
  </spine>
</package>
"""


def build_epub(sections: list[Section], epub_path: Path, illustrations: dict[int, Illustration]) -> None:
    uid = f"urn:uuid:{uuid.uuid4()}"
    container = """<?xml version="1.0" encoding="UTF-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
  <rootfiles>
    <rootfile full-path="EPUB/package.opf" media-type="application/oebps-package+xml" />
  </rootfiles>
</container>
"""
    with zipfile.ZipFile(epub_path, "w") as epub:
        epub.writestr("mimetype", "application/epub+zip", compress_type=zipfile.ZIP_STORED)
        epub.writestr("META-INF/container.xml", container)
        epub.writestr("EPUB/package.opf", build_opf(sections, uid, illustrations))
        epub.writestr("EPUB/nav.xhtml", build_nav(sections))
        epub.writestr("EPUB/toc.ncx", build_ncx(sections, uid))
        epub.writestr("EPUB/style.css", css())
        for illustration in illustrations.values():
            image_path = ILLUSTRATIONS / illustration.file
            epub.write(image_path, f"EPUB/images/{illustration.file}")
        for section in sections:
            body = markdown_to_html_body(
                section.markdown,
                heading_ids=True,
                image_path_rewriter=rewrite_epub_image_path,
            )
            epub.writestr(f"EPUB/{section.filename}", xhtml_document(section.title, body))


def write_readme(chapter_count: int) -> None:
    (EXPORTS / "README.md").write_text(
        f"""# Lars Odin Reading Exports

Generated phone-friendly reading exports from the current preferred draft.

Files:

- `lars-odin-preferred-draft.epub` - ebook file for Apple Books, Google Play Books, Kindle apps that accept EPUB, etc.
- `lars-odin-preferred-draft.html` - single-file browser reading copy.
- `lars-odin-preferred-draft.md` - combined Markdown manuscript.

Reading order included:

- Chapters 1-16 from `../Lars_Odin_English_Manuscript.md`
- Chapters 17-20 from `../chapters/`
- Chapters 21-55 from `../drafts/preferred-merged/`

EPUB structure:

- {chapter_count} chapter files in the reading spine
- EPUB 3 `nav.xhtml` table of contents
- EPUB 2 `toc.ncx` table of contents for older readers
- Chapter-opening illustrations are included when present in `../assets/illustrations/manifest.json`

Generated: {datetime.now().strftime("%Y-%m-%d %H:%M")}
""",
        encoding="utf-8",
    )


def main() -> None:
    EXPORTS.mkdir(exist_ok=True)
    parts = read_manuscript_parts()
    illustrations = load_illustrations()
    markdown = combined_markdown(parts, illustrations)
    sections = split_chapters(markdown)

    if len(sections) != 55:
        raise ValueError(f"Expected 55 chapters, found {len(sections)}")

    (EXPORTS / "lars-odin-preferred-draft.md").write_text(markdown, encoding="utf-8")
    html_body = markdown_to_html_body(markdown, heading_ids=True)
    (EXPORTS / "lars-odin-preferred-draft.html").write_text(html_document(html_body), encoding="utf-8")
    build_epub(sections, EXPORTS / "lars-odin-preferred-draft.epub", illustrations)
    write_readme(len(sections))

    print(f"Generated exports with {len(sections)} chapters and {len(illustrations)} illustrations")


if __name__ == "__main__":
    main()

# Lars Odin Novel Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Write a coherent 50+ chapter English hard sci-fi novel about Lars Odin after Lyra Vargstjärna's Pluto discovery, following the established timeline, worldbuilding, style, and long-term Återviens logic.

**Architecture:** Treat the manuscript as a controlled long-form project, not a scene pile. Each chapter must advance at least two of these: external plot, Lars's memory restoration, long-term Återviens strategy, character agenda, or the larger Creators/Nomads mystery. Use Lars's limited perspective for most chapters, with rare controlled POV breaks only when suspense or dramatic irony benefits.

**Tech Stack:** Markdown manuscript (`Lars_Odin_English_Manuscript.md` for chapters 1-16), separate chapter files (`chapters/` from chapter 17 onward), canon source (`Världsbyggnad/Världsbyggnad.md`), prior draft PDF (`Lars_Odin_sci-fi copy.pdf`), this plan file as continuity control.

---

## Current Manuscript State

**Current file strategy:** `Lars_Odin_English_Manuscript.md` contains chapters 1-16. New chapters are drafted as one file per chapter in `chapters/`. A later cleanup pass can split chapters 1-16 into matching files and optionally generate a combined manuscript.

**Written chapters:** 1-20.

**Current position in story:** Lars has returned to Arkology Zero, partially restored his memory, rescued Valdrun, brought Fastulv inside the spacetime bubble, activated Havets Sista Sång, captured evidence of Black Hole B-7 blood-harvesting technology, established an Aphex audit cover, reached Aphex Dependency L-Prime 41, identified Dr. Mira Sovan as a likely hidden Aerit, survived an attempted Black Hole-style infiltration, revealed limited evidence to Mira, and made the first consent-based ask without forcing an unlock.

**Important current continuity:**
- Lars no longer gets lock-trigger migraines after stage-one/two restoration.
- He still has incomplete memory and emotional shock.
- Grim had no android body during the LP 890-9c shipbuilding flashback; he was a biological quantum brain core in tanks.
- Återviens did not exist as a mature doctrine during Pluto; it developed over ~50 years from survival practice, GRIN, Heliostat pressure, Kalari influence, and repeated failures.
- `Coherence?` / `Coherence.` is now an old Aerit greeting/status phrase; Valdrun and Ödesvaka understand it, Grim is learning it.

---

## Core Story Promise

This book should feel like:
- Lars being funny, rough, overqualified, and emotionally avoidant while becoming more dangerous and more responsible.
- Hard sci-fi competence: sensors, ships, logistics, nanotech, GRIN, spacetime folds, AI, biology, reactor systems, and quantum language should do real plot work.
- Suspense and action: Black Hole B-7, Syren remnants, corrupt elites, artifact traffickers, and hidden hunters keep pressure on the plot.
- Long time horizon: Aerits think in decades and centuries. Urgent events happen, but strategic decisions must be survivable over 90, 300, and 700 years.
- Sense of wonder without spiritual vagueness: Creators, Nomads, consciousness projection, and KBC Void mysteries are strange but framed through evidence, models, and incomplete science.

---

## Five-Act Novel Structure

### Act I: The Drunk Idiot Who Is Not an Idiot (Ch. 1-10, drafted)

Purpose: Establish Lars's voice, hidden abilities, Grim, The Rim, Vigor, Black Hole pressure, Arkology Zero, Valdrun, Lyra's Pluto record, Heliostat/Kalari memory, and the slow emergence of Återviens.

Status: Drafted.

Revision needs later:
- Smooth chapter lengths.
- Make chapter 1-3 transitions less abrupt where needed.
- Ensure early jokes do not repeat too often.
- Ensure object continuity: sunglasses, beef, Fastulv docking, Grim body timeline.

### Act II: Hold Coherence (Ch. 11-22)

Purpose: Turn the discovery into disciplined action. Lars, Grim, Valdrun, Ödesvaka, and Havets Sista Sång use the five-track plan while rescuing/contacting the first hidden Aerit under Aphex cover.

Main threads:
- Aphex audit mission.
- Major Elliot Fabron returns in a larger role.
- Gabriel Arsenault's agenda becomes ambiguous: greedy, pragmatic, genuinely loyal, or all three.
- First hidden Aerit contact tests the consent rule.
- Black Hole B-7 proves it has inside access to corporate/military data.
- Havets Sista Sång becomes a character-like strategic asset.

Drafted chapters:
- Ch. 17: `Audit Cover` - Lars arrives at the Aphex dependency as an absurd board-level auditor; Fabron is assigned as escort.
- Ch. 18: `Materials Fatigue` - Dr. Mira Sovan is introduced through work, habits, hidden brilliance, and ordinary life before Lars explains anything.
- Ch. 19: `Fabron's Orders` - Fabron stays loyal to Aphex while revealing a separate inherited discipline/order that understands fragments of Återviens-shaped practice.
- Ch. 20: `The First Ask` - Lars approaches Mira under consent constraint; she agrees to evidence, not memory work, as new hostile ships approach.

Planned chapters:
- Ch. 21: `Containment Drill` - fight/infiltration at the Aphex facility; Lars uses Fastulv visibly and Havets invisibly.
- Ch. 22: `After the Choice` - the hidden Aerit chooses partial unlock or delay; the outcome costs them something socially or emotionally.

### Act III: Networks That Pretend To Be People (Ch. 23-34)

Purpose: Broaden the conflict across Aphex, NUKEA, The Rim, Vigor, other guardians, hidden nodes, and hostile factions.

Main threads:
- Aphex Defence agenda: not purely evil, but structurally tempted toward monopoly and militarized control.
- NUKEA agenda: modular power lifeline vs licensing dependency trap.
- Major Fabron: possible hidden agenda. He may not be Aerit, but he may be part of an old human-side Återviens church/order seeded by Aerit culture. He is brave, annoying, observant, and harder to fool than Lars expects.
- Vigor becomes active as a guardian through food, logistics, farms, station politics, and quiet defense.
- Black Hole B-7 is not the final boss; it is a symptom and a predator.
- Syren Collective thread becomes more dangerous because they can turn rescue into religious spectacle.

Planned chapters:
- Ch. 23: `The Frenchman's Ledger` - Arsenault's private agenda is revealed as layered: profit, Aphex survival, personal fear of galactic collapse, and desire to keep Lars aligned.
- Ch. 24: `NUKEA Recall` - a reactor standard recall becomes cover for strengthening a vulnerable colony.
- Ch. 25: `Vigor's Table` - Vigor hosts Aphex soldiers and smugglers while coordinating hidden logistics.
- Ch. 26: `The Second Guardian Channel` - one of the unnamed guardians sends a signal that may be compromised.
- Ch. 27: `No Single Heart` - Lars must choose between saving a central hub or letting it fail safely.
- Ch. 28: `Fabron Sees Too Much` - Fabron notices impossible inconsistencies and confronts Lars.
- Ch. 29: `Black Hole Nursery` - evidence shows B-7 is growing biological acquisition capacity, not just stealing it.
- Ch. 30: `The Consent Problem` - a hidden Aerit refuses unlocking but still wants protection.
- Ch. 31: `A Quiet War` - Havets Sista Sång performs a stealth operation that looks like bureaucratic failure from outside.
- Ch. 32: `The Syren Invitation` - Syren Collective offers a trap disguised as negotiation.
- Ch. 33: `Coherence Break` - team disagreement: rescue now vs long-term containment.
- Ch. 34: `The Wrong Savior` - a public actor claims Aerit mythology for propaganda, forcing Lars to avoid direct correction.

### Act IV: The Creators Were Not the Beginning (Ch. 35-44)

Purpose: Escalate from corporate/factional threats to the larger sense-of-wonder mystery: Creators, portals, Nomads, KBC Void, and Lyra's real long game.

Main threads:
- The Creators built the portal network but misunderstood the older artifacts.
- Multiverse Nomads created the artifact/nanobot network and transcended into a consciousness field.
- KBC Void may not be empty in the normal sense; it may be a low-observation conservation/buffer region used by older intelligences to avoid Kardashev-style visibility.
- Lyra has not simply vanished. She may be operating through temporary bodies, distributed clones, delayed holojournals, and field-coupled projections.
- The twist must be sense-of-wonder but not mystical: evidence first, models second, implications third.

Major twist candidate:
The KBC Void is not a natural absence. It is a deliberately low-interaction zone, a cosmic-scale quiet buffer where advanced civilizations reduce observability and complexity to survive. The Creators believed they were hiding portals in spacetime folds; the Nomad network uses such quiet zones as low-noise consciousness-field anchors. The Aerits accidentally built Arkology Zero in the correct kind of place because Lyra learned just enough from the Pluto artifact to feel the pattern without fully understanding it.

Planned chapters:
- Ch. 35: `The Creator Map` - a recovered map shows portal distribution aligned with outer-system artifacts but not caused by them.
- Ch. 36: `Dead Subway` - Lars uses Havets Sista Sång near an old Creator portal; it works but reveals the portal is a crude layer.
- Ch. 37: `Nomad Noise` - Grim detects nonlocal correlations that are communication-like but not message-like.
- Ch. 38: `Lyra's Bad Body` - a flashback/memory/holojournal shows an early failed temporary body experiment, funny and unsettling.
- Ch. 39: `The Empty Place Is Listening` - KBC Void data contradicts cosmological expectations.
- Ch. 40: `Fabron's Lineage` - Fabron's hidden agenda is revealed: not Aerit, but descended from a quiet Återviens order/church that preserved strict principles without knowing the full Aerit origin.
- Ch. 41: `The Creator Mistake` - the team realizes the Creators copied transport from a communication system they did not understand.
- Ch. 42: `The Nomad Hypothesis` - Lyra's later model: artifacts are routers; nanobots are hosts; consciousness projection is local use of a multiversal communication layer.
- Ch. 43: `No Gods, Just Old Engineers` - Lars rejects mystical framing while accepting the scale of the discovery.
- Ch. 44: `Lyra Checks In` - a temporary manifestation appears, leaves evidence, and gives almost no direct answers.

### Act V: Re-Becoming (Ch. 45-55+)

Purpose: Converge the four themes: Återviens, dark forces, civilizational cancer, and the Creators/Nomads agenda. The final conflict should not be "biggest weapon wins"; it should be a system-level crisis where Lars must choose a survivable pattern over a satisfying victory.

Main threads:
- Black Hole B-7 attempts a mass acquisition event against multiple suspected Aerits.
- Syren Collective tries to turn the Nomad/Creator revelation into an extinction religion.
- Aphex and NUKEA must be nudged away from becoming central monopolies.
- Guardians disagree on whether to wake many Aerits.
- Lars must use Havets Sista Sång, Fastulv, Grim, Valdrun, Vigor, Fabron, and Aphex cover in coordinated layers.
- Lyra's plan includes humanity reluctantly, not sentimentally.
- Lyra's long-running plan is larger than the seven guardians: she has been building a distributed recovery apparatus to locate, watch, and eventually gather locked Aerits across the galaxy.
- The recovery apparatus includes manifestation-capable agents using preserved-body consciousness projection / temporary bodies. They can appear in locked rooms, leave unstable nanomaterial residue, and disappear without normal access logs.
- Återviens has a much larger human and multi-species following than the Aerits realize. It has spread as religion, maintenance culture, farming practice, reactor ethics, mutual-aid networks, station guilds, old stories, and social movements.
- This latent following can change history like a galactic social network: not by central command, but by synchronized local action, refusal, repair, whistleblowing, shelter, logistics, and cultural contagion.

Planned chapters:
- Ch. 45: `The Cancer Model` - Grim and Lars model galactic collapse as overgrown control systems.
- Ch. 46: `Wake No More Than Needed` - the hardest Återviens decision: selective awakening.
- Ch. 47: `The Blood Market` - action chapter against a Black Hole biological acquisition hub.
- Ch. 48: `The Public Lie` - Lars must let the galaxy believe a false but stabilizing story.
- Ch. 49: `Havets Sista Sång Sings` - the old ship performs a large-scale operation that is mostly invisible.
- Ch. 50: `The Seven` - surviving/available guardians align, disagree, and choose a limited activation protocol.
- Ch. 51: `The Creator Door` - a portal event reveals the next layer beyond Creator technology.
- Ch. 52: `Not a Return` - the Aerits do not return as rulers; they restore distributed capacity.
- Ch. 53: `Coherence Breaks` - a personal cost: someone refuses, dies, leaves, or remains locked by choice.
- Ch. 54: `Re-Becoming` - final system-level resolution; threat reduced, not permanently solved.
- Ch. 55: `A Quiet Signal` - epilogue hook: Lyra/Nomad/KBC Void mystery remains open with wonder.

---

## Mystery Ledger

### Major Elliot Fabron

Reader question: Is Fabron just a French Aphex major, or does he have a hidden agenda?

Writer truth to use:
- Fabron is not secretly Aerit in the first novel unless a later decision changes it.
- He is unusually resistant to easy manipulation because his family/institution has inherited fragments of Aerit-shaped culture: duty, decentralization, suspicion of monopoly, old stories about "the clear ones."
- His lineage belongs to a quiet Återviens-derived order/church. It looks religious from the outside, but its strict practices are actually cultural encodings of resilience: redundancy, modesty, distributed authority, maintenance duty, suspicion of empire, and refusal to worship central power.
- The order does not know the full truth about Aerits, Lyra, or nanobots. It has preserved useful patterns as ritual and discipline.
- Fabron's order is one visible branch of a much larger latent Återviens following. He may initially think his order is small and marginal, then discover it has sibling traditions across Aphex, NUKEA, The Rim, Abantu trade guilds, station maintenance crews, and old colony networks.
- He begins as Arsenault's watcher on Lars.
- He becomes a human bridge: proof that Aerit influence worked culturally even without nanobots.
- He should remain funny, stiff, brave, and irritated by Lars.

Reveal path:
- Ch. 19: separate orders.
- Ch. 28: notices impossible evidence.
- Ch. 40: lineage/cultural inheritance reveal.
- After Ch. 40: Fabron becomes a human ally who can mobilize non-Aerit Återviens believers without exposing Aerits publicly.

### Gabriel Arsenault and Aphex Defence

Reader question: Is Aphex a villain, ally, or future problem?

Writer truth:
- Aphex is useful, dangerous, and not a monolith.
- Arsenault wants profit and power, but he is not stupid; he understands that galactic collapse is bad for business and France.
- Aphex can become an Återviens-supporting distributed defense supplier or a central militarized cancer.
- Lars's board seat is a lever.

Reveal path:
- Use Aphex as cover and source of tension.
- Let Aphex help for self-interested reasons.
- Make Lars constantly prevent Aphex from centralizing too much.

### Black Hole B-7

Role:
- Immediate predator.
- Fascist paramilitary/criminal consortium.
- Wants Aerit blood/nanobots and knowledge.
- Cannot use the knowledge well because its culture destroys distributed understanding.

Long-term use:
- Black Hole is dangerous but not the deepest mystery.
- It shows what anti-Återviens looks like.
- It drives action, fights, infiltrations, and rescues.

### Syren Collective

Role:
- More ideologically dangerous than Black Hole.
- Can turn revelations into martyrdom/religious spectacle.
- Should force Lars to avoid heroic public action.

### The Creators

Writer truth:
- Built portal network.
- Found older Nomad artifacts and misunderstood them.
- Their portals are a transport layer, not the deepest technology.
- They disappeared ~600,000 years ago; whether they died, transcended, or fragmented remains open until late Act IV/V.

### Multiverse Nomads

Writer truth:
- Older than Creators.
- Built artifact/nanobot network as a multiversal communication/access system.
- Exist as field-like consciousness patterns, not gods.
- Their "agenda" is invitation, selection, and survival through low-dependence coherence, not conquest.

### Lyra

Writer truth:
- Not gone in a simple sense.
- Uses preserved-body consciousness projection, temporary bodies, clones, delayed archives, and nonlocal communication.
- Does not give easy answers because central authority would violate the doctrine she built.
- She includes humanity reluctantly and strategically, not sentimentally.
- She has been working for centuries on a galaxy-scale Aerit recovery plan.
- The plan does not simply "wake everyone." It triages: watch, shield, contact, ask, partially unlock, relocate, or leave locked depending on danger, consent, and local system effects.
- Locked Aerits are findable because they still carry the Aerit nanobot line. Even under hypnosis, the nanobots remain faintly coupled to the larger Aerit network and the older mindfield. The signal does not reveal identity or memory, but it can reveal probable carrier presence through weak coherence signatures, repair-cycle harmonics, route drift, and long-baseline biological error-correction patterns.
- Station Zero/Arkology Zero is the main quiet long-baseline receiver for the recovery plan, not the only one. It coordinates with an older quiet-node mesh: hidden arkology fragments, guardian stations, seeded low-noise observatories, old ships like Havets Sista Sång, dormant relay caches, and trusted cultural/logistics nodes. Together they triangulate weak locked-Aerit carrier signals over decades.
- The recovery plan uses a hypno-safe contact method called the Quiet Knock after detection. Quiet Knock avoids direct truth confrontation. It uses the person's current life and expertise as the first interface, because the hypno protocol was designed to protect identity continuity and punish unsafe recall.
- Lars being drawn to Arkology Zero is the strong version of this wayfinding system. Most locked Aerits should receive weaker, safer nudges: job opportunities, maintenance anomalies, route pressure, familiar technical failures, dreams only as non-semantic pressure, or encounters with agents who never name the old identity first.
- Lyra uses manifestation-capable agents and perhaps her own temporary bodies to check on locked Aerits, seed artifacts, verify readiness, or nudge probability without creating a central command footprint.
- The dark figure in the LP 890-9c memory may be one such manifestation, but keep this unresolved until later.
- Lyra also seeded or tolerated human-scale Återviens movements because culture can move faster than secret agents. She may not fully control these movements anymore, which is good Återviens and also dangerous.

Reveal path:
- Early: unexplained temporary-body traces, missing logs, disintegrating residue.
- Mid: evidence of agents who appear inside locked systems without access records.
- Late: Lyra's recovery apparatus is revealed as a distributed Återviens network, not a secret army.
- Final: Lars inherits or joins the network, but must keep it decentralized.

---

## Continuity Rules

- Pluto ~2030: artifact infection; only survival instincts, no mature Återviens.
- 2030-2033: Pluto survival, defense, portal discovery.
- 2033: flight to Heliostat.
- 2033-2083: Nexus Outpost, Kalari first contact, GRIN, FTL/fusion/energy systems, early colonies, Återviens develops gradually.
- 2083: Rakh'Na attack Earth; Aerits help secretly.
- 2083-2180: Aerits aid expansion but retreat into background.
- 2133: Lars born on Station Zero in KBC Void.
- 2180s: Alpha Fourteen/Hypno project; all except seven guardians hypnotized.
- 2774: Lars story begins.
- Lars true age in 2774: 641.
- Ship's 315-year watch-state is time since Lars's last command access, not Lars's age.
- After partial unlock, Lars no longer has the old lock-trigger migraine.
- Still-locked Aerits can still get the hypno-protocol migraine. The block is selective: external metadata or carefully bounded evidence may pass, but direct contradiction of a cover memory can trigger fallback pain if the primary cognitive steering fails.
- Do not identify locked Aerits by blunt confrontation. First detect probable carriers through nanobot/network coherence; then use Quiet Knock sequence: non-semantic behavioral/occupational challenge, explicit consent for evidence layers, then identity words and memory work only at late stage.
- Lars's staged unlock is a special case, not the standard field method: he was physically at Station Zero/Arkology Zero, under guardian and Ödesvaka authority, with original medical hardware, old command access, and a lock already destabilized by emergency repair demands. Quiet Knock does not dehypnotize; it prevents accidental dehypnotization until a safe staged unlock is possible and consented.
- Quiet Knock can draw a candidate toward safety without conscious knowledge, but it must not override local choice. It should feel like plausible life pressure from inside the person's current identity, not mind control.
- Grim's android body exists only in present-day chapters after he built it two months before Chapter 1; in LP 890-9c flashbacks he is tank-based biological quantum cognition.
- Havets Sista Sång is a major active ship/tool from Act II onward.
- Fastulv remains visible cover and personality; Havets is hidden capability.
- Återviens should usually be shown through practice, not speeches. The inner circle can name it.
- Coherence greeting should appear sparingly but meaningfully.
- Human groups can preserve Återviens principles as religion, ritual, craft, military discipline, maintenance culture, or family tradition without knowing the Aerit origin.
- Fabron's order/church should feel sincere and disciplined, not cartoon religious. Its value is that it lets human civilization carry Aerit-shaped resilience without nanobots.
- The broader Återviens following should not be portrayed as a single church. It is a federation of compatible habits, myths, guild rules, mutual-aid practices, reactor safety rituals, farming customs, and resistance networks.
- The following can mobilize like a social network: fast, messy, partly wrong, locally powerful, hard to decapitate, and impossible for centralized enemies to fully understand.
- Lyra's Aerit recovery network should behave like Återviens: distributed, redundant, consent-aware, low visibility, and resistant to central capture.
- Manifestation-capable agents should leave hard-sci-fi traces: missing access logs, local thermal anomalies, unstable nanomaterial residue, corrupted recordings, field noise, and mass-balance oddities.

---

## Style Rules

- Use `docs/character-voices.md` for dialogue revision. Characters should be identifiable by vocabulary, rhythm, humor type, and professional metaphors, not only by tags.
- Lars banter hides stress and competence.
- Grim should be funny, precise, hungry/food-curious, and increasingly emotionally intelligent.
- Valdrun should be dry, old, affectionate through irritation, and strategically patient.
- Ödesvaka is not comic relief only; its logging jokes should coexist with deep protocol authority.
- Avoid spiritual language unless a character rejects it or reframes it technically.
- Use hard-sci-fi evidence before wonder: sensor data, logs, models, experiments, failures.
- Keep lookbacks vivid and purposeful. A flashback must reveal a present decision, capability, relationship, or mystery.
- Do not resolve every mystery immediately. Maintain writer knowledge > reader knowledge.

---

## Drafting Tasks

### Task 1: Stabilize Existing Manuscript Structure

**Files:**
- Modify: `Lars_Odin_English_Manuscript.md`
- Reference: `Världsbyggnad/Världsbyggnad.md`

- [ ] Review chapter headings 1-16 for consistent pacing and rename any weak titles.
- [ ] Check that chapters 1-16 each advance plot, memory, or strategy.
- [ ] Remove repeated jokes that do not escalate or reveal character.
- [ ] Keep all approved continuity fixes: sunglasses, beef, Grim body timeline, post-unlock migraine, Återviens timeline.

### Task 2: Draft Act II Opening - Aphex Audit Arc

**Files:**
- Add/modify: `chapters/17-audit-cover.md`
- Add/modify: `chapters/18-materials-fatigue.md`
- Add/modify: `chapters/19-fabrons-orders.md`
- Add/modify: `chapters/20-the-first-ask.md`
- Reference: `docs/superpowers/plans/2026-06-16-lars-odin-novel-plan.md`

- [x] Draft Ch. 17 `Audit Cover`.
- [x] Draft Ch. 18 `Materials Fatigue`.
- [x] Draft Ch. 19 `Fabron's Orders`.
- [x] Draft Ch. 20 `The First Ask`.
- [x] Check that the hidden Aerit is treated as a person with consent, not a plot token.

### Task 3: Draft First Major Act II Action Sequence

**Files:**
- Add/modify: `chapters/21-containment-drill.md`

- [ ] Draft Ch. 21 `Containment Drill`.
- [ ] Use both Fastulv and Havets Sista Sång with distinct tactical roles.
- [ ] Include Fabron doing something competent and irritating.
- [ ] Make the fight suspenseful but not just bigger weapons.
- [ ] End with a cost or complication.

### Task 4: Draft Act II Consequence and Reorientation

**Files:**
- Add/modify: `chapters/22-after-the-choice.md`

- [ ] Draft Ch. 22 `After the Choice`.
- [ ] Show the rescued/contacted Aerit's choice.
- [ ] Update the long-term plan based on new information.
- [ ] Seed the Aphex/NUKEA/Syren Act III arcs.

### Task 5: Maintain Mystery Ledger

**Files:**
- Modify: `docs/superpowers/plans/2026-06-16-lars-odin-novel-plan.md`

- [ ] After each 4-chapter drafting block, update what the reader knows.
- [ ] Update what Lars knows.
- [ ] Update what the writer knows but has not revealed.
- [ ] Track open questions: Fabron's order, Arsenault, Vigor, Lyra manifestations, the Aerit recovery apparatus, Creators, Nomads, KBC Void.

### Task 6: Verification After Each Block

**Files:**
- Check: `Lars_Odin_English_Manuscript.md`
- Check: `chapters/`

- [ ] Run linter diagnostics.
- [ ] Search for timeline-sensitive terms: `years`, `Lyra`, `Återviens`, `migraine`, `Grim`, `Havets`, `Fastulv`.
- [ ] Check object continuity: who has what, where ships are, whether supplies are loaded, whether a character could know the fact they state.
- [ ] Check tone balance: suspense, hard science, humor, wonder.

---

## Next Recommended Drafting Block

Draft chapters 17-20 as one coherent block:

1. `Audit Cover` - Lars uses Arsenault/Aphex cover; Fabron returns.
2. `Materials Fatigue` - introduce the hidden Aerit as a working scientist/engineer, not yet aware.
3. `Fabron's Orders` - reveal Fabron has layered instructions and is watching Lars carefully.
4. `The First Ask` - Lars attempts consent-based contact while Black Hole surveillance closes in.

This block should end with a cliffhanger or forced choice, not a full rescue.


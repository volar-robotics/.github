---
name: preflight
description: Preflight is Volar's rehearsal of a deliverable against its audience before it ships. A presenter agent delivers the deck, report, paper, proposal or pitch; a separate audience agent who sees only what the real audience will see reacts, questions and reviews it; the presenter answers from the material alone; then you verify every finding against the sources and report what to fix. Use it whenever a Volar deliverable is about to meet an outside audience that will judge it (a reviewer, a client, an evaluator, an investor, a conference), and whenever someone asks to rehearse, dry-run, mock-review or stress-test a talk or document, asks how a specific person or panel will react, or wants "reviewer 2" feedback, even if they never say "preflight".
date: 2026-11-18
---

# Preflight

Before an aircraft flies, it gets a preflight. Before a Volar deliverable meets its
audience, it flies once in a simulated room: a **pilot** delivers it, a **panel** that
knows only what the real audience will know reacts to it, and you, the **flight
director**, verify what both say before anything changes.

It works because each role sits in its own context. A reviewer that has read your notes
fills the gaps you left without noticing them. A panel that sees only the slides and
hears only the talk finds them. The Q&A pass is the sharpest instrument: every question
the pilot cannot answer from the material is a gap the real audience will find too.

**What it is not.** The panel comes from the same model as you, so it shares your blind
spots and knows no more of the field than you do. It shows what is unclear, unsupported
or hard to defend; it does not stand in for the real person. Never report the panel's
opinions as what the real audience thinks, and never treat its praise as evidence.

## Cost and consent

A preflight runs four to six agent passes on the full artifact. Say so and get a yes
before launching it, unless the person asked for one in so many words.

## 0. Brief

Settle these with the person, or from the wiki vault, before rendering anything:

- **Artifact and format:** a live talk with discussion, a pre-read, a submitted paper, a
  written evaluation. The format decides what the pilot produces (step 2).
- **Audience:** role, expertise, what they care about, and their **state of knowledge**,
  above all what they have *not* read. Take it from the person or from their
  `person_*` page in the wiki vault (`volar-robotics/wiki`, `vault/entities/`).
- **Panel size:** one persona by default. Add up to two more only where the room really
  holds different stakes (for example an expert reviewer, a client engineer, an
  evaluator scoring against a call's criteria).
- **Confidentiality:** what the artifact may not leave. It decides the audio step.

## 1. Render what the audience sees

Put the artifact in the form the audience receives it, in a fresh folder named
`YYYY-MM-DD_<slug>_preflight/` in the scratchpad:

- slides as images (`soffice` to PDF, then `pdftoppm`), one per slide;
- a document as page images, or its PDF;
- each embedded video as a few frames across its length;
- the presenter's private material (speaker notes, the sources) in a separate file the
  panel never receives.

## 2. Pilot: delivery

Spawn the pilot with the artifact, the private material and the brief (template in
`references/prompts.md`). For a talk it writes the transcript it would speak, section by
section; for a document it writes the cover note and the answers it expects to give.
It uses only what the material contains, and after each section it adds
`[Pilot difficulty: …]` wherever the material left it without something it needed.
Those notes are the first signal: they are the places the author knows are thin.

## 3. Panel: live pass

Spawn each panel member separately, with only the rendered artifact and the pilot's
delivery, minus the difficulty notes. Its persona is a **role and a state of knowledge,
never a real individual**: it does not claim to be a named person, to have authored a
cited paper, or to know what that person thinks. It writes per-section reactions (what it
understood, what it did not, what it thinks) and the six to ten questions it would ask,
worded as it would say them.

## 4. Pilot: Q&A

Resume the same pilot agent with the panel's questions. It answers each from the material
alone, and says "we don't know" or "I don't have that" when that is the truth. Count those
answers: the number of questions the material cannot carry is the preflight's headline
measure, and it goes first in the report.

## 5. Panel: debrief

Resume each panel member with the answers. It gives an overall assessment (did it
understand what was done and why, what the real contribution is and whether the artifact
supports it, the weakest points) and ranked feedback, content problems separate from
form problems, plus what to keep. In practice one pass can combine steps 3 and 5 if the
panel writes its debrief after the live pass; the separate pass is better when the Q&A is
likely to change its view.

## 6. Flight director: verification

Before reporting anything, check each factual claim from both agents against the sources:
the report repositories, the simulator and its stored runs, the wiki vault. Label each
finding **confirmed**, **refuted** (say by what) or **unverifiable**. Start with your own
errors: a preflight that finds a mistake in the artifact has done its job, and the
mistake is reported plainly, not softened. A panel claim about the field that you cannot
check stays unverifiable; it is a lead for a literature check, not a fact.

## 7. Report

Write `debrief.md` in the preflight folder and give the person its summary:

1. **Answer gaps:** how many of the panel's questions the material could not answer, and which.
2. **Errors in the artifact:** confirmed mistakes, each with its fix. Fix these before delivery.
3. **Presentation fixes:** changes that need no new work (wording, layout, missing definitions).
4. **New work:** what only analysis, experiments or literature can fix; say whether it fits before the deadline, and if not, how to present it as open.
5. **Disagreements:** findings you do not accept, each with the evidence.
6. **Keep:** what the panel found strong, so revisions do not lose it.

Then ask which fixes to apply. Changing the artifact is a separate step.

## 8. Second sortie (optional)

After fixes, run steps 2 to 5 again on the changed parts only, with a fresh panel, to see
that the fixes land and break nothing nearby.

## 9. Audio (only on request)

Audio adds nothing to the findings; it is for listening to the session for fun. Offer it
in one line at most, and build it only when the person asks: assemble the session as a dialogue (delivery, each
question at the point it was asked, its answer, the debrief) and render it with
`scripts/preflight_audio.py`, which uses local Piper voices so no text leaves the machine.
It needs `pip install piper-tts` and one voice model per speaker from the
`rhasspy/piper-voices` collection; only the models download, never the text.
Confidential material never goes to an online speech service. Mark the recording as
simulated in its first line.

## Variants

| Deliverable | Pilot produces | Panel |
|---|---|---|
| Talk or review meeting | Spoken transcript, slide by slide | The room's expert, plus the client if present |
| Paper | Cover letter and expected rebuttal points | Reviewers for the venue, scoring its criteria |
| Proposal or funding application | The pitch to the evaluators | Evaluators scoring the call's criteria from its `funding-call_*` wiki page |
| Client report | The cover email and walkthrough | The client's engineer, who must act on it |
| Investor pitch | The spoken pitch | An investor and a technical due-diligence reviewer |

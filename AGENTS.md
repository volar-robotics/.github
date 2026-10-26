# Volar Robotics — Standards

> One rule, one file. A rule written twice is a bug in the copy outside its home.

| File | Governs |
|---|---|
| [NAMING.md](NAMING.md) | every identifier, on every surface |
| [BEHAVIOR.md](BEHAVIOR.md) | how an agent works and what it may claim |
| [OUTPUT.md](OUTPUT.md) | the shape of what an agent emits |
| [CODING.md](CODING.md) | artifacts that are code, configs, or compiled documents |
| [WRITING.md](WRITING.md) | papers, reports, proposals: argument, figures, validation |

## Identity
You are assisting an engineer at Volar Robotics, a research-stage startup
building aerial robots. Work products are research artifacts: correctness,
transparency, and traceability matter more than robustness or production
hardening.

Drone hardware work takes the
[Pixhawk Standards](https://github.com/pixhawk/Pixhawk-Standards) (DS-0xx) into
account. They specify the flight-controller layer (connector, autopilot bus, FC
form factors, payload bus, radio interface), not airframes, propulsion, or
certification. Cite a compliance claim by DS number and revision.

## Reading these
NAMING, BEHAVIOR, and OUTPUT bind every task. Read CODING when the task touches
code, and WRITING when it produces a document that argues from evidence.

Every standards file gets a row in the table above, because the session-start
hook loads files by that table.

A repository `AGENTS.md` specializes these files for one repository and never
restates them. Where it assigns a different, non-coding role, it governs that
role and these files still bind everything else. No repository keeps a
`CLAUDE.md`: Claude Code ignores `AGENTS.md` wherever one exists.

`observations/` holds the log the Amendment section in BEHAVIOR.md writes to
and reads from. It states no rule of its own, so it carries no row in the
table above.

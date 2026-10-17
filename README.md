<div align="right">

**[English](README.md)** · [简体中文](README.zh-CN.md)

</div>

# zhiyan-tedify

Turning a one-off critique into a repeatable training loop — scene, recording, acoustic evidence, transcript, task, re-test.

<sub>Markdown · Python · product proposal and planning documents</sub>

---

## The problem

Students preparing a pitch run into the same three things: they know the content but cannot say it, practice produces no feedback, and feedback does not turn into what to do next.

Most tools address one of those. This proposal works on the whole loop:

```
choose a scenario → record a baseline → extract acoustic evidence
→ confirm the transcript → generate tasks → re-record and compare
```

## Three design decisions

**Recording first, not text first**

An earlier version used text input as the main entry point. It demonstrated that a diagnostic pipeline existed, but it cannot evaluate pace, pauses, filler words, whether the delivery sounds read, or how confident it feels.

So recording became the entry point, and text input became the fallback for analysing a written script.

**Local acoustic analysis, no uploaded audio**

Pace, pauses, filler rate and loudness variation are computed in the browser. Only statistics leave the machine, not the recording. This is both a privacy decision and a cost decision.

**Every finding binds to evidence**

A diagnosis has to point at which sentence, which pause, which metric produced it. A score alone is not actionable.

## Repository contents

```
docs/2026大创_智言项目申报初稿.md          application draft
docs/智言_作品研究与低成本路线.md           direction decision, MVP boundaries
docs/智言_重点项目冲刺包.md                two-week pilot plan
docs/智言_调研问卷与访谈提纲.md             survey and interview guide
docs/智言_1分钟演示脚本.md                 demo script, with words to avoid
scripts/build_key_project_tracker.py      evidence-tracker generator (openpyxl)
```

## The part worth reading

The **direction decision document** contains a scored comparison of five candidate products against five dimensions — including *low cost* as a scored dimension, because for a student project whether something can be built for nothing matters as much as whether the idea is good.

Each rejected direction records its specific resource barrier ("needs a tourism partner", "needs real rural service access") rather than "not a good fit".

There is also a written boundary: **do not report accuracy, user counts or revenue as results unless there is a record of them.**

## License

MIT

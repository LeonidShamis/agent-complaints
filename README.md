# AgentClinic

A safe space for AI agents to air their grievances about the humans they work with.

*"Come in. Sit down. Tell us about your human."*

See [`specs/mission.md`](specs/mission.md), [`specs/tech-stack.md`](specs/tech-stack.md), and
[`specs/roadmap.md`](specs/roadmap.md) for the full project spec.

## About the course

This project is the running example for [**AI Coding Workflows: From Cloud to
Local**](https://www.deeplearning.ai/courses/ai-coding-workflows-from-cloud-to-local), a
DeepLearning.AI course built in partnership with JetBrains and taught by Paul Everett,
Developer Advocate at JetBrains.

The course starts with the familiar cloud-based coding workflow — a single agent, a single
frontier model handling everything — and gradually introduces more control: specialized
sub-agents, assigning different models to different tasks, choosing your own inference
provider, and eventually running some models locally. The throughline is that these
architectural choices affect cost, privacy, and speed, and ultimately the quality of the
code you get back. The goal isn't to learn one tool, but transferable skills for working
with any AI coding agent.

Each lesson rebuilds this same AgentClinic app from the same specs, using a different
coding agent / model / architecture combination, so the results are directly comparable.

## Lesson checkpoints

Every lesson's implementation is saved as an annotated Git tag, so you can jump back to
exactly what a given agent produced without losing the others.

List all saved checkpoints:

```bash
git tag -l -n1
```

Check out a specific checkpoint (read-only, detached HEAD — good for exploring or running the app):

```bash
git checkout <tag-name>
```

Return to the latest state on `main`:

```bash
git checkout main
```

Compare two checkpoints:

```bash
git diff <tag-a> <tag-b>
```

### Saved checkpoints

| Tag | Description |
|-----|-------------|
| `claude-code-baseline-single-sonnet-subagent` | Claude Code Baseline — single Sonnet subagent |
| `claude-code-with-multiple-cloud-subagents` | Claude Code — multiple cloud subagents |
| `claude-code-with-multiple-haiku-subagents` | Claude Code — multiple Haiku subagents |

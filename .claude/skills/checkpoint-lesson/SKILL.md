---
name: checkpoint-lesson
description: Save the current lesson's freshly-built AgentClinic app as a Git checkpoint (annotated tag + README entry), then wipe the generated code back to a clean slate for the next lesson. Use after a lesson's coding agent(s) have built the app from specs/ and it has been tested successfully, and the user wants to snapshot it and reset the repo.
---

# Checkpoint a lesson and reset to a clean slate

This project (AgentClinic) is rebuilt from scratch in every lesson of the "AI Coding
Workflows: From Cloud to Local" course, always from the same `specs/` files but with a
different coding agent / model / architecture. This skill performs the repeatable
end-of-lesson ritual: preserve this lesson's result as a restorable checkpoint, then
delete the generated code so the next lesson starts from a clean repo.

Follow these steps in order. Do not skip the push steps — each of the three stages ends
with a push to `origin`, matching the pattern already established in this repo's history
(see `git log` and existing tags like `claude-code-baseline-single-sonnet-subagent`).

## 0. Preconditions

- Run `git status`. If there are uncommitted changes that don't look like this lesson's
  generated app output (e.g. stray edits to `specs/`), stop and ask the user before
  proceeding — do not silently commit or discard unexpected changes.
- Confirm there is actually new generated code to checkpoint (tracked or untracked files
  outside the protected paths below). If the tree is already clean/reset, tell the user
  there's nothing to checkpoint instead of creating an empty commit/tag.

## 1. Determine the tag name and description

The **protected paths** — never delete, never treat as "generated app code" — are:
`specs/`, `README.md`, `requirements.txt`, `.gitignore`, `.claude/`, `.venv/`, `.git/`.
Everything else tracked or newly created in the repo root is this lesson's generated
output.

Figure out (from the conversation, or by asking the user if it's not already clear):
- **Tag name**: short kebab-case, describing the agent/model/architecture combo used,
  consistent with existing tags, e.g. `claude-code-baseline-single-sonnet-subagent`,
  `claude-code-with-multiple-cloud-subagents`.
- **Description**: one line inferred from the tag name and what was actually built,
  matching the style already in the README table (e.g. "Claude Code — multiple cloud
  subagents"). Confirm your inferred description with the user only if it's ambiguous.

## 2. Commit the generated code, tag it, and push

```bash
git add <generated files/dirs — everything outside the protected paths>
git commit -m "<short imperative summary of what this lesson built>"
git tag -a <tag-name> -m "<description>"
git push origin main
git push origin <tag-name>
```

Use `git status` beforehand to see exactly what's staged — do not `git add -A` blindly,
since that could sweep in stray `__pycache__`/`.pytest_cache` directories that happen not
to be gitignored, or unrelated files. Only add the actual generated app code.

## 3. Update README.md and push

Add a new row to the **Saved checkpoints** table in `README.md` (near the bottom), in the
same `| \`tag-name\` | Description |` format as existing rows. Then:

```bash
git add README.md
git commit -m "Add <tag-name> checkpoint to README"
git push origin main
```

## 4. Delete the generated code and push

Remove everything outside the protected paths listed in step 1:

```bash
git rm -r <same generated files/dirs from step 2>
```

Also clean up any stray untracked build artifacts left on disk (these are normally
gitignored but should still be removed so the working tree is truly clean), e.g.
`__pycache__/`, `.pytest_cache/`, and any nested copies under subdirectories:

```bash
find . -maxdepth 3 \( -name '__pycache__' -o -name '.pytest_cache' \) -not -path './.venv/*' -exec rm -rf {} +
```

Then commit and push:

```bash
git commit -m "Remove generated app code to reset for next lesson

Preserved at the <tag-name> tag."
git push origin main
```

## 5. Confirm

Report back to the user concisely: the tag name, the three commit hashes (checkpoint,
README update, reset), and confirmation that `git status` is clean and the repo is back
to just `specs/`, `README.md`, `requirements.txt`, and `.gitignore`. Mention that the
work can be restored anytime with `git checkout <tag-name>`.

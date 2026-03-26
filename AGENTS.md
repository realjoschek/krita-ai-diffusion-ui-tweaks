# AGENTS.md

## Scope
Applies to the entire repository.

## Purpose
This repository is a real GitHub fork of `Acly/krita-ai-diffusion` with an unofficial optional live-preview behavior for regular generation.

## Priorities
1. Keep fork changes minimal and easy to diff from upstream.
2. Preserve upstream attribution/license and avoid presenting fork changes as upstream defaults.
3. Keep release artifacts and notes aligned with actual code behavior.

## Current Fork-Specific Behavior
- Per-step preview frames are forwarded during regular generation.
- Final full-resolution image replaces preview at completion.
- Comfy preview hint is configurable with:
  - `KRITA_AI_DIFFUSION_PREVIEW_METHOD` (default `auto`)

## Files Most Relevant To Live Preview
- `ai_diffusion/client.py`
- `ai_diffusion/comfy_client.py`
- `ai_diffusion/model.py`

## Maintenance Rules
- Prefer additive/minimal edits.
- Do not commit `__pycache__` or `*.pyc`.
- If behavior changes, update:
  - `README.md` (if user-facing behavior changes)
  - `.github/release-drafts/`
  - `docs/unofficial/` notes

## Release Notes And Drafts
- Release drafts: `.github/release-drafts/`
- Fork maintainer notes: `docs/maintainers/`
- Unofficial behavior notes: `docs/unofficial/`

## Upstream Sync Guidance
- Keep `upstream` remote configured.
- Rebase or merge upstream regularly.
- Resolve conflicts in live-preview files carefully and re-test preview flow.

## What Not To Do
- Do not delete historical release tags.
- Do not claim untested compatibility across arbitrary ComfyUI versions.
- Do not redirect fork-specific support requests to upstream maintainers.

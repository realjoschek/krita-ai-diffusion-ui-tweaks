# Publish Checklist (Fork)

1. Confirm fork branch is up to date with `upstream/main`.
2. Verify live-preview files compile and run:
   - `ai_diffusion/client.py`
   - `ai_diffusion/comfy_client.py`
   - `ai_diffusion/model.py`
3. Ensure no `__pycache__`/`.pyc` files are committed.
4. Update release draft in `.github/release-drafts/`.
5. Tag release with clear suffix (example: `v1.47.0-livepreview.2`).
6. Publish GitHub release and attach the generated zip/patch assets.
7. Keep release notes explicit that this behavior is unofficial fork behavior.

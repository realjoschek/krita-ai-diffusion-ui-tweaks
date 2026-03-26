# Unofficial Live Preview Behavior

This fork enables per-step preview updates during regular generation.

Preview method configuration:
- In plugin UI: Interface Settings → Preview Method Hint (`auto`, `taesd`, `latent2rgb`)
- Environment variable fallback:
  - `KRITA_AI_DIFFUSION_PREVIEW_METHOD=auto` (default)
  - `KRITA_AI_DIFFUSION_PREVIEW_METHOD=taesd`
  - `KRITA_AI_DIFFUSION_PREVIEW_METHOD=latent2rgb`

Notes:
- Live previews depend on ComfyUI-side preview image emission.
- Final image insertion remains full-resolution at completion.
- Experimental overlay mode (non-layer preview) can be enabled with:
  - `KRITA_AI_DIFFUSION_EXPERIMENTAL_CANVAS_OVERLAY=1`
  - Pan/zoom tracking is supported; behavior across all Krita versions and canvas rotation states is still experimental.

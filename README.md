# Joscheks UI Tweaks Fork

This fork includes several tweaks that save me some clicks here and there and some upscaling improvements. 

In case this won't get implemented in some fashion, I'll try to keep this up to date with the main branch.

Leave some feedback if you like.


## UI Tweaks

*   **Quick LoRA Selectors**: Moved Lora selection to the generation tab, so you don't have to go into style settings so often
*   **10x Generation Button**: i regularly queue up large queues. this saves me from carpal tunnel syndrome. i know batches exist, but im too afraid of oom.
*   **Cancel Queue Button**: A one click **Cancel** button. saves one click. i change my mind a lot.
*   **Incremental Seeds**: An **Increment** option like is standart in Comfy. i sometimes test thinks and i rarely want to return to comfy to do that.
*   **Apply image now also sets a favourite flag so you can clear out the history of bad generations**
*   **Auto-apply transparency mask**: i use those pretty much everytime anyways. saves me 2 clicks.
*   **Cleanup**: A **Clear History (Keep Favorites)** option added to the history menu to remove bad generations while preserving applied/favorite results.

## Upscaling Tweaks

*   **SeedVR2 Upscaling**: upscaling using SeedVR2. Important: For now you need to install [https://github.com/numz/ComfyUI-SeedVR2_VideoUpscaler](https://github.com/numz/ComfyUI-SeedVR2_VideoUpscaler) by hand to use this.
*   **Upscaling Noise Injection**: Added an option in the Upscale workspace to inject random noise into the image before running the upscale model. This can help fix some blurryness with some upscales.


## Installation

The simplest way to install is to use the release package.

1.  Download the latest **Release ZIP** from the [Releases page](../../releases).
2.  Go to your Krita resources folder (In Krita: `Settings` -> `Manage Resources` -> `Open Resource Folder`).
3.  Open the `pykrita` folder.
4.  Close Krita.
5.  **Delete** any existing `ai-diffusion` folder and the `ai-diffusion.desktop` files (important!).
6.  Extract the ZIP file here. You should end up with a new `ai-diffusion` folder inside `pykrita`.
7.  Start Krita.

---

## For everything else refer back to the original [Krita Ai Diffusion repo](https://github.com/Acly/krita-ai-diffusion)

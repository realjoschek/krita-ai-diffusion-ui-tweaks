# Joscheks UI Tweaks Fork

This fork includes several tweaks that save me some clicks here and there and some upscaling improvements. 

In case this won't get implemented in some fashion, I'll try to keep this up to date with the main branch.

The main goals of this project are:
* **Precision and Control.** Creating entire images from text can be unpredictable.
  To get the result you envision, you can restrict generation to selections,
  refine existing content with a variable degree of strength, focus text on image
  regions, and guide generation with reference images, sketches, line art,
  depth maps, and more.
* **Workflow Integration.** Most image generation tools focus heavily on AI parameters.
  This project aims to be an unobtrusive tool that integrates and synergizes
  with image editing workflows in Krita. Draw, paint, edit and generate seamlessly without worrying about resolution and technical details.
* **Local, Open, Free.** We are committed to open source models. Customize presets, bring your
  own models, and run everything local on your hardware. Cloud generation is also available
  to get started quickly without heavy investment.  

[![Watch video demo](media/screenshot-video-preview.webp)](https://youtu.be/Ly6USRwTHe0 "Watch video demo")

## <a name="features"></a> Features

* **Inpainting**: Use selections for generative fill, expand, to add or remove objects
* **Live Painting**: Let AI interpret your canvas in real time for immediate feedback. [Watch Video](https://youtu.be/AF2VyqSApjA?si=Ve5uQJWcNOATtABU)
* **Upscaling**: Upscale and enrich images to 4k, 8k and beyond without running out of memory.
* **Diffusion Models**: Supports Stable Diffusion 1.5, XL, Illustrious and Flux models
* **Edit Models**: Supports Flux Kontext for instruction-based image editing
* **ControlNet**: Scribble, Line art, Canny edge, Pose, Depth, Normals, Segmentation, +more
* **IP-Adapter**: Reference images, Style and composition transfer, Face swap
* **Regions**: Assign individual text descriptions to image areas defined by layers.
* **Job Queue**: Queue and cancel generation jobs while working on your image.
* **History**: Preview results and browse previous generations and prompts at any time.
* **Strong Defaults**: Versatile default style presets allow for a streamlined UI.
* **Customization**: Create your own presets - custom checkpoints, LoRA, samplers and more.

## <a name="installation"></a> Getting Started

See the [Plugin Installation Guide](https://docs.interstice.cloud/installation) for instructions.

A concise (more technical) version is below:

### Operating System

Windows, Linux, MacOS

#### Hardware support

To run locally a powerful graphics card with at least 6 GB VRAM (NVIDIA) is
recommended. Otherwise generating images will take very long or may fail due to
insufficient memory!

<table>
<tr><td>NVIDIA GPU</td><td>supported via CUDA (Windows/Linux)</td></tr>
<tr><td>AMD GPU</td><td>supported but requires custom ComfyUI setup</td></tr>
<tr><td>Apple Silicon</td><td>community support, MPS on macOS 14+</td></tr>
<tr><td>CPU</td><td>supported, but very slow</td></tr>
<tr><td>XPU</td><td>supported, may see performance issues (Windows/Linux)</td></tr>
</table>

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

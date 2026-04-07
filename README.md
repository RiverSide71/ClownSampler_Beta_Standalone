# ClownSampler_Beta_Standalone ComfyUI Custom Node

A minimal standalone package that gives you
**ClownSampler Beta** and **ClownSampler Advanced Beta** 
custom nodes in ComfyUI for use with the official LTX2.3 workflow, without installing the entire
[RES4LYF](https://github.com/ClownsharkBatwing/RES4LYF) node pack.

> All sampling algorithms and original code belong to **ClownsharkBatwing**.  
> This package only contains necessary files, and edits to be able to use Clownsampler Beta and ClownSampler Advanced Beta nodes for use with LTX2.3 official workflow  
> Source: https://github.com/ClownsharkBatwing/RES4LYF

---

## No extra packages required

The full RES4LYF `requirements.txt` has several requirements. **None of these are needed here.** Those packages are used by other nodes which are not part of the beta sampler chain at all. The beta sampler depends only on `torch` and `numpy`, both of which are already bundled with every ComfyUI installation.

**Do not run `pip install -r requirements.txt` from the full RES4LYF repo **
Doing so risks installing pinned package versions that can break your existing ComfyUI Python enviornment.

---

## Why this repo?

The official LTX2.3 workflow requires the ClownSampler Beta custom node. This package identifies exactly which files to copy, and makes minor edits to some, so all dependencies resolve correctly for ClownSampler Beta to run, without pulling in anything else from the original RES4LYF repo.

---

## Setup

1. Clone this repo into your `ComfyUI/custom_nodes/` folder. 

```bash
git clone https://github.com/RiverSide71/ClownSampler_Beta_Standlone.git
```
2. Restart ComfyUI. The startup log will print:

```
[ClownSampler_Beta_Standalone] Loaded successfully.
```

No git? Download and extract the ZIP from GitHub → **Code → Download ZIP**.

---
## Required folder layout if downloading directly from RES4LYF repo

If you don't want to clone the repo and decide to download individual files directly from the RES4LYF repo, your folder **must** look exactly like this before ComfyUI will load the nodes.

### IMPORTANT:

Files which have ``provided in this package`` below **must** be downloaded from this repository. Do **NOT** use RES4LYF versions of these files!

```
ComfyUI/
└─ custom_nodes/
   └─ ClownSampler_Beta_Standalone/
      ├─ __init__.py                   ← provided in this package
      ├─ helper.py                     ← copy from RES4LYF
      ├─ latents.py                    ← copy from RES4LYF
      ├─ models.py                     ← provided in this package
      ├─ README.md                     ← this file
      ├─ requirements.txt              ← provided in this package (intentionally empty)
      ├─ res4lyf.config.json           ← provided in this package
      ├─ res4lyf.py                    ← provided in this package
      ├─ sigmas.py                     ← copy from RES4LYF
      ├─ style_transfer.py             ← copy from RES4LYF
      └─ beta/
         ├─ __init__.py                ← provided in this package
         ├─ constants.py               ← copy from RES4LYF  beta/constants.py
         ├─ deis_coefficients.py       ← copy from RES4LYF  beta/deis_coefficients.py
         ├─ noise_classes.py           ← copy from RES4LYF  beta/noise_classes.py
         ├─ phi_functions.py           ← copy from RES4LYF  beta/phi_functions.py
         ├─ rk_coefficients_beta.py    ← copy from RES4LYF  beta/rk_coefficients_beta.py
         ├─ rk_guide_func_beta.py      ← copy from RES4LYF  beta/rk_guide_func_beta.py
         ├─ rk_method_beta.py          ← copy from RES4LYF  beta/rk_method_beta.py
         ├─ rk_noise_sampler_beta.py   ← copy from RES4LYF  beta/rk_noise_sampler_beta.py
         ├─ rk_sampler_beta.py         ← copy from RES4LYF  beta/rk_sampler_beta.py
         ├─ samplers.py                ← copy from RES4LYF  beta/samplers.py       
         └─ samplers_extensions.py     ← copy from RES4LYF  beta/samplers_extensions.py
      └─ lightricks/
         ├─ model.py                   ← copy from RES4LYF  lightricks/model.py
         └─ symmetric_patchifier.py    ← copy from RES4LYF  lightricks/symmetric_patchifier.py
```

### Finding the node in ComfyUI

Right-click the canvas → **Add Node** and look under:

```
RES4LYF / samplers / ClownSampler Beta
RES4LYF / samplers / ClownSampler Advanced Beta
```

---

## ⚠️ Important notes

- **Do not install this package alongside the full RES4LYF pack.** Both register nodes under the same class names and will conflict. This package is strictly for users who want only the ClownSampler_Beta node without having to install requirements that might break their ComfyUI Python environment.
- Do not run `pip install` from the full RES4LYF `requirements.txt`. It is not needed here and risks breaking your ComfyUI Python environment.
- If you later decide you want all of RES4LYF, remove this standalone folder first, then install normally.

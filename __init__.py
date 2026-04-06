"""
ClownSampler_Beta - Standalone ComfyUI Custom Node
====================================================
Minimal standalone package containing only the files needed for ClownSampler_Beta.
Extracted from the RES4LYF project by ClownsharkBatwing.
Source: https://github.com/ClownsharkBatwing/RES4LYF

SETUP INSTRUCTIONS
------------------
This folder must contain the following files copied from the RES4LYF repo:

  ClownSampler_Beta_standalone/   <-- this folder goes in ComfyUI/custom_nodes/
  ├── __init__.py                 <-- this file (already provided)
  ├── res4lyf.py                  <-- copy from repo root
  ├── beta/
  │   ├── __init__.py             <-- copy from repo  beta/__init__.py
  │   ├── constants.py            <-- copy from repo  beta/constants.py
  │   ├── samplers_beta.py        <-- copy from repo  beta/samplers_beta.py
  │   ├── rk_sampler_beta.py      <-- copy from repo  beta/rk_sampler_beta.py
  │   ├── rk_method_beta.py       <-- copy from repo  beta/rk_method_beta.py
  │   ├── rk_noise_sampler_beta.py<-- copy from repo  beta/rk_noise_sampler_beta.py
  │   ├── noise_classes.py        <-- copy from repo  beta/noise_classes.py
  │   └──samplers_extensions.py  <-- copy from repo  beta/samplers_extensions.py
  └── requirements.txt            <-- copy from repo root (for pip install - skip!)

STEP-BY-STEP
------------
1. Download/clone the full RES4LYF repo temporarily:
       git clone https://github.com/ClownsharkBatwing/RES4LYF /tmp/RES4LYF

2. Create this folder in your ComfyUI custom_nodes directory:
       mkdir ComfyUI/custom_nodes/ClownSampler_Beta_Standalone

3. Copy the required files:
       cp /tmp/RES4LYF/res4lyf.py              ClownSampler_Beta_Standalone/
       cp /tmp/RES4LYF/requirements.txt         ClownSampler_Beta_Standalone/
       cp -r /tmp/RES4LYF/beta                  ClownSampler_Beta_Standalone/

4. Copy this __init__.py into ClownSampler_Beta_Standalone/ (replacing nothing).

5. Install requirements (adjust pip path for portable ComfyUI if needed):
       pip install -r ClownSampler_Beta_Standalone/requirements.txt

6. Restart ComfyUI. You will find "ClownSampler Beta" under RES4LYF/samplers.

NOTE: If you already have the full RES4LYF installed, do NOT also install this standalone package — they will conflict. This is only for users who want ONLY the ClownSampler_Beta custom node without installing the rest of the pack.
"""

# ──────────────────────────────────────────────────────────────────────────────
# Guard: warn clearly if required files are missing instead of a cryptic crash
# ──────────────────────────────────────────────────────────────────────────────
import os, sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_REQUIRED_FILES = [
    os.path.join(_HERE, "res4lyf.py"),
    os.path.join(_HERE, "beta", "__init__.py"),
    os.path.join(_HERE, "beta", "constants.py"),
    os.path.join(_HERE, "beta", "samplers.py"),
    os.path.join(_HERE, "beta", "rk_sampler_beta.py"),
    os.path.join(_HERE, "beta", "rk_method_beta.py"),
    os.path.join(_HERE, "beta", "rk_noise_sampler_beta.py"),
    os.path.join(_HERE, "beta", "noise_classes.py"),
    os.path.join(_HERE, "beta", "samplers_extensions.py"),
]

_missing = [f for f in _REQUIRED_FILES if not os.path.isfile(f)]
if _missing:
    print("\n[ClownSampler_Beta_Standalone] *** SETUP INCOMPLETE ***")
    print("The following files are missing. Please read the SETUP INSTRUCTIONS")
    print("at the top of __init__.py.\n")
    for m in _missing:
        print(f"  MISSING: {m}")
    print()
    # Raise so ComfyUI shows a clear load error rather than a confusing one
    raise FileNotFoundError(
        "[ClownSampler_Beta_Standalone] Required source files not found. "
        "See __init__.py for setup instructions."
    )

# ──────────────────────────────────────────────────────────────────────────────
# Make sure our local res4lyf module is importable (needed by beta/ submodules)
# ──────────────────────────────────────────────────────────────────────────────
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

# ──────────────────────────────────────────────────────────────────────────────
# Import only the beta sampler nodes — skip all other RES4LYF subsystems
# ──────────────────────────────────────────────────────────────────────────────
try:
    from .beta.samplers import ClownSampler_Beta, ClownSamplerAdvanced_Beta
    _import_ok = True
except Exception as e:
    print(f"[ClownSampler_Beta_Standalone] Import error: {e}")
    raise

# ──────────────────────────────────────────────────────────────────────────────
# Register samplers with the ComfyUI k-diffusion sampling system
# (mirrors the minimal part of RES4LYF's __init__.py that registers extra
#  sampler functions so they can be selected in the node's dropdown)
# ──────────────────────────────────────────────────────────────────────────────
try:
    import comfy.samplers as comfy_samplers
    import comfy.k_diffusion.sampling as k_diffusion_sampling
    from .beta import extra_samplers   # exported by beta/__init__.py

    extra_samplers = extra_samplers()
    for sampler_name, sampler_fn in extra_samplers.items():
        if sampler_name not in comfy_samplers.KSampler.SAMPLERS:
            try:
                idx = comfy_samplers.KSampler.SAMPLERS.index("uni_pc_bh2")
                comfy_samplers.KSampler.SAMPLERS.insert(idx + 1, sampler_name)
            except ValueError:
                comfy_samplers.KSampler.SAMPLERS.append(sampler_name)
        setattr(k_diffusion_sampling, f"sample_{sampler_name}", sampler_fn)
except Exception as e:
    print(f"[ClownSampler_Beta_Standalone] Warning: could not register extra samplers: {e}")

# ──────────────────────────────────────────────────────────────────────────────
# ComfyUI node registration
# ──────────────────────────────────────────────────────────────────────────────
NODE_CLASS_MAPPINGS = {
    "ClownSampler_Beta":         ClownSampler_Beta,
    "ClownSamplerAdvanced_Beta": ClownSamplerAdvanced_Beta,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ClownSampler_Beta":         "ClownSampler Beta",
    "ClownSamplerAdvanced_Beta": "ClownSampler Advanced Beta",
}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]

print("[ClownSampler_Beta_Standalone] Loaded successfully.")

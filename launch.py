import os
import runpy
import sys

import stable_audio_3.model as model_module
import stable_audio_3.model_configs as model_configs
from stable_audio_3.model_configs import ModelConfig


MIRROR_MODELS = {
    "small-music": os.environ.get(
        "SA3_SMALL_MUSIC_REPO", "cocktailpeanut/stable-audio-3-small-music"
    ),
    "small-sfx": os.environ.get(
        "SA3_SMALL_SFX_REPO", "cocktailpeanut/stable-audio-3-small-sfx"
    ),
}


def register_mirrors():
    for name, repo_id in MIRROR_MODELS.items():
        config = ModelConfig(repo_id, "model_config.json", "model.safetensors")
        model_configs.models[name] = config
        model_configs.all_models[name] = config

    model_module.all_models = model_configs.all_models


if __name__ == "__main__":
    register_mirrors()
    sys.argv[0] = "run_gradio.py"
    runpy.run_path("run_gradio.py", run_name="__main__")

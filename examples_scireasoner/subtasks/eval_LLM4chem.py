from mmengine.config import read_base
from opencompass.models import HuggingFacewithChatTemplate, TurboMindModelwithChatTemplate, HuggingFaceCausalLM

with read_base():
    from opencompass.configs.datasets.LLM4Chem.all_datasets import all_datasets
    from opencompass.configs.models.scireason.hf_scireasoner_8b import models

datasets = all_datasets
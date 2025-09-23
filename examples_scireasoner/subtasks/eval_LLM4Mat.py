from mmengine.config import read_base
from opencompass.models import HuggingFacewithChatTemplate


with read_base():
    from opencompass.configs.datasets.LLM4Mat.LLM4Mat_gen import LLM4Mat_datasets
    from opencompass.configs.summarizers.LLM4Mat import summarizer
    from opencompass.configs.models.scireason.hf_scireasoner_8b import models

datasets = LLM4Mat_datasets
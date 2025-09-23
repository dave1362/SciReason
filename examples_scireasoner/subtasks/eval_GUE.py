from mmengine.config import read_base
from opencompass.models import HuggingFacewithChatTemplate


with read_base():
    from opencompass.configs.datasets.GUE.GUE_gen import GUE_datasets
    from opencompass.configs.summarizers.GUE import summarizer
    from opencompass.configs.models.scireason.hf_scireasoner_8b import models

datasets = GUE_datasets

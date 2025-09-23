# retrosysnthesis uspto-50k
from mmengine.config import read_base
with read_base():
    from opencompass.configs.datasets.LLM4Chem.retrosynthesis import Retrosynthesis_datasets
    from opencompass.configs.models.scireason.hf_scireasoner_8b import models

datasets = Retrosynthesis_datasets


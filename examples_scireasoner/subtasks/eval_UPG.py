# unconditional protein generation
from mmengine.config import read_base

with read_base():
    from opencompass.configs.datasets.unconditional_protein_generation.UPG import UPG_datasets 
    from opencompass.configs.models.scireason.hf_scireasoner_8b import models

datasets = UPG_datasets
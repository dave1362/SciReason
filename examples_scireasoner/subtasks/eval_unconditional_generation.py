from mmengine.config import read_base

with read_base():
    from opencompass.configs.datasets.unconditional_molecule_generation.UMG_5shot import UMG_Datasets
    from opencompass.configs.models.scireason.hf_scireasoner_8b import models

datasets = UMG_Datasets
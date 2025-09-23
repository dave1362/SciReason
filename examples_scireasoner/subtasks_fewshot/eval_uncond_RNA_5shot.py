from mmengine.config import read_base

with read_base():
    from opencompass.configs.datasets.uncond_RNA.unconditional_RNA_gen_0shot import uncond_RNA_datasets
    from opencompass.configs.models.scireason.hf_scireasoner_8b import models

datasets = uncond_RNA_datasets


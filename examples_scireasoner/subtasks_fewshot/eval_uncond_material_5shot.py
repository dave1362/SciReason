from mmengine.config import read_base
with read_base():
    from opencompass.configs.datasets.uncond_material.unconditional_material_gen_0shot import uncond_material_datasets
    from opencompass.configs.models.scireason.hf_scireasoner_8b import models

datasets = uncond_material_datasets

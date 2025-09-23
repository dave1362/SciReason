from mmengine.config import read_base

with read_base():
    from opencompass.configs.datasets.composition_material.composition_material_gen_1shot import composition_material_datasets
    from opencompass.configs.models.scireason.hf_scireasoner_8b import models

datasets = composition_material_datasets

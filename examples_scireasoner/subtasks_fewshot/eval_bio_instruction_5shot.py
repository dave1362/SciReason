from mmengine.config import read_base

with read_base():
    from opencompass.configs.datasets.bio_instruction.bio_instruction_5shot import bio_instruction_datasets
    from opencompass.configs.models.scireason.hf_scireasoner_8b import models

datasets = bio_instruction_datasets
from mmengine.config import read_base
from opencompass.models import HuggingFacewithChatTemplate


with read_base():
    from opencompass.configs.datasets.modulus_material.bulk_modulus_material_gen_1shot import modulus_material_datasets
    from opencompass.configs.models.scireason.hf_scireasoner_8b import models

datasets = modulus_material_datasets
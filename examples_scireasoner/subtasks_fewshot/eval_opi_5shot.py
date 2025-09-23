from mmengine.config import read_base
with read_base():
    from opencompass.configs.datasets.opi.all_datasets_5shot import all_datasets
    from opencompass.configs.models.scireason.hf_scireasoner_8b import models

datasets = all_datasets
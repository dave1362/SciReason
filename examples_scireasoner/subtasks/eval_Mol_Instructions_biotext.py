import os.path as osp
from mmengine.config import read_base

with read_base():
    from opencompass.configs.datasets.Mol_Instructions.biotext import mol_biotext_datasets
    from opencompass.configs.models.scireason.hf_scireasoner_8b import models

datasets = mol_biotext_datasets

base_exp_dir = 'outputs/biotext/'
work_dir = osp.join(base_exp_dir, 'mol_instructions')
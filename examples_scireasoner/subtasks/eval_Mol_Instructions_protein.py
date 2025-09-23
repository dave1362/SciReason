import os.path as osp
from mmengine.config import read_base

with read_base():
    from opencompass.configs.datasets.Mol_Instructions.protein import mol_protein_datasets
    from opencompass.configs.models.scireason.hf_scireasoner_8b import models

datasets = mol_protein_datasets

base_exp_dir = 'outputs/protein/'
work_dir = osp.join(base_exp_dir, 'mol_instructions')
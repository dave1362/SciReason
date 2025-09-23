import os.path as osp
from mmengine.config import read_base
with read_base():
    from opencompass.configs.datasets.PEER.peer import PEER_datasets
    from opencompass.configs.models.scireason.hf_scireasoner_8b import models

datasets = PEER_datasets

base_exp_dir = 'outputs/protein/'
work_dir = osp.join(base_exp_dir, 'PEER')
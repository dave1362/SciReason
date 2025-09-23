from mmengine.config import read_base

with read_base():
    from .groups.LLM4Mat import LLM4Mat_summary_groups

summarizer = dict(
    dataset_abbrs=[
        ('MP_classification', 'AUC'),
        ('MP_regression', 'MAD/MAE'),
        ('SNUMAT_classification', 'AUC'),
        ('SNUMAT_regression', 'MAD/MAE'),
        ('JARVISDFT', 'MAD/MAE'),
        ('JARVISQETB', 'MAD/MAE'),
        ('GNoME', 'MAD/MAE'),
        ('hMOF', 'MAD/MAE'),
        ('Cantor_HEA', 'MAD/MAE'),
        ('QMOF', 'MAD/MAE'),
        ('OQMD', 'MAD/MAE'),
        ('OMDB', 'MAD/MAE'),
    ],
    summary_groups=sum([v for k, v in locals().items() if k.endswith('_summary_groups')], []),
)
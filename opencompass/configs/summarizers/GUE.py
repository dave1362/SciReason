from mmengine.config import read_base

with read_base():
    from .groups.GUE import GUE_summary_groups

summarizer = dict(
    dataset_abbrs=[
        ('PD', 'matthews_correlation_all'),
        ('CPD', 'matthews_correlation_all'),
        ('TF-H', 'matthews_correlation_all'),

    ],
    summary_groups=sum([v for k, v in locals().items() if k.endswith('_summary_groups')], []),
)

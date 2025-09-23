GUE_sub_tasks = [
    'cpd-prom_core_all',
    'cpd-prom_core_notata',
    'cpd-prom_core_tata',
    'pd-prom_300_all',
    'pd-prom_300_notata',
    'pd-prom_300_tata',
    'tf-h-0',
    'tf-h-1',
    'tf-h-2',
    'tf-h-3',
    'tf-h-4',
]

GUE_summary_groups = [
    {'name': 'PD', 'subsets': [task for task in GUE_sub_tasks if 'pd-prom_300' in task]},
    {'name': 'CPD', 'subsets': [task for task in GUE_sub_tasks if 'cpd-prom_core' in task]},
    {'name': 'TF-H', 'subsets': [task for task in GUE_sub_tasks if 'tf-h' in task]},
]

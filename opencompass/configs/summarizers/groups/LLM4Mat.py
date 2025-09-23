LLM4Mat_sub_tasks = {
    "MP_FEPA": 10318,
    "MP_Bandgap": 10259,
    "MP_EPA": 10318,
    "MP_Ehull": 10318,
    "MP_Efermi": 10257,
    "MP_Density": 10257,
    "MP_DensityAtomic": 10257,
    "MP_Volume": 10257,
    "MP_IsStable": 10318,
    "MP_IsGapDirect": 10257,
    "JARVISDFT_FEPA": 7597,
    "JARVISDFT_Bandgap_OPT": 7597,
    "JARVISDFT_TotEn": 7597,
    "JARVISDFT_Ehull": 7597,
    "JARVISDFT_Bandgap_MBJ": 1954,
    "JARVISDFT_Kv": 2340,
    "JARVISDFT_Gv": 2340,
    "JARVISDFT_SLME": 967,
    "JARVISDFT_Spillage": 1125,
    "JARVISDFT_Epsx_OPT": 1804,
    "JARVISDFT_Dielectric_DFPT": 459,
    "JARVISDFT_Max_Piezo_dij": 308,
    "JARVISDFT_Max_Piezo_eij": 470,
    "JARVISDFT_MaxEFG": 1205,
    "JARVISDFT_ExfEn": 63,
    "JARVISDFT_AvgMe": 1792,
    "JARVISDFT_nSeebeck": 2358,
    "JARVISDFT_nPF": 2358,
    "JARVISDFT_pSeebeck": 2358,
    "JARVISDFT_pPF": 2358,
    "SNUMAT_Bandgap_GGA": 1038,
    "SNUMAT_Bandgap_HSE": 1038,
    "SNUMAT_Bandgap_GGA_Optical": 1038,
    "SNUMAT_Bandgap_HSE_Optical": 1038,
    "SNUMAT_IsDirect": 2076,
    "SNUMAT_IsDirect_HSE": 1038,
    "SNUMAT_SOC": 1038,
    "GNoME_FEPA": 37620,
    "GNoME_DEPA": 37620,
    "GNoME_Bandgap": 28355,
    "GNoME_TotEn": 37620,
    "GNoME_Volume": 37620,
    "GNoME_Density": 37620,
    "hMOF_MaxCO2": 13275,
    "hMOF_MinCO2": 13275,
    "hMOF_LCD": 13275,
    "hMOF_PLD": 13275,
    "hMOF_VoidFraction": 13275,
    "hMOF_SA_m2g": 13275,
    "hMOF_SA_m2cm3": 13275,
    "Cantor_HEA_FEPA": 8402,
    "Cantor_HEA_EPA": 8402,
    "Cantor_HEA_Ehull": 8402,
    "Cantor_HEA_VPA": 8402,
    "QMOF_TotEn": 766,
    "QMOF_Bandgap": 766,
    "QMOF_LCD": 766,
    "QMOF_PLD": 766,
    "JARVISQETB_EPA": 62399,
    "JARVISQETB_IndirBandgap": 62399,
    "JARVISQETB_FEPA": 62399,
    "JARVISQETB_TotEn": 62399,
    "OQMD_Bandgap": 96358,
    "OQMD_FEPA": 96441,
    "OMDB_Bandgap": 1213
}


LLM4Mat_summary_groups = []

MP_classification_tasks = ["MP_IsStable", "MP_IsGapDirect"]
MP_regression_tasks = [
    task for task in LLM4Mat_sub_tasks
    if task.startswith("MP_") and task not in MP_classification_tasks
]

LLM4Mat_summary_groups.append({
    'name': 'MP_classification',
    'subsets': MP_classification_tasks,
    'weights': {task: LLM4Mat_sub_tasks[task] for task in MP_classification_tasks}
})

LLM4Mat_summary_groups.append({
    'name': 'MP_regression',
    'subsets': MP_regression_tasks,
    'weights': {task: LLM4Mat_sub_tasks[task] for task in MP_regression_tasks}
})

SNUMAT_classification_tasks = ["SNUMAT_IsDirect", "SNUMAT_IsDirect_HSE", "SNUMAT_SOC"]
SNUMAT_regression_tasks = [
    task for task in LLM4Mat_sub_tasks
    if task.startswith("SNUMAT_") and task not in SNUMAT_classification_tasks
]

LLM4Mat_summary_groups.append({
    'name': 'SNUMAT_classification',
    'subsets': SNUMAT_classification_tasks,
    'weights': {task: LLM4Mat_sub_tasks[task] for task in SNUMAT_classification_tasks}
})

LLM4Mat_summary_groups.append({
    'name': 'SNUMAT_regression',
    'subsets': SNUMAT_regression_tasks,
    'weights': {task: LLM4Mat_sub_tasks[task] for task in SNUMAT_regression_tasks}
})

prefixes = ["JARVISDFT", "GNoME", "hMOF", "Cantor_HEA", "QMOF", "OQMD", "OMDB", "JARVISQETB",]

for prefix in prefixes:
    tasks = [task for task in LLM4Mat_sub_tasks if task.startswith(prefix)]
    if tasks:
        LLM4Mat_summary_groups.append({
            'name': prefix,
            'subsets': tasks,
            'weights': {task: LLM4Mat_sub_tasks[task] for task in tasks}
        })
from opencompass.datasets import (
    LLM4MatDataset,
    LLM4Mat_Evaluator,
    LLM4Mat_postprocessor
)
from opencompass.openicl.icl_prompt_template import PromptTemplate
from opencompass.openicl.icl_inferencer import GenInferencer
from opencompass.openicl.icl_retriever import FixKRetriever, ZeroRetriever

LLM4Mat_sub_tasks = \
{ 'MP_FEPA': { 'property': 'formation_energy_per_atom',
               'test_path': 'SciLM/LLM4Mat-test/mp/test/data.json',
               'train_path': 'SciLM/LLM4Mat-test/mp/dev/data.json'},
  'MP_Bandgap': { 'property': 'band_gap',
                  'test_path': 'SciLM/LLM4Mat-test/mp/test/data.json',
                  'train_path': 'SciLM/LLM4Mat-test/mp/dev/data.json'},
  'MP_EPA': { 'property': 'GGA-PBE-based_energy_per_atom',
              'test_path': 'SciLM/LLM4Mat-test/mp/test/data.json',
              'train_path': 'SciLM/LLM4Mat-test/mp/dev/data.json'},
  'MP_Ehull': { 'property': 'energy_above_hull',
                'test_path': 'SciLM/LLM4Mat-test/mp/test/data.json',
                'train_path': 'SciLM/LLM4Mat-test/mp/dev/data.json'},
  'MP_Efermi': { 'property': 'efermi',
                 'test_path': 'SciLM/LLM4Mat-test/mp/test/data.json',
                 'train_path': 'SciLM/LLM4Mat-test/mp/dev/data.json'},
  'MP_Density': { 'property': 'density',
                  'test_path': 'SciLM/LLM4Mat-test/mp/test/data.json',
                  'train_path': 'SciLM/LLM4Mat-test/mp/dev/data.json'},
  'MP_DensityAtomic': { 'property': 'density_atomic',
                        'test_path': 'SciLM/LLM4Mat-test/mp/test/data.json',
                        'train_path': 'SciLM/LLM4Mat-test/mp/dev/data.json'},
  'MP_Volume': { 'property': 'volume',
                 'test_path': 'SciLM/LLM4Mat-test/mp/test/data.json',
                 'train_path': 'SciLM/LLM4Mat-test/mp/dev/data.json'},
  'MP_IsStable': { 'property': 'is_stable',
                   'test_path': 'SciLM/LLM4Mat-test/mp/test/data.json',
                   'train_path': 'SciLM/LLM4Mat-test/mp/dev/data.json'},
  'MP_IsGapDirect': { 'property': 'is_gap_direct',
                      'test_path': 'SciLM/LLM4Mat-test/mp/test/data.json',
                      'train_path': 'SciLM/LLM4Mat-test/mp/dev/data.json'},
  'JARVISDFT_FEPA': { 'property': 'formation_energy_peratom',
                      'test_path': 'SciLM/LLM4Mat-test/jarvis_dft/test/data.json',
                      'train_path': 'SciLM/LLM4Mat-test/jarvis_dft/dev/data.json'},
  'JARVISDFT_Bandgap_OPT': { 'property': 'optb88vdw_bandgap',
                             'test_path': 'SciLM/LLM4Mat-test/jarvis_dft/test/data.json',
                             'train_path': 'SciLM/LLM4Mat-test/jarvis_dft/dev/data.json'},
  'JARVISDFT_TotEn': { 'property': 'optb88vdw_total_energy',
                       'test_path': 'SciLM/LLM4Mat-test/jarvis_dft/test/data.json',
                       'train_path': 'SciLM/LLM4Mat-test/jarvis_dft/dev/data.json'},
  'JARVISDFT_Ehull': { 'property': 'ehull',
                       'test_path': 'SciLM/LLM4Mat-test/jarvis_dft/test/data.json',
                       'train_path': 'SciLM/LLM4Mat-test/jarvis_dft/dev/data.json'},
  'JARVISDFT_Bandgap_MBJ': { 'property': 'mbj_bandgap',
                             'test_path': 'SciLM/LLM4Mat-test/jarvis_dft/test/data.json',
                             'train_path': 'SciLM/LLM4Mat-test/jarvis_dft/dev/data.json'},
  'JARVISDFT_Kv': { 'property': 'bulk_modulus_kv',
                    'test_path': 'SciLM/LLM4Mat-test/jarvis_dft/test/data.json',
                    'train_path': 'SciLM/LLM4Mat-test/jarvis_dft/dev/data.json'},
  'JARVISDFT_Gv': { 'property': 'shear_modulus_gv',
                    'test_path': 'SciLM/LLM4Mat-test/jarvis_dft/test/data.json',
                    'train_path': 'SciLM/LLM4Mat-test/jarvis_dft/dev/data.json'},
  'JARVISDFT_SLME': { 'property': 'slme',
                      'test_path': 'SciLM/LLM4Mat-test/jarvis_dft/test/data.json',
                      'train_path': 'SciLM/LLM4Mat-test/jarvis_dft/dev/data.json'},
  'JARVISDFT_Spillage': { 'property': 'spillage',
                          'test_path': 'SciLM/LLM4Mat-test/jarvis_dft/test/data.json',
                          'train_path': 'SciLM/LLM4Mat-test/jarvis_dft/dev/data.json'},
  'JARVISDFT_Epsx_OPT': { 'property': 'mepsx',
                          'test_path': 'SciLM/LLM4Mat-test/jarvis_dft/test/data.json',
                          'train_path': 'SciLM/LLM4Mat-test/jarvis_dft/dev/data.json'},
  'JARVISDFT_Dielectric_DFPT': { 'property': 'dfpt_piezo_max_dielectric',
                                 'test_path': 'SciLM/LLM4Mat-test/jarvis_dft/test/data.json',
                                 'train_path': 'SciLM/LLM4Mat-test/jarvis_dft/dev/data.json'},
  'JARVISDFT_Max_Piezo_dij': { 'property': 'dfpt_piezo_max_dij',
                               'test_path': 'SciLM/LLM4Mat-test/jarvis_dft/test/data.json',
                               'train_path': 'SciLM/LLM4Mat-test/jarvis_dft/dev/data.json'},
  'JARVISDFT_Max_Piezo_eij': { 'property': 'dfpt_piezo_max_eij',
                               'test_path': 'SciLM/LLM4Mat-test/jarvis_dft/test/data.json',
                               'train_path': 'SciLM/LLM4Mat-test/jarvis_dft/dev/data.json'},
  'JARVISDFT_MaxEFG': { 'property': 'max_efg',
                        'test_path': 'SciLM/LLM4Mat-test/jarvis_dft/test/data.json',
                        'train_path': 'SciLM/LLM4Mat-test/jarvis_dft/dev/data.json'},
  'JARVISDFT_ExfEn': { 'property': 'exfoliation_energy',
                       'test_path': 'SciLM/LLM4Mat-test/jarvis_dft/test/data.json',
                       'train_path': 'SciLM/LLM4Mat-test/jarvis_dft/dev/data.json'},
  'JARVISDFT_AvgMe': { 'property': 'avg_elec_mass',
                       'test_path': 'SciLM/LLM4Mat-test/jarvis_dft/test/data.json',
                       'train_path': 'SciLM/LLM4Mat-test/jarvis_dft/dev/data.json'},
  'JARVISDFT_nSeebeck': { 'property': 'n-Seebeck',
                          'test_path': 'SciLM/LLM4Mat-test/jarvis_dft/test/data.json',
                          'train_path': 'SciLM/LLM4Mat-test/jarvis_dft/dev/data.json'},
  'JARVISDFT_nPF': { 'property': 'n-powerfact',
                     'test_path': 'SciLM/LLM4Mat-test/jarvis_dft/test/data.json',
                     'train_path': 'SciLM/LLM4Mat-test/jarvis_dft/dev/data.json'},
  'JARVISDFT_pSeebeck': { 'property': 'p-Seebeck',
                          'test_path': 'SciLM/LLM4Mat-test/jarvis_dft/test/data.json',
                          'train_path': 'SciLM/LLM4Mat-test/jarvis_dft/dev/data.json'},
  'JARVISDFT_pPF': { 'property': 'p-powerfact',
                     'test_path': 'SciLM/LLM4Mat-test/jarvis_dft/test/data.json',
                     'train_path': 'SciLM/LLM4Mat-test/jarvis_dft/dev/data.json'},
  'SNUMAT_Bandgap_GGA': { 'property': 'Band_gap_GGA',
                          'test_path': 'SciLM/LLM4Mat-test/snumat/test/data.json',
                          'train_path': 'SciLM/LLM4Mat-test/snumat/dev/data.json'},
  'SNUMAT_Bandgap_HSE': { 'property': 'Band_gap_HSE',
                          'test_path': 'SciLM/LLM4Mat-test/snumat/test/data.json',
                          'train_path': 'SciLM/LLM4Mat-test/snumat/dev/data.json'},
  'SNUMAT_Bandgap_GGA_Optical': { 'property': 'Band_gap_GGA_optical',
                                  'test_path': 'SciLM/LLM4Mat-test/snumat/test/data.json',
                                  'train_path': 'SciLM/LLM4Mat-test/snumat/dev/data.json'},
  'SNUMAT_Bandgap_HSE_Optical': { 'property': 'Band_gap_HSE_optical',
                                  'test_path': 'SciLM/LLM4Mat-test/snumat/test/data.json',
                                  'train_path': 'SciLM/LLM4Mat-test/snumat/dev/data.json'},
  'SNUMAT_IsDirect': { 'property': 'Direct_or_indirect',
                       'test_path': 'SciLM/LLM4Mat-test/snumat/test/data.json',
                       'train_path': 'SciLM/LLM4Mat-test/snumat/dev/data.json'},
  'SNUMAT_IsDirect_HSE': { 'property': 'Direct_or_indirect_HSE',
                           'test_path': 'SciLM/LLM4Mat-test/snumat/test/data.json',
                           'train_path': 'SciLM/LLM4Mat-test/snumat/dev/data.json'},
  'SNUMAT_SOC': { 'property': 'SOC',
                  'test_path': 'SciLM/LLM4Mat-test/snumat/test/data.json',
                  'train_path': 'SciLM/LLM4Mat-test/snumat/dev/data.json'},
  'GNoME_FEPA': { 'property': 'Formation_Energy_Per_Atom',
                  'test_path': 'SciLM/LLM4Mat-test/gnome/test/data.json',
                  'train_path': 'SciLM/LLM4Mat-test/gnome/dev/data.json'},
  'GNoME_DEPA': { 'property': 'Decomposition_Energy_Per_Atom',
                  'test_path': 'SciLM/LLM4Mat-test/gnome/test/data.json',
                  'train_path': 'SciLM/LLM4Mat-test/gnome/dev/data.json'},
  'GNoME_Bandgap': { 'property': 'Bandgap',
                     'test_path': 'SciLM/LLM4Mat-test/gnome/test/data.json',
                     'train_path': 'SciLM/LLM4Mat-test/gnome/dev/data.json'},
  'GNoME_TotEn': { 'property': 'Corrected_Energy',
                   'test_path': 'SciLM/LLM4Mat-test/gnome/test/data.json',
                   'train_path': 'SciLM/LLM4Mat-test/gnome/dev/data.json'},
  'GNoME_Volume': { 'property': 'Volume',
                    'test_path': 'SciLM/LLM4Mat-test/gnome/test/data.json',
                    'train_path': 'SciLM/LLM4Mat-test/gnome/dev/data.json'},
  'GNoME_Density': { 'property': 'Density',
                     'test_path': 'SciLM/LLM4Mat-test/gnome/test/data.json',
                     'train_path': 'SciLM/LLM4Mat-test/gnome/dev/data.json'},
  'hMOF_MaxCO2': { 'property': 'max_co2_adsp',
                   'test_path': 'SciLM/LLM4Mat-test/hmof/test/data.json',
                   'train_path': 'SciLM/LLM4Mat-test/hmof/dev/data.json'},
  'hMOF_MinCO2': { 'property': 'min_co2_adsp',
                   'test_path': 'SciLM/LLM4Mat-test/hmof/test/data.json',
                   'train_path': 'SciLM/LLM4Mat-test/hmof/dev/data.json'},
  'hMOF_LCD': { 'property': 'lcd',
                'test_path': 'SciLM/LLM4Mat-test/hmof/test/data.json',
                'train_path': 'SciLM/LLM4Mat-test/hmof/dev/data.json'},
  'hMOF_PLD': { 'property': 'pld',
                'test_path': 'SciLM/LLM4Mat-test/hmof/test/data.json',
                'train_path': 'SciLM/LLM4Mat-test/hmof/dev/data.json'},
  'hMOF_VoidFraction': { 'property': 'void_fraction',
                         'test_path': 'SciLM/LLM4Mat-test/hmof/test/data.json',
                         'train_path': 'SciLM/LLM4Mat-test/hmof/dev/data.json'},
  'hMOF_SA_m2g': { 'property': 'surface_area_m2g',
                   'test_path': 'SciLM/LLM4Mat-test/hmof/test/data.json',
                   'train_path': 'SciLM/LLM4Mat-test/hmof/dev/data.json'},
  'hMOF_SA_m2cm3': { 'property': 'surface_area_m2cm3',
                     'test_path': 'SciLM/LLM4Mat-test/hmof/test/data.json',
                     'train_path': 'SciLM/LLM4Mat-test/hmof/dev/data.json'},
  'Cantor_HEA_FEPA': { 'property': 'Ef_per_atom',
                       'test_path': 'SciLM/LLM4Mat-test/cantor_hea/test/data.json',
                       'train_path': 'SciLM/LLM4Mat-test/cantor_hea/dev/data.json'},
  'Cantor_HEA_EPA': { 'property': 'e_per_atom',
                      'test_path': 'SciLM/LLM4Mat-test/cantor_hea/test/data.json',
                      'train_path': 'SciLM/LLM4Mat-test/cantor_hea/dev/data.json'},
  'Cantor_HEA_Ehull': { 'property': 'e_above_hull',
                        'test_path': 'SciLM/LLM4Mat-test/cantor_hea/test/data.json',
                        'train_path': 'SciLM/LLM4Mat-test/cantor_hea/dev/data.json'},
  'Cantor_HEA_VPA': { 'property': 'volume_per_atom',
                      'test_path': 'SciLM/LLM4Mat-test/cantor_hea/test/data.json',
                      'train_path': 'SciLM/LLM4Mat-test/cantor_hea/dev/data.json'},
  'QMOF_TotEn': { 'property': 'energy_total',
                  'test_path': 'SciLM/LLM4Mat-test/qmof/test/data.json',
                  'train_path': 'SciLM/LLM4Mat-test/qmof/dev/data.json'},
  'QMOF_Bandgap': { 'property': 'bandgap',
                    'test_path': 'SciLM/LLM4Mat-test/qmof/test/data.json',
                    'train_path': 'SciLM/LLM4Mat-test/qmof/dev/data.json'},
  'QMOF_LCD': { 'property': 'lcd',
                'test_path': 'SciLM/LLM4Mat-test/qmof/test/data.json',
                'train_path': 'SciLM/LLM4Mat-test/qmof/dev/data.json'},
  'QMOF_PLD': { 'property': 'pld',
                'test_path': 'SciLM/LLM4Mat-test/qmof/test/data.json',
                'train_path': 'SciLM/LLM4Mat-test/qmof/dev/data.json'},
  'JARVISQETB_EPA': { 'property': 'TB-based_energy_per_atom',
                      'test_path': 'SciLM/LLM4Mat-test/jarvis_qetb/test/data.json',
                      'train_path': 'SciLM/LLM4Mat-test/jarvis_qetb/dev/data.json'},
  'JARVISQETB_IndirBandgap': { 'property': 'indir_gap',
                               'test_path': 'SciLM/LLM4Mat-test/jarvis_qetb/test/data.json',
                               'train_path': 'SciLM/LLM4Mat-test/jarvis_qetb/dev/data.json'},
  'JARVISQETB_FEPA': { 'property': 'f_enp',
                       'test_path': 'SciLM/LLM4Mat-test/jarvis_qetb/test/data.json',
                       'train_path': 'SciLM/LLM4Mat-test/jarvis_qetb/dev/data.json'},
  'JARVISQETB_TotEn': { 'property': 'final_energy',
                        'test_path': 'SciLM/LLM4Mat-test/jarvis_qetb/test/data.json',
                        'train_path': 'SciLM/LLM4Mat-test/jarvis_qetb/dev/data.json'},
  'OQMD_Bandgap': { 'property': 'bandgap',
                    'test_path': 'SciLM/LLM4Mat-test/oqmd/test/data.json',
                    'train_path': 'SciLM/LLM4Mat-test/oqmd/dev/data.json'},
  'OQMD_FEPA': { 'property': 'e_form',
                 'test_path': 'SciLM/LLM4Mat-test/oqmd/test/data.json',
                 'train_path': 'SciLM/LLM4Mat-test/oqmd/dev/data.json'},
  'OMDB_Bandgap': { 'property': 'bandgap',
                    'test_path': 'SciLM/LLM4Mat-test/omdb/test/data.json',
                    'train_path': 'SciLM/LLM4Mat-test/omdb/dev/data.json'}}


non_numeric_props_options = {
    'Direct_or_indirect': ['Direct', 'Indirect'],
    'Direct_or_indirect_HSE': ['Direct', 'Indirect'],
    'SOC': [True, False], 
    'is_gap_direct': [True, False],
    'is_stable': [True, False],
}

LLM4Mat_reader_cfg = dict(input_columns=['input'], output_column='output')

LLM4Mat_datasets = []

generation_kwargs = dict(
    do_sample=False,
)

for name, info in LLM4Mat_sub_tasks.items():
    prop = info['property']
    test_path = info['test_path']
    train_path = info['train_path']

    if prop in non_numeric_props_options:
        options = non_numeric_props_options[prop]
        if all(isinstance(x, bool) for x in options):
            options_str = 'True/False'
        else:
            options_str = '/'.join(str(x) for x in options)
        
        prompt_template = dict(
            round = [
                dict(role='HUMAN', prompt=f"{{input}}"),
                dict(role='BOT', prompt=''),
            ]
        )
    else:
        prompt_template = dict(
            round = [
                dict(role='HUMAN', prompt="{input}"),
                dict(role='BOT', prompt=''),
            ]
        )

    LLM4Mat_infer_cfg = dict(
        prompt_template=dict(
            type=PromptTemplate,
            template=prompt_template,
        ),
        retriever=dict(
            type=ZeroRetriever
        ),
        inferencer=dict(type=GenInferencer, generation_kwargs=generation_kwargs),
    )

    LLM4Mat_eval_cfg = dict(
        evaluator=dict(type=LLM4Mat_Evaluator),
        pred_role='BOT',
        pred_postprocessor=dict(type=LLM4Mat_postprocessor,property=prop),
        dataset_postprocessor=dict(type=LLM4Mat_postprocessor,property=prop),
    )

    LLM4Mat_datasets.append(
        dict(
            abbr=name,
            type=LLM4MatDataset,
            path=test_path,
            train_path=train_path, 
            property=prop,
            hf_hub=True,
            reader_cfg=LLM4Mat_reader_cfg,
            infer_cfg=LLM4Mat_infer_cfg,
            eval_cfg=LLM4Mat_eval_cfg,
        )
    )
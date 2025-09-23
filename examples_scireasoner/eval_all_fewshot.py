from mmengine.config import read_base

with read_base():
    # bio instruction 15 tasks:['antibody_antigen', 'rna_protein_interaction', 'emp', 'enhancer_activity', 'tf_m', 'Isoform', 'Modification', 'MeanRibosomeLoading', 'ProgrammableRNASwitches', 'CRISPROnTarget', 'promoter_enhancer_interaction', 'sirnaEfficiency', 'cpd', 'pd', 'tf_h']
    from opencompass.configs.datasets.bio_instruction.bio_instruction_5shot import bio_instruction_datasets
    # composition_to_material_generation task
    from opencompass.configs.datasets.composition_material.composition_material_gen_5shot import composition_material_datasets
    # GUE 11 tasks : ['cpd-prom_core_all', 'cpd-prom_core_notata', 'cpd-prom_core_tata', 'pd-prom_300_all', 'pd-prom_300_notata', 'pd-prom_300_tata', 'tf-h-0', 'tf-h-1', 'tf-h-2', 'tf-h-3', 'tf-h-4']
    from opencompass.configs.datasets.GUE.GUE_gen_5shot import GUE_datasets
    # LLM4Chem(smol) 14 tasks: ['forward_synthesis', 'retrosynthesis', 'molecule_captioning', 'molecule_generation', 'name_conversion-i2f', 'name_conversion-i2s', 'name_conversion-s2f', 'name_conversion-s2i', 'property_prediction-esol', 'property_prediction-lipo', 'property_prediction-bbbp', 'property_prediction-clintox', 'property_prediction-hiv', 'property_prediction-sider']
    from opencompass.configs.datasets.LLM4Chem.all_datasets_5shot import all_datasets as smol_datasets
    # Retrosynthesis task in Uspto50k Dataset
    from opencompass.configs.datasets.LLM4Chem.retrosynthesis_5shot import Retrosynthesis_datasets as Retrosynthesis_uspto50k_datasets
    # LLM4Mat 65 tasks: ['MP_FEPA', 'MP_Bandgap', 'MP_EPA', 'MP_Ehull', 'MP_Efermi', 'MP_Density', 'MP_DensityAtomic', 'MP_Volume', 'MP_IsStable', 'MP_IsGapDirect', 'JARVISDFT_FEPA', 'JARVISDFT_Bandgap_OPT', 'JARVISDFT_TotEn', 'JARVISDFT_Ehull', 'JARVISDFT_Bandgap_MBJ', 'JARVISDFT_Kv', 'JARVISDFT_Gv', 'JARVISDFT_SLME', 'JARVISDFT_Spillage', 'JARVISDFT_Epsx_OPT', 'JARVISDFT_Dielectric_DFPT', 'JARVISDFT_Max_Piezo_dij', 'JARVISDFT_Max_Piezo_eij', 'JARVISDFT_MaxEFG', 'JARVISDFT_ExfEn', 'JARVISDFT_AvgMe', 'JARVISDFT_nSeebeck', 'JARVISDFT_nPF', 'JARVISDFT_pSeebeck', 'JARVISDFT_pPF', 'SNUMAT_Bandgap_GGA', 'SNUMAT_Bandgap_HSE', 'SNUMAT_Bandgap_GGA_Optical', 'SNUMAT_Bandgap_HSE_Optical', 'SNUMAT_IsDirect', 'SNUMAT_IsDirect_HSE', 'SNUMAT_SOC', 'GNoME_FEPA', 'GNoME_DEPA', 'GNoME_Bandgap', 'GNoME_TotEn', 'GNoME_Volume', 'GNoME_Density', 'hMOF_MaxCO2', 'hMOF_MinCO2', 'hMOF_LCD', 'hMOF_PLD', 'hMOF_VoidFraction', 'hMOF_SA_m2g', 'hMOF_SA_m2cm3', 'Cantor_HEA_FEPA', 'Cantor_HEA_EPA', 'Cantor_HEA_Ehull', 'Cantor_HEA_VPA', 'QMOF_TotEn', 'QMOF_Bandgap', 'QMOF_LCD', 'QMOF_PLD', 'JARVISQETB_EPA', 'JARVISQETB_IndirBandgap', 'JARVISQETB_FEPA', 'JARVISQETB_TotEn', 'OQMD_Bandgap', 'OQMD_FEPA', 'OMDB_Bandgap']
    from opencompass.configs.datasets.LLM4Mat.LLM4Mat_gen_5shot import LLM4Mat_datasets
    # bulk_modulus_to_material_generation task
    from opencompass.configs.datasets.modulus_material.bulk_modulus_material_gen_5shot import modulus_material_datasets
    # Mol Instructions part1 6 tasks: ['chemical_disease_interaction_extraction', 'chemical_entity_recognition', 'chemical_protein_interaction_extraction', 'multi_choice_question', 'open_question', 'true_or_false_question']
    from opencompass.configs.datasets.Mol_Instructions.biotext_5shot import mol_biotext_datasets
    # Mol Instructions part2 6 tasks: ['property_prediction_str', 'description_guided_molecule_design', 'forward_reaction_prediction', 'retrosynthesis', 'reagent_prediction', 'molecular_description_generation']
    from opencompass.configs.datasets.Mol_Instructions.molecule_1shot import mol_mol_datasets
    # Mol Instructions part3 4 tasks: ['catalytic_activity', 'domain_motif', 'general_function', 'protein_function']
    from opencompass.configs.datasets.Mol_Instructions.protein_1shot import mol_protein_datasets
    # OPI 16 tasks: ['EC_number_CLEAN_EC_number_new', 'EC_number_CLEAN_EC_number_price', 'Fold_type_fold_type', 'Function_CASPSimilarSeq_function', 'Function_IDFilterSeq_function', 'Function_UniProtSeq_function', 'gName2Cancer_gene_name_to_cancer', 'GO_CASPSimilarSeq_go', 'GO_IDFilterSeq_go', 'GO_UniProtSeq_go', 'gSymbol2Cancer_gene_symbol_to_cancer', 'gSymbol2Tissue_gene_symbol_to_tissue', 'Keywords_CASPSimilarSeq_keywords', 'Keywords_IDFilterSeq_keywords', 'Keywords_UniProtSeq_keywords', 'Subcellular_localization_subcell_loc']
    from opencompass.configs.datasets.opi.all_datasets_5shot import all_datasets as opi_datasets
    # PEER 4 tasks: ['solubility', 'stability', 'human_ppi', 'yeast_ppi']
    from opencompass.configs.datasets.PEER.peer_1shot_and_5shot import PEER_datasets

    # unconditional material generation task
    from opencompass.configs.datasets.uncond_material.unconditional_material_gen_0shot import uncond_material_datasets
    # unconditional RNA generation task
    from opencompass.configs.datasets.uncond_RNA.unconditional_RNA_gen_0shot import uncond_RNA_datasets
    # unconditional protein generation task
    from opencompass.configs.datasets.unconditional_protein_generation.UPG_5shot import UPG_datasets  as uncond_protein_datasets
    # unconditional molecule generation task
    from opencompass.configs.datasets.unconditional_molecule_generation.UMG_5shot import UMG_Datasets


    # from opencompass.configs.models.scireason.hf_scireasoner_8b import models

from opencompass.models import OpenAI

datasets = bio_instruction_datasets + composition_material_datasets + GUE_datasets + smol_datasets + \
           Retrosynthesis_uspto50k_datasets + LLM4Mat_datasets + modulus_material_datasets + \
           mol_biotext_datasets + mol_mol_datasets + mol_protein_datasets + opi_datasets + PEER_datasets + \
           uncond_material_datasets + uncond_RNA_datasets + uncond_protein_datasets + UMG_Datasets

models = [
    dict(
        type=OpenAI,
        path='o3',  # model name
        key='', # your openai api key
        openai_api_base='', # your openai api base url, e.g., for Azure OpenAI, "https://{your-azure-openai-endpoint}.openai.azure.com/"
        max_seq_len=32000,
        abbr='o3',
        run_cfg=dict(num_gpus=0),
        max_out_len=32000,
        batch_size=1,
        retry=3,
    ),
]
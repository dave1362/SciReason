from mmengine.config import read_base
from opencompass.models import HuggingFacewithChatTemplate
from opencompass.openicl.icl_prompt_template import PromptTemplate
from opencompass.openicl.icl_retriever import ZeroRetriever,FixKRetriever
from opencompass.openicl.icl_inferencer import GenInferencer
from transformers import Qwen2ForCausalLM, Qwen2Tokenizer, Qwen3ForCausalLM
from opencompass.datasets import Bioinstruction_Dataset,bio_instruction_Evaluator


INFER_TEMPLATE=''''''
reader_cfg = dict(input_columns=['input'], output_column='output')

MODEL_NAME=r'model'

bio_instruction_datasets = []


path=["antibody_antigen","rna_protein_interaction","emp","enhancer_activity","tf_m","Isoform","Modification","MeanRibosomeLoading","ProgrammableRNASwitches",
"CRISPROnTarget","promoter_enhancer_interaction","sirnaEfficiency","cpd","pd","tf_h"]


for task in path:
    infer_cfg = dict(
        prompt_template=dict(
                type=PromptTemplate,
                template=dict(
                begin=[
                    '</E>',
                ],
                    round=[
                    dict(role='HUMAN', prompt="{input}  Please use the <summary> tag to summarize predication after thinking."),
                ]),
                ice_token="</E>",
                ),
        ice_template=dict(
            type=PromptTemplate,
            template = dict(
                round = [
                    dict(role='HUMAN', prompt="{input} Please use the <summary> tag to summarize predication after thinking."),
                    dict(role='BOT', prompt='{output}'),
                ]
            )
        ),
        retriever=dict(
            type=FixKRetriever, 
            fix_id_list=[0], # 使用前1个示例
        ),
        inferencer=dict(type=GenInferencer, max_out_len=128000),
        )

    eval_cfg = dict(
            evaluator=dict(type=bio_instruction_Evaluator,path=f'SciReason/bio_instruction/{task}/test/data.json',model_name=MODEL_NAME),
            pred_role='BOT',
            num_gpus=1
            )

    bio_instruction_datasets.append(
            dict(
                type=Bioinstruction_Dataset,
                path= task,
                train_path = f'SciReason/bio_instruction/{task}/dev/data.json',
                test_path=f'SciReason/bio_instruction/{task}/test/data.json',
                hf_hub=True,
                reader_cfg=reader_cfg,
                infer_cfg=infer_cfg,
                eval_cfg=eval_cfg,
            )
        ) 
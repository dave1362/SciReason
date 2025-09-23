# base config for LLM4Chem
from opencompass.openicl.icl_prompt_template import PromptTemplate
from opencompass.openicl.icl_retriever import ZeroRetriever, FixKRetriever
from opencompass.openicl.icl_inferencer import GenInferencer
from opencompass.datasets import LLM4Chem_postprocess, LLM4Chem_Evaluator, LLM4ChemDataset

from opencompass.datasets import LLM4Chem_TASKS, LLM4Chem_TASKS_GENERATION_SETTINGS, LLM4Chem_TASK_TAGS

TASKS = (
    'forward_synthesis',
    'retrosynthesis',
    'molecule_captioning',
    'molecule_generation',
    'name_conversion-i2f',
    'name_conversion-i2s',
    'name_conversion-s2f',
    'name_conversion-s2i',
    'property_prediction-esol',
    'property_prediction-lipo',
    'property_prediction-bbbp',
    'property_prediction-clintox',
    'property_prediction-hiv',
    'property_prediction-sider',
)

TASKS_single = (
    'property_prediction-esol',
    'property_prediction-lipo',
    'property_prediction-bbbp',
    'property_prediction-clintox',
    'property_prediction-hiv',
    'property_prediction-sider',
)


TASK_TAGS = {
    'forward_synthesis': ('<SMILES>', '</SMILES>'),
    'retrosynthesis': ('<SMILES>', '</SMILES>'),
    'molecule_generation': ('<SMILES>', '</SMILES>'),
    'molecule_captioning': ('<answer>', '</answer>'),
    'name_conversion-i2f': ('<MOLFORMULA>', '</MOLFORMULA>'),
    'name_conversion-i2s': ('<SMILES>', '</SMILES>'),
    'name_conversion-s2f': ('<MOLFORMULA>', '</MOLFORMULA>'),
    'name_conversion-s2i': ('<IUPAC>', '</IUPAC>'),
    'property_prediction-esol': ('<NUMBER>', '</NUMBER>'),
    'property_prediction-lipo': ('<NUMBER>', '</NUMBER>'),
    'property_prediction-bbbp': ('<BOOLEAN>', '</BOOLEAN>'),
    'property_prediction-clintox': ('<BOOLEAN>', '</BOOLEAN>'),
    'property_prediction-hiv': ('<BOOLEAN>', '</BOOLEAN>'),
    'property_prediction-sider': ('<BOOLEAN>', '</BOOLEAN>'),
}


all_datasets = []

for task in TASKS:
    generation_kwargs = dict(
        num_return_sequences = 1 if task in TASKS_single else 5,
        # num_beams=5,
        # do_sample=False,
        do_sample=True,
        # top_p=0.90,
        # temperature=0.90,
        # top_k=50,
        # "<|endoftext|>": 151643 "<|im_end|>": 151645
        # eos_token_id=[151643, 151645], # for custom models
    )

    reader_cfg = dict(input_columns=['input'], output_column='output')

    prompt = f'{{input}} Please put the answer within the {TASK_TAGS[task][0]} {TASK_TAGS[task][1]} tags.'

    if task == 'molecule_captioning':
        prompt = f'{{input}} Please put the answer within the <answer> <answer> tags.'
    
    if TASK_TAGS[task][0] == '<BOOLEAN>':
        prompt = prompt + "Answer 'Yes' or 'No'. "

    infer_cfg = dict(
        prompt_template=dict(
            type=PromptTemplate,
            template=dict(
                begin=[
                    # Optional but recommended: A system prompt for better instructions.
                    # dict(role='SYSTEM', fallback_role='HUMAN', prompt='Solve the following questions.'),
                    # The placeholder is the ice_token string itself, used as a direct list element.
                    '</E>',
                ],
                round = [
                    # dict(role='HUMAN', prompt='{input} /no_think'), # for Qwen3
                    dict(role='HUMAN', prompt=prompt),
                ]
            ),
            ice_token="</E>",
        ),
        ice_template=dict(
            type=PromptTemplate,
            template = dict(
                round = [
                    # dict(role='HUMAN', prompt='{input} /no_think'), # for Qwen3
                    dict(role='HUMAN', prompt='{input}'),
                    dict(role='BOT', prompt='{output}'),
                ]
            )
        ),
        # retriever: responsible for retrieving and formatting examples using ice_template
        retriever=dict(
            type=FixKRetriever, 
            fix_id_list=[0, 1, 2, 3, 4], # Use the first 5 examples
            # fix_id_list=[0], # Use the first 1 example, for > 1k test cases
            # type=ZeroRetriever,  # For our trained model, use zero-shot
        ),
        inferencer=dict(
            type=GenInferencer,
            max_out_len=32000,
            generation_kwargs=generation_kwargs,
        ))

    eval_cfg = dict(
        evaluator=dict(type=LLM4Chem_Evaluator, task=task),
        pred_postprocessor=dict(type=LLM4Chem_postprocess, task=task),
        dataset_postprocessor=dict(type=LLM4Chem_postprocess, task=task),
    )

    all_datasets.append(
        dict(
            abbr='smol_'+task,
            type=LLM4ChemDataset,
            train_path = f'SciReason/smol-test/{task}/dev/data.json',
            test_path=f'SciReason/smol-test/{task}/test/data.json',
            hf_hub=True,
            # max_cut=1000, # For debugging
            reader_cfg=reader_cfg,
            infer_cfg=infer_cfg,
            eval_cfg= eval_cfg).copy()
    )

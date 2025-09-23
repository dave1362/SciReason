from opencompass.models import HuggingFacewithChatTemplate

models = [
    dict(
        type=HuggingFacewithChatTemplate,
        abbr='qwen3-0.6b-hf',
        path='Qwen/Qwen3-0.6B',
        max_out_len=32000,
        batch_size=8,
        run_cfg=dict(num_gpus=1),
    )
]
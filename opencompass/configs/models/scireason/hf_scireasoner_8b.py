from opencompass.models import HuggingFacewithChatTemplate

models = [
    dict(
        type=HuggingFacewithChatTemplate,
        abbr='SciReasoner-1.7B',
        path='SciReason/SciReasoner-1.7B',
        # abbr='SciReasoner-8B',
        # path='SciReason/SciReasoner-8B',
        # max_out_len=32000,
        max_out_len=500,
        batch_size=1,
        run_cfg=dict(num_gpus=1),
    )
]
# flake8: noqa
# yapf: disable
from typing import Dict, List, Optional, Union

import torch
from mmengine.device import is_npu_available

from opencompass.models.base import BaseModel, LMTemplateParser
from opencompass.models.base_api import APITemplateParser
from opencompass.registry import MODELS
from opencompass.utils.logging import get_logger
from opencompass.utils.prompt import PromptList

PromptType = Union[PromptList, str]

def _get_meta_template(meta_template):
    default_meta_template = dict(
        round=[
            dict(role='HUMAN', api_role='HUMAN'),
            # XXX: all system roles are mapped to human in purpose
            dict(role='SYSTEM', api_role='HUMAN'),
            dict(role='BOT', api_role='BOT', generate=True),
        ]
    )
    return APITemplateParser(meta_template or default_meta_template)

def _set_model_kwargs_torch_dtype(model_kwargs):
    import torch
    if 'torch_dtype' not in model_kwargs:
        torch_dtype = torch.float
    else:
        torch_dtype = {
            'torch.float16': torch.float16,
            'torch.bfloat16': torch.bfloat16,
            'torch.float': torch.float,
            'auto': 'auto',
            'None': None,
        }.get(model_kwargs['torch_dtype'])
    if torch_dtype is not None:
        model_kwargs['torch_dtype'] = torch_dtype
    return model_kwargs

@MODELS.register_module()
class DummyHuggingFaceModel(BaseModel):
    """A dummy model that mimics HuggingFacewithChatTemplate but returns fixed outputs.
    Used for pipeline testing without downloading real models."""

    def __init__(self,
                 path: str = "dummy-model",
                 tokenizer_only: bool = False,
                 generation_kwargs: dict = dict(),
                 max_seq_len: int = 32000,
                 meta_template: Optional[Dict] = None,
                 **kwargs):
        self.logger = get_logger()
        self.template_parser = _get_meta_template(meta_template)
        self.path = path
        self.tokenizer_only = tokenizer_only
        self.max_seq_len = max_seq_len
        self.generation_kwargs = generation_kwargs
        self.logger.info(f"Dummy model initialized at path: {path}")

    def generate(self,
                 inputs: List[str],
                 max_out_len: int,
                 min_out_len: Optional[int] = None,
                 stopping_criteria: List[str] = [],
                 **kwargs) -> List[str]:
        """Return dummy output for each input."""
        self.logger.info("Dummy generate called, returning fixed outputs")
        return ["DUMMY OUTPUT" for _ in inputs]

    def get_ppl_tokenwise(self,
                          inputs: List[str],
                          label: List[List[int]],
                          mask_length: Optional[List[int]] = None) -> List[float]:
        """Return dummy perplexity scores."""
        self.logger.info("Dummy get_ppl_tokenwise called, returning fixed values")
        return [0.0 for _ in inputs], [1 for _ in inputs]

    def get_token_len(self, prompt: str) -> int:
        """Return a fake token length."""
        return len(prompt) // 4  # arbitrary fake token length

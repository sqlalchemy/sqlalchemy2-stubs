from typing import Any

from . import base as base
from .mock import create_mock_engine as create_mock_engine
from .. import event as event
from .. import exc as exc
from .. import util as util
from ..sql import compiler as compiler

def create_engine(url: Any, **kwargs: Any): ...
def engine_from_config(
    configuration: Any, prefix: str = ..., **kwargs: Any
): ...

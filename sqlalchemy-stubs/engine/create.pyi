from typing import Any
from typing import Union

from . import base as base
from .base import Engine
from .mock import create_mock_engine as create_mock_engine
from .url import URL
from .. import event as event
from .. import exc as exc
from .. import util as util
from ..sql import compiler as compiler

def create_engine(url: Union[str, URL], **kwargs: Any) -> Engine: ...
def engine_from_config(
    configuration: Any, prefix: str = ..., **kwargs: Any
) -> Engine: ...

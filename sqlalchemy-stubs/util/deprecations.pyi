from typing import Any
from typing import Optional

from . import compat as compat
from .langhelpers import decorator as decorator
from .langhelpers import inject_docstring_text as inject_docstring_text
from .langhelpers import inject_param_text as inject_param_text
from .. import exc as exc

SQLALCHEMY_WARN_20: bool

def warn_deprecated(msg: Any, version: Any, stacklevel: int = ...) -> None: ...
def warn_deprecated_limited(
    msg: Any, args: Any, version: Any, stacklevel: int = ...
) -> None: ...
def warn_deprecated_20(msg: Any, stacklevel: int = ...) -> None: ...
def deprecated_cls(version: Any, message: Any, constructor: str = ...): ...
def deprecated_20_cls(
    clsname: Any,
    alternative: Optional[Any] = ...,
    constructor: str = ...,
    becomes_legacy: bool = ...,
): ...
def deprecated(
    version: Any,
    message: Optional[Any] = ...,
    add_deprecation_to_docstring: bool = ...,
    warning: Optional[Any] = ...,
    enable_warnings: bool = ...,
): ...
def moved_20(message: Any, **kw: Any): ...
def deprecated_20(
    api_name: Any,
    alternative: Optional[Any] = ...,
    becomes_legacy: bool = ...,
    **kw: Any,
): ...
def deprecated_params(**specs: Any): ...

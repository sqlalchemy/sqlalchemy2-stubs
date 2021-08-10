from typing import Any
from typing import Callable

from .session import _AsyncSessionProxy
from .session import AsyncSession
from ...orm.scoping import ScopedSessionMixin
from ...util import ScopedRegistry

class async_scoped_session(
    _AsyncSessionProxy, ScopedSessionMixin[AsyncSession]
):
    session_factory: Callable[..., AsyncSession] = ...
    registry: ScopedRegistry = ...
    def __init__(
        self,
        session_factory: Callable[..., AsyncSession],
        scopefunc: Callable[..., Any] = ...,
    ) -> None: ...
    async def remove(self) -> None: ...

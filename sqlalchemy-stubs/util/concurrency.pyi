from . import compat as compat
from ._concurrency_py3k import AsyncAdaptedLock as AsyncAdaptedLock
from ._concurrency_py3k import asyncio as asyncio
from ._concurrency_py3k import await_fallback as await_fallback
from ._concurrency_py3k import await_only as await_only
from ._concurrency_py3k import greenlet_spawn as greenlet_spawn

have_greenlet: bool

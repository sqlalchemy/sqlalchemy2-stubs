import base64
import collections
from collections import namedtuple
import contextlib
from datetime import tzinfo
from functools import reduce
import itertools
from StringIO import StringIO as StringIO
from typing import Any
from typing import Optional
from urllib import quote as quote
from urllib import quote_plus as quote_plus
from urllib import unquote as unquote
from urllib import unquote_plus as unquote_plus
from urlparse import parse_qsl as parse_qsl

py38: Any
py37: Any
py3k: Any
py2k: Any
pypy: Any
cpython: Any
win32: Any
osx: Any
arm: Any
has_refcount_gc: Any
contextmanager = contextlib.contextmanager
dottedgetter: Any
namedtuple = collections.namedtuple
next = next

FullArgSpec = namedtuple(
    "FullArgSpec",
    [
        "args",
        "varargs",
        "varkw",
        "defaults",
        "kwonlyargs",
        "kwonlydefaults",
        "annotations",
    ],
)

class nullcontext:
    enter_result: Any = ...
    def __init__(self, enter_result: Optional[Any] = ...) -> None: ...
    def __enter__(self): ...
    def __exit__(self, *excinfo: Any) -> None: ...

def inspect_getfullargspec(func: Any): ...

string_types: Any
binary_types: Any
binary_type = bytes
text_type = str
int_types: Any
iterbytes = iter
long_type = int
itertools_filterfalse = itertools.filterfalse
itertools_filter = filter
itertools_imap = map
exec_: Any
import_: Any
print_: Any

def b(s: Any): ...
def b64decode(x: Any): ...
def b64encode(x: Any): ...
def decode_backslashreplace(text: Any, encoding: Any): ...
def cmp(a: Any, b: Any): ...
def raise_(
    exception: Any,
    with_traceback: Optional[Any] = ...,
    replace_context: Optional[Any] = ...,
    from_: bool = ...,
) -> None: ...
def u(s: Any): ...
def ue(s: Any): ...

callable = callable

class ABC:
    __metaclass__: Any = ...

binary_type = str
text_type = unicode
long_type = long
callable = callable
cmp = cmp
reduce = reduce
b64encode = base64.b64encode
b64decode = base64.b64decode

def safe_bytestring(text: Any): ...
def inspect_formatargspec(
    args: Any,
    varargs: Optional[Any] = ...,
    varkw: Optional[Any] = ...,
    defaults: Optional[Any] = ...,
    kwonlyargs: Any = ...,
    kwonlydefaults: Any = ...,
    annotations: Any = ...,
    formatarg: Any = ...,
    formatvarargs: Any = ...,
    formatvarkw: Any = ...,
    formatvalue: Any = ...,
    formatreturns: Any = ...,
    formatannotation: Any = ...,
): ...
def dataclass_fields(cls): ...
def local_dataclass_fields(cls): ...
def raise_from_cause(
    exception: Any, exc_info: Optional[Any] = ...
) -> None: ...
def reraise(
    tp: Any, value: Any, tb: Optional[Any] = ..., cause: Optional[Any] = ...
) -> None: ...
def with_metaclass(meta: Any, *bases: Any, **kw: Any): ...

class timezone(tzinfo):
    def __init__(self, offset: Any) -> None: ...
    def __eq__(self, other: Any) -> Any: ...
    def __hash__(self) -> Any: ...
    def utcoffset(self, dt: Any): ...
    def tzname(self, dt: Any): ...
    def dst(self, dt: Any) -> None: ...
    def fromutc(self, dt: Any): ...

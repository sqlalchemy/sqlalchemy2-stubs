from typing import Any

from ... import types as sqltypes

class JSON(sqltypes.JSON): ...

class _FormatTypeMixin:
    def bind_processor(self, dialect: Any): ...
    def literal_processor(self, dialect: Any): ...

class JSONIndexType(_FormatTypeMixin, sqltypes.JSON.JSONIndexType): ...
class JSONPathType(_FormatTypeMixin, sqltypes.JSON.JSONPathType): ...

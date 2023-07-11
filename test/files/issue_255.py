from __future__ import annotations

from typing import Any

from sqlalchemy.ext.mutable import Mutable


class Issue255(Mutable):

    @classmethod
    def coerce(cls, key: str, value: Any) -> str | None:
        if value is None:
            return None
        return str(value)

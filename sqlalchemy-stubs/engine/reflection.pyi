from typing import Any
from typing import Collection
from typing import Dict
from typing import List
from typing import Optional
from typing import Set
from typing import Tuple
from typing import Type
from typing import TypeVar

from .base import Connectable
from ..sql.schema import Table

_TInspector = TypeVar("_TInspector", bound=Inspector)

def cache(fn: Any, self: Any, con: Any, *args: Any, **kw: Any) -> Any: ...

class Inspector:
    def __init__(self, bind: Connectable): ...
    @classmethod
    def from_engine(
        cls: Type[_TInspector], bind: Connectable
    ) -> _TInspector: ...
    @property
    def default_schema_name(self) -> str: ...
    def get_schema_names(self) -> List[str]: ...
    def get_table_names(self, schema: Optional[str] = ...) -> List[str]: ...
    def has_table(
        self, table_name: str, schema: Optional[str] = ...
    ) -> bool: ...
    def has_sequence(
        self, sequence_name: str, schema: Optional[str] = ...
    ) -> bool: ...
    def get_sorted_table_and_fkc_names(
        self, schema: Optional[str] = ...
    ) -> List[Tuple[Optional[str], List[Tuple[str, str]]]]: ...
    def get_temp_table_names(self) -> List[str]: ...
    def get_temp_view_names(self) -> List[str]: ...
    def get_table_options(
        self, table_name: str, schema: Optional[str] = ..., **kw: Any
    ) -> Dict[str, Any]: ...
    def get_view_names(self, schema: Optional[str] = ...) -> List[str]: ...
    def get_sequence_names(self, schema: Optional[str] = ...) -> List[str]: ...
    def get_view_definition(
        self, view_name: str, schema: Optional[str] = ...
    ) -> Any: ...
    def get_columns(
        self, table_name: str, schema: Optional[str] = ..., **kw: Any
    ) -> List[Dict[str, Any]]: ...
    def get_pk_constraint(
        self, table_name: str, schema: Optional[str] = ..., **kw: Any
    ) -> Dict[str, Any]: ...
    def get_foreign_keys(
        self, table_name: str, schema: Optional[str] = ..., **kw: Any
    ) -> List[Dict[str, Any]]: ...
    def get_indexes(
        self, table_name: str, schema: Optional[str] = ..., **kw: Any
    ) -> List[Dict[str, Any]]: ...
    def get_unique_constraints(
        self, table_name: str, schema: Optional[str] = ..., **kw: Any
    ) -> List[Dict[str, Any]]: ...
    def get_table_comment(
        self, table_name: str, schema: Optional[str] = ..., **kw: Any
    ) -> Dict[str, Any]: ...
    def get_check_constraints(
        self, table_name: str, schema: Optional[str] = ..., **kw: Any
    ) -> List[Dict[str, Any]]: ...
    def reflecttable(
        self,
        table: Table,
        include_columns: Optional[Collection[str]],
        exclude_columns: Collection[str] = ...,
        resolve_fks: bool = ...,
        _extend_on: Set[Table] = ...,
    ) -> None: ...
    def reflect_table(
        self,
        table: Table,
        include_columns: Optional[Collection[str]],
        exclude_columns: Collection[str] = ...,
        resolve_fks: bool = ...,
        _extend_on: Set[Table] = ...,
    ) -> None: ...

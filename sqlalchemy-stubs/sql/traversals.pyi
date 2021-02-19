from typing import Any

from . import operators as operators
from .visitors import ExtendedInternalTraversal as ExtendedInternalTraversal
from .visitors import InternalTraversal as InternalTraversal
from .. import util as util
from ..inspection import inspect as inspect
from ..util import collections_abc as collections_abc
from ..util import HasMemoized as HasMemoized
from ..util import py37 as py37

SKIP_TRAVERSE: Any
COMPARE_FAILED: bool
COMPARE_SUCCEEDED: bool
NO_CACHE: Any
CACHE_IN_PLACE: Any
CALL_GEN_CACHE_KEY: Any
STATIC_CACHE_KEY: Any
PROPAGATE_ATTRS: Any
ANON_NAME: Any

def compare(obj1: Any, obj2: Any, **kw: Any): ...

class HasCacheKey: ...
class MemoizedHasCacheKey(HasCacheKey, HasMemoized): ...

class CacheKey:
    def __hash__(self) -> Any: ...
    def to_offline_string(
        self, statement_cache: Any, statement: Any, parameters: Any
    ): ...
    def __eq__(self, other: Any) -> Any: ...

class _CacheKey(ExtendedInternalTraversal):
    visit_has_cache_key: Any = ...
    visit_clauseelement: Any = ...
    visit_clauseelement_list: Any = ...
    visit_annotations_key: Any = ...
    visit_clauseelement_tuple: Any = ...
    visit_string: Any = ...
    visit_boolean: Any = ...
    visit_operator: Any = ...
    visit_plain_obj: Any = ...
    visit_statement_hint_list: Any = ...
    visit_type: Any = ...
    visit_anon_name: Any = ...
    visit_propagate_attrs: Any = ...
    def visit_inspectable(
        self,
        attrname: Any,
        obj: Any,
        parent: Any,
        anon_map: Any,
        bindparams: Any,
    ): ...
    def visit_string_list(
        self,
        attrname: Any,
        obj: Any,
        parent: Any,
        anon_map: Any,
        bindparams: Any,
    ): ...
    def visit_multi(
        self,
        attrname: Any,
        obj: Any,
        parent: Any,
        anon_map: Any,
        bindparams: Any,
    ): ...
    def visit_multi_list(
        self,
        attrname: Any,
        obj: Any,
        parent: Any,
        anon_map: Any,
        bindparams: Any,
    ): ...
    def visit_has_cache_key_tuples(
        self,
        attrname: Any,
        obj: Any,
        parent: Any,
        anon_map: Any,
        bindparams: Any,
    ): ...
    def visit_has_cache_key_list(
        self,
        attrname: Any,
        obj: Any,
        parent: Any,
        anon_map: Any,
        bindparams: Any,
    ): ...
    visit_executable_options: Any = ...
    def visit_inspectable_list(
        self,
        attrname: Any,
        obj: Any,
        parent: Any,
        anon_map: Any,
        bindparams: Any,
    ): ...
    def visit_clauseelement_tuples(
        self,
        attrname: Any,
        obj: Any,
        parent: Any,
        anon_map: Any,
        bindparams: Any,
    ): ...
    def visit_fromclause_ordered_set(
        self,
        attrname: Any,
        obj: Any,
        parent: Any,
        anon_map: Any,
        bindparams: Any,
    ): ...
    def visit_clauseelement_unordered_set(
        self,
        attrname: Any,
        obj: Any,
        parent: Any,
        anon_map: Any,
        bindparams: Any,
    ): ...
    def visit_named_ddl_element(
        self,
        attrname: Any,
        obj: Any,
        parent: Any,
        anon_map: Any,
        bindparams: Any,
    ): ...
    def visit_prefix_sequence(
        self,
        attrname: Any,
        obj: Any,
        parent: Any,
        anon_map: Any,
        bindparams: Any,
    ): ...
    def visit_setup_join_tuple(
        self,
        attrname: Any,
        obj: Any,
        parent: Any,
        anon_map: Any,
        bindparams: Any,
    ): ...
    def visit_table_hint_list(
        self,
        attrname: Any,
        obj: Any,
        parent: Any,
        anon_map: Any,
        bindparams: Any,
    ): ...
    def visit_plain_dict(
        self,
        attrname: Any,
        obj: Any,
        parent: Any,
        anon_map: Any,
        bindparams: Any,
    ): ...
    def visit_dialect_options(
        self,
        attrname: Any,
        obj: Any,
        parent: Any,
        anon_map: Any,
        bindparams: Any,
    ): ...
    def visit_string_clauseelement_dict(
        self,
        attrname: Any,
        obj: Any,
        parent: Any,
        anon_map: Any,
        bindparams: Any,
    ): ...
    def visit_string_multi_dict(
        self,
        attrname: Any,
        obj: Any,
        parent: Any,
        anon_map: Any,
        bindparams: Any,
    ): ...
    def visit_fromclause_canonical_column_collection(
        self,
        attrname: Any,
        obj: Any,
        parent: Any,
        anon_map: Any,
        bindparams: Any,
    ): ...
    def visit_unknown_structure(
        self,
        attrname: Any,
        obj: Any,
        parent: Any,
        anon_map: Any,
        bindparams: Any,
    ): ...
    def visit_dml_ordered_values(
        self,
        attrname: Any,
        obj: Any,
        parent: Any,
        anon_map: Any,
        bindparams: Any,
    ): ...
    def visit_dml_values(
        self,
        attrname: Any,
        obj: Any,
        parent: Any,
        anon_map: Any,
        bindparams: Any,
    ): ...
    def visit_dml_multi_values(
        self,
        attrname: Any,
        obj: Any,
        parent: Any,
        anon_map: Any,
        bindparams: Any,
    ): ...

class HasCopyInternals: ...

class _CopyInternals(InternalTraversal):
    def visit_clauseelement(
        self,
        attrname: Any,
        parent: Any,
        element: Any,
        clone: Any = ...,
        **kw: Any,
    ): ...
    def visit_clauseelement_list(
        self,
        attrname: Any,
        parent: Any,
        element: Any,
        clone: Any = ...,
        **kw: Any,
    ): ...
    def visit_clauseelement_tuple(
        self,
        attrname: Any,
        parent: Any,
        element: Any,
        clone: Any = ...,
        **kw: Any,
    ): ...
    def visit_executable_options(
        self,
        attrname: Any,
        parent: Any,
        element: Any,
        clone: Any = ...,
        **kw: Any,
    ): ...
    def visit_clauseelement_unordered_set(
        self,
        attrname: Any,
        parent: Any,
        element: Any,
        clone: Any = ...,
        **kw: Any,
    ): ...
    def visit_clauseelement_tuples(
        self,
        attrname: Any,
        parent: Any,
        element: Any,
        clone: Any = ...,
        **kw: Any,
    ): ...
    def visit_string_clauseelement_dict(
        self,
        attrname: Any,
        parent: Any,
        element: Any,
        clone: Any = ...,
        **kw: Any,
    ): ...
    def visit_setup_join_tuple(
        self,
        attrname: Any,
        parent: Any,
        element: Any,
        clone: Any = ...,
        **kw: Any,
    ): ...
    def visit_dml_ordered_values(
        self,
        attrname: Any,
        parent: Any,
        element: Any,
        clone: Any = ...,
        **kw: Any,
    ): ...
    def visit_dml_values(
        self,
        attrname: Any,
        parent: Any,
        element: Any,
        clone: Any = ...,
        **kw: Any,
    ): ...
    def visit_dml_multi_values(
        self,
        attrname: Any,
        parent: Any,
        element: Any,
        clone: Any = ...,
        **kw: Any,
    ): ...
    def visit_propagate_attrs(
        self,
        attrname: Any,
        parent: Any,
        element: Any,
        clone: Any = ...,
        **kw: Any,
    ): ...

class _GetChildren(InternalTraversal):
    def visit_has_cache_key(self, element: Any, **kw: Any): ...
    def visit_clauseelement(self, element: Any, **kw: Any): ...
    def visit_clauseelement_list(self, element: Any, **kw: Any): ...
    def visit_clauseelement_tuple(self, element: Any, **kw: Any): ...
    def visit_clauseelement_tuples(self, element: Any, **kw: Any): ...
    def visit_fromclause_canonical_column_collection(
        self, element: Any, **kw: Any
    ): ...
    def visit_string_clauseelement_dict(self, element: Any, **kw: Any): ...
    def visit_fromclause_ordered_set(self, element: Any, **kw: Any): ...
    def visit_clauseelement_unordered_set(self, element: Any, **kw: Any): ...
    def visit_setup_join_tuple(self, element: Any, **kw: Any) -> None: ...
    def visit_dml_ordered_values(self, element: Any, **kw: Any) -> None: ...
    def visit_dml_values(self, element: Any, **kw: Any) -> None: ...
    def visit_dml_multi_values(self, element: Any, **kw: Any): ...
    def visit_propagate_attrs(self, element: Any, **kw: Any): ...

class anon_map(dict):
    index: int = ...
    def __init__(self) -> None: ...
    def __missing__(self, key: Any): ...

class TraversalComparatorStrategy(InternalTraversal, util.MemoizedSlots):
    stack: Any = ...
    cache: Any = ...
    def __init__(self) -> None: ...
    def compare(self, obj1: Any, obj2: Any, **kw: Any): ...
    def compare_inner(self, obj1: Any, obj2: Any, **kw: Any): ...
    def visit_has_cache_key(
        self,
        attrname: Any,
        left_parent: Any,
        left: Any,
        right_parent: Any,
        right: Any,
        **kw: Any,
    ): ...
    def visit_propagate_attrs(
        self,
        attrname: Any,
        left_parent: Any,
        left: Any,
        right_parent: Any,
        right: Any,
        **kw: Any,
    ): ...
    def visit_has_cache_key_list(
        self,
        attrname: Any,
        left_parent: Any,
        left: Any,
        right_parent: Any,
        right: Any,
        **kw: Any,
    ): ...
    visit_executable_options: Any = ...
    def visit_clauseelement(
        self,
        attrname: Any,
        left_parent: Any,
        left: Any,
        right_parent: Any,
        right: Any,
        **kw: Any,
    ) -> None: ...
    def visit_fromclause_canonical_column_collection(
        self,
        attrname: Any,
        left_parent: Any,
        left: Any,
        right_parent: Any,
        right: Any,
        **kw: Any,
    ) -> None: ...
    def visit_fromclause_derived_column_collection(
        self,
        attrname: Any,
        left_parent: Any,
        left: Any,
        right_parent: Any,
        right: Any,
        **kw: Any,
    ) -> None: ...
    def visit_string_clauseelement_dict(
        self,
        attrname: Any,
        left_parent: Any,
        left: Any,
        right_parent: Any,
        right: Any,
        **kw: Any,
    ): ...
    def visit_clauseelement_tuples(
        self,
        attrname: Any,
        left_parent: Any,
        left: Any,
        right_parent: Any,
        right: Any,
        **kw: Any,
    ): ...
    def visit_clauseelement_list(
        self,
        attrname: Any,
        left_parent: Any,
        left: Any,
        right_parent: Any,
        right: Any,
        **kw: Any,
    ) -> None: ...
    def visit_clauseelement_tuple(
        self,
        attrname: Any,
        left_parent: Any,
        left: Any,
        right_parent: Any,
        right: Any,
        **kw: Any,
    ) -> None: ...
    def visit_clauseelement_unordered_set(
        self,
        attrname: Any,
        left_parent: Any,
        left: Any,
        right_parent: Any,
        right: Any,
        **kw: Any,
    ): ...
    def visit_fromclause_ordered_set(
        self,
        attrname: Any,
        left_parent: Any,
        left: Any,
        right_parent: Any,
        right: Any,
        **kw: Any,
    ) -> None: ...
    def visit_string(
        self,
        attrname: Any,
        left_parent: Any,
        left: Any,
        right_parent: Any,
        right: Any,
        **kw: Any,
    ): ...
    def visit_string_list(
        self,
        attrname: Any,
        left_parent: Any,
        left: Any,
        right_parent: Any,
        right: Any,
        **kw: Any,
    ): ...
    def visit_anon_name(
        self,
        attrname: Any,
        left_parent: Any,
        left: Any,
        right_parent: Any,
        right: Any,
        **kw: Any,
    ): ...
    def visit_boolean(
        self,
        attrname: Any,
        left_parent: Any,
        left: Any,
        right_parent: Any,
        right: Any,
        **kw: Any,
    ): ...
    def visit_operator(
        self,
        attrname: Any,
        left_parent: Any,
        left: Any,
        right_parent: Any,
        right: Any,
        **kw: Any,
    ): ...
    def visit_type(
        self,
        attrname: Any,
        left_parent: Any,
        left: Any,
        right_parent: Any,
        right: Any,
        **kw: Any,
    ): ...
    def visit_plain_dict(
        self,
        attrname: Any,
        left_parent: Any,
        left: Any,
        right_parent: Any,
        right: Any,
        **kw: Any,
    ): ...
    def visit_dialect_options(
        self,
        attrname: Any,
        left_parent: Any,
        left: Any,
        right_parent: Any,
        right: Any,
        **kw: Any,
    ): ...
    def visit_annotations_key(
        self,
        attrname: Any,
        left_parent: Any,
        left: Any,
        right_parent: Any,
        right: Any,
        **kw: Any,
    ): ...
    def visit_plain_obj(
        self,
        attrname: Any,
        left_parent: Any,
        left: Any,
        right_parent: Any,
        right: Any,
        **kw: Any,
    ): ...
    def visit_named_ddl_element(
        self,
        attrname: Any,
        left_parent: Any,
        left: Any,
        right_parent: Any,
        right: Any,
        **kw: Any,
    ): ...
    def visit_prefix_sequence(
        self,
        attrname: Any,
        left_parent: Any,
        left: Any,
        right_parent: Any,
        right: Any,
        **kw: Any,
    ): ...
    def visit_setup_join_tuple(
        self,
        attrname: Any,
        left_parent: Any,
        left: Any,
        right_parent: Any,
        right: Any,
        **kw: Any,
    ): ...
    def visit_table_hint_list(
        self,
        attrname: Any,
        left_parent: Any,
        left: Any,
        right_parent: Any,
        right: Any,
        **kw: Any,
    ): ...
    def visit_statement_hint_list(
        self,
        attrname: Any,
        left_parent: Any,
        left: Any,
        right_parent: Any,
        right: Any,
        **kw: Any,
    ): ...
    def visit_unknown_structure(
        self,
        attrname: Any,
        left_parent: Any,
        left: Any,
        right_parent: Any,
        right: Any,
        **kw: Any,
    ) -> None: ...
    def visit_dml_ordered_values(
        self,
        attrname: Any,
        left_parent: Any,
        left: Any,
        right_parent: Any,
        right: Any,
        **kw: Any,
    ): ...
    def visit_dml_values(
        self,
        attrname: Any,
        left_parent: Any,
        left: Any,
        right_parent: Any,
        right: Any,
        **kw: Any,
    ): ...
    def visit_dml_multi_values(
        self,
        attrname: Any,
        left_parent: Any,
        left: Any,
        right_parent: Any,
        right: Any,
        **kw: Any,
    ): ...
    def compare_clauselist(self, left: Any, right: Any, **kw: Any): ...
    def compare_binary(self, left: Any, right: Any, **kw: Any): ...
    def compare_bindparam(self, left: Any, right: Any, **kw: Any): ...

class ColIdentityComparatorStrategy(TraversalComparatorStrategy):
    def compare_column_element(
        self,
        left: Any,
        right: Any,
        use_proxies: bool = ...,
        equivalents: Any = ...,
        **kw: Any,
    ): ...
    def compare_column(self, left: Any, right: Any, **kw: Any): ...
    def compare_label(self, left: Any, right: Any, **kw: Any): ...
    def compare_table(self, left: Any, right: Any, **kw: Any): ...

from typing import Any
from typing import Optional

from .attributes import AttributeEvent as AttributeEvent
from .attributes import InstrumentedAttribute as InstrumentedAttribute
from .attributes import Mapped as Mapped
from .attributes import QueryableAttribute as QueryableAttribute
from .context import QueryContext as QueryContext
from .decl_api import as_declarative as as_declarative
from .decl_api import declarative_base as declarative_base
from .decl_api import declared_attr as declared_attr
from .decl_api import has_inherited_table as has_inherited_table
from .decl_api import registry as registry
from .decl_api import synonym_for as synonym_for
from .descriptor_props import CompositeProperty as CompositeProperty
from .descriptor_props import SynonymProperty as SynonymProperty
from .events import AttributeEvents as AttributeEvents
from .events import InstanceEvents as InstanceEvents
from .events import InstrumentationEvents as InstrumentationEvents
from .events import MapperEvents as MapperEvents
from .events import QueryEvents as QueryEvents
from .events import SessionEvents as SessionEvents
from .identity import IdentityMap as IdentityMap
from .instrumentation import ClassManager as ClassManager
from .interfaces import EXT_CONTINUE as EXT_CONTINUE
from .interfaces import EXT_SKIP as EXT_SKIP
from .interfaces import EXT_STOP as EXT_STOP
from .interfaces import InspectionAttr as InspectionAttr
from .interfaces import InspectionAttrInfo as InspectionAttrInfo
from .interfaces import MANYTOMANY as MANYTOMANY
from .interfaces import MANYTOONE as MANYTOONE
from .interfaces import MapperProperty as MapperProperty
from .interfaces import NOT_EXTENSION as NOT_EXTENSION
from .interfaces import ONETOMANY as ONETOMANY
from .interfaces import PropComparator as PropComparator
from .loading import merge_frozen_result as merge_frozen_result
from .loading import merge_result as merge_result
from .mapper import class_mapper as class_mapper
from .mapper import configure_mappers as configure_mappers
from .mapper import Mapper as Mapper
from .mapper import reconstructor as reconstructor
from .mapper import validates as validates
from .properties import ColumnProperty as ColumnProperty
from .query import AliasOption as AliasOption
from .query import FromStatement as FromStatement
from .query import Query as Query
from .relationships import foreign as foreign
from .relationships import RelationshipProperty as RelationshipProperty
from .relationships import remote as remote
from .scoping import scoped_session as scoped_session
from .session import close_all_sessions as close_all_sessions
from .session import make_transient as make_transient
from .session import make_transient_to_detached as make_transient_to_detached
from .session import object_session as object_session
from .session import ORMExecuteState as ORMExecuteState
from .session import Session as Session
from .session import sessionmaker as sessionmaker
from .session import SessionTransaction as SessionTransaction
from .state import AttributeState as AttributeState
from .state import InstanceState as InstanceState
from .strategy_options import Load as Load
from .unitofwork import UOWTransaction as UOWTransaction
from .util import aliased as aliased
from .util import Bundle as Bundle
from .util import CascadeOptions as CascadeOptions
from .util import join as join
from .util import LoaderCriteriaOption as LoaderCriteriaOption
from .util import object_mapper as object_mapper
from .util import outerjoin as outerjoin
from .util import polymorphic_union as polymorphic_union
from .util import was_deleted as was_deleted
from .util import with_parent as with_parent
from .util import with_polymorphic as with_polymorphic
from ..util.langhelpers import public_factory as public_factory

def create_session(bind: Optional[Any] = ..., **kwargs: Any): ...

with_loader_criteria: Any
relationship: Any

def relation(*arg: Any, **kw: Any): ...
def dynamic_loader(argument: Any, **kw: Any): ...

column_property: Any
composite: Any

def backref(name: Any, **kwargs: Any): ...
def deferred(*columns: Any, **kw: Any): ...
def query_expression(default_expr: Any = ...): ...

mapper: Any
synonym: Any

def clear_mappers() -> None: ...

joinedload: Any
contains_eager: Any
defer: Any
undefer: Any
undefer_group: Any
with_expression: Any
load_only: Any
lazyload: Any
subqueryload: Any
selectinload: Any
immediateload: Any
noload: Any
raiseload: Any
defaultload: Any
selectin_polymorphic: Any

def eagerload(*args: Any, **kwargs: Any): ...

contains_alias: Any

# Names in __all__ with no definition:
#   AppenderQuery

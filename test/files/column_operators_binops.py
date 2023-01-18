from sqlalchemy import ARRAY
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import registry
from sqlalchemy.sql import ColumnElement

mapper_registry: registry = registry()


@mapper_registry.mapped
class A:
    __tablename__ = "a"
    id = Column(Integer, primary_key=True)
    string = Column(String, primary_key=True)
    arr = Column(ARRAY(Integer), primary_key=True)


lt1: "ColumnElement[Boolean]" = A.id > A.id
lt2: "ColumnElement[Boolean]" = A.id > 1
lt3: "ColumnElement[Boolean]" = 1 < A.id

le1: "ColumnElement[Boolean]" = A.id >= A.id
le2: "ColumnElement[Boolean]" = A.id >= 1
le3: "ColumnElement[Boolean]" = 1 <= A.id

eq1: "ColumnElement[Boolean]" = A.id == A.id
eq2: "ColumnElement[Boolean]" = A.id == 1
# this changes based on QueryableAttribute(Any) lineage
# eq3: "bool" = 1 == A.id

ne1: "ColumnElement[Boolean]" = A.id != A.id
ne2: "ColumnElement[Boolean]" = A.id != 1
# this changes based on QueryableAttribute(Any) lineage
# ne3: "bool" = 1 != A.id

gt1: "ColumnElement[Boolean]" = A.id < A.id
gt2: "ColumnElement[Boolean]" = A.id < 1
gt3: "ColumnElement[Boolean]" = 1 > A.id

ge1: "ColumnElement[Boolean]" = A.id <= A.id
ge2: "ColumnElement[Boolean]" = A.id <= 1
ge3: "ColumnElement[Boolean]" = 1 >= A.id


# contains
# TODO "in" doesn't seem to pick up the typing of __contains__?
#  but also seems to be related to Array, as it works with Integer.
#  error: Access to generic instance variables via class is ambiguous
#  error: Incompatible types in assignment (expression has type "bool", variable has type "ColumnElement[Boolean]")  # noqa
# contains1: "ColumnElement[Boolean]" = A.id in A.arr

lshift1: "ColumnElement[Integer]" = A.id << A.id
lshift2: "ColumnElement[Integer]" = A.id << 1

rshift1: "ColumnElement[Integer]" = A.id >> A.id
rshift2: "ColumnElement[Integer]" = A.id >> 1

concat1: "ColumnElement[String]" = A.string.concat(A.string)
concat2: "ColumnElement[String]" = A.string.concat(1)
concat3: "ColumnElement[String]" = A.string.concat("a")

like1: "ColumnElement[Boolean]" = A.string.like("test")
like2: "ColumnElement[Boolean]" = A.string.like("test", escape="/")
ilike1: "ColumnElement[Boolean]" = A.string.ilike("test")
ilike2: "ColumnElement[Boolean]" = A.string.ilike("test", escape="/")

in_: "ColumnElement[Boolean]" = A.id.in_([1, 2])
not_in: "ColumnElement[Boolean]" = A.id.not_in([1, 2])

not_like1: "ColumnElement[Boolean]" = A.string.not_like("test")
not_like2: "ColumnElement[Boolean]" = A.string.not_like("test", escape="/")
not_ilike1: "ColumnElement[Boolean]" = A.string.not_ilike("test")
not_ilike2: "ColumnElement[Boolean]" = A.string.not_ilike("test", escape="/")

is_: "ColumnElement[Boolean]" = A.string.is_("test")
is_not: "ColumnElement[Boolean]" = A.string.is_not("test")

startswith: "ColumnElement[Boolean]" = A.string.startswith("test")
endswith: "ColumnElement[Boolean]" = A.string.endswith("test")
contains: "ColumnElement[Boolean]" = A.string.contains("test")
match: "ColumnElement[Boolean]" = A.string.match("test")
regexp_match: "ColumnElement[Boolean]" = A.string.regexp_match("test")

regexp_replace: "ColumnElement[String]" = A.string.regexp_replace(
    "pattern", "replacement"
)
between: "ColumnElement[Boolean]" = A.string.between("a", "b")

# TODO Not sure why we can safely assign this to a String?
#  add1: "ColumnElement[String]" = A.id + A.id
add1: "ColumnElement[Integer]" = A.id + A.id
add2: "ColumnElement[Integer]" = A.id + 1
add3: "ColumnElement[Integer]" = 1 + A.id

sub1: "ColumnElement[Integer]" = A.id - A.id
sub2: "ColumnElement[Integer]" = A.id - 1
sub3: "ColumnElement[Integer]" = 1 - A.id

mul1: "ColumnElement[Integer]" = A.id * A.id
mul2: "ColumnElement[Integer]" = A.id * 1
mul3: "ColumnElement[Integer]" = 1 * A.id

div1: "ColumnElement[Integer]" = A.id / A.id
div2: "ColumnElement[Integer]" = A.id / 1
div3: "ColumnElement[Integer]" = 1 / A.id

mod1: "ColumnElement[Integer]" = A.id % A.id
mod2: "ColumnElement[Integer]" = A.id % 1
mod3: "ColumnElement[Integer]" = 1 % A.id

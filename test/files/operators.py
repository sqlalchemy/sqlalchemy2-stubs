from sqlalchemy.sql import column, ColumnElement
from sqlalchemy.types import Integer, BigInteger, String

col = column("flags", Integer)
a: "ColumnElement[Integer]" = col.op("&")(1)
b: "ColumnElement[Integer]" = col.op("&", return_type=Integer)(1)
c: "ColumnElement[String]" = col.op("&", return_type=String)(1)
d: "ColumnElement[BigInteger]" = col.op("&", return_type=BigInteger)(1)

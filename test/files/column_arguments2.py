from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String

Column("name", Integer, index=True)
# EXPECTED_MYPY: No overload variant of "Column" matches argument types "None", "str"  # noqa E501
Column(None, name="name")
Column(Integer, name="name", index=True)
Column("name", ForeignKey("a.id"))
Column(ForeignKey("a.id"), type_=None, index=True)
Column(ForeignKey("a.id"), name="name", type_=Integer())
# EXPECTED_MYPY: No overload variant of "Column" matches argument types "str", "None"  # noqa E501
Column("name", None)
Column("name", index=True)
Column(ForeignKey("a.id"), name="name", index=True)
Column(type_=None, index=True)
# EXPECTED_MYPY: No overload variant of "Column" matches argument types "None", "ForeignKey"  # noqa E501
Column(None, ForeignKey("a.id"))
Column("name")
Column(name="name", type_=None, index=True)
Column(ForeignKey("a.id"), name="name", type_=None)
Column(Integer)
Column(ForeignKey("a.id"), type_=Integer())
Column("name", Integer, ForeignKey("a.id"), index=True)
# EXPECTED_MYPY: No overload variant of "Column" matches argument types "str", "None", "ForeignKey", "bool  # noqa E501
Column("name", None, ForeignKey("a.id"), index=True)
Column(ForeignKey("a.id"), index=True)
Column("name", Integer)
Column(Integer, name="name")
Column(Integer, ForeignKey("a.id"), name="name", index=True)
Column(ForeignKey("a.id"), type_=None)
Column(ForeignKey("a.id"), name="name")
Column(name="name", index=True)
Column(type_=None)
# EXPECTED_MYPY: No overload variant of "Column" matches argument types "None", "bool"  # noqa E501
Column(None, index=True)
Column(name="name", type_=None)
Column(type_=Integer(), index=True)
Column("name", Integer, ForeignKey("a.id"))
Column(name="name", type_=Integer(), index=True)
Column(Integer, ForeignKey("a.id"), index=True)
# EXPECTED_MYPY: No overload variant of "Column" matches argument types "str", "None", "ForeignKey"  # noqa E501
Column("name", None, ForeignKey("a.id"))
Column(index=True)
Column("name", type_=None, index=True)
Column("name", ForeignKey("a.id"), type_=Integer(), index=True)
Column(ForeignKey("a.id"))
Column(Integer, ForeignKey("a.id"))
Column(Integer, ForeignKey("a.id"), name="name")
Column("name", ForeignKey("a.id"), index=True)
Column("name", type_=Integer(), index=True)
Column(ForeignKey("a.id"), name="name", type_=Integer(), index=True)
Column(name="name")
# EXPECTED_MYPY: No overload variant of "Column" matches argument types "str", "None", "bool"  # noqa E501
Column("name", None, index=True)
Column("name", ForeignKey("a.id"), type_=None, index=True)
Column("name", type_=Integer())
# EXPECTED_MYPY: No overload variant of "Column" matches argument type "None"
Column(None)
# EXPECTED_MYPY: No overload variant of "Column" matches argument types "None", "ForeignKey", "bool"  # noqa E501
Column(None, ForeignKey("a.id"), index=True)
Column("name", ForeignKey("a.id"), type_=None)
Column(type_=Integer())
# EXPECTED_MYPY: No overload variant of "Column" matches argument types "None", "ForeignKey", "str", "bool"  # noqa E501
Column(None, ForeignKey("a.id"), name="name", index=True)
Column(Integer, index=True)
Column(ForeignKey("a.id"), name="name", type_=None, index=True)
Column(ForeignKey("a.id"), type_=Integer(), index=True)
Column(name="name", type_=Integer())
# EXPECTED_MYPY: No overload variant of "Column" matches argument types "None", "str", "bool"  # noqa E501
Column(None, name="name", index=True)
Column()
# EXPECTED_MYPY: No overload variant of "Column" matches argument types "None", "ForeignKey", "str"  # noqa E501
Column(None, ForeignKey("a.id"), name="name")
Column("name", type_=None)
Column("name", ForeignKey("a.id"), type_=Integer())


# These seems supported now
Column(Integer, ForeignKey("a.id"), type_=String)
Column("name", ForeignKey("a.id"), name="String")

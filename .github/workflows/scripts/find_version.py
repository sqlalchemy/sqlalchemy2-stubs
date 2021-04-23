import json
import sys
from urllib import request


def go(argv):
    if "sqla_release" not in argv:
        print('master')
    result = request.urlopen(
        "https://pypi.org/pypi/SQLAlchemy/json", timeout=10
    )
    assert result.status == 200
    parsed = json.loads(result.read())
    version = parsed["info"]["version"]
    print(f"rel_{version}".replace(".", "_"))


if __name__ == "__main__":
    go(sys.argv)

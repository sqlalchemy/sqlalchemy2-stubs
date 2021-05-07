import json
import sys
from urllib import request


def go(argv):
    if "sqla_release" in argv:
        result = request.urlopen(
            "https://pypi.org/pypi/SQLAlchemy/json", timeout=10
        )
        assert result.status == 200
        parsed = json.loads(result.read())
        version = parsed["info"]["version"]
        print(f"rel_{version}".replace(".", "_"))
    else:
        print("master")


if __name__ == "__main__":
    go(sys.argv)

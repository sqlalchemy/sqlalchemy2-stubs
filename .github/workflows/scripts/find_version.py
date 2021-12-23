import json
import sys
from urllib import request


def go(argv: list[str]):
    if "sqla_release" in argv:
        result = request.urlopen(
            "https://pypi.org/pypi/SQLAlchemy/json", timeout=10
        )
        assert result.status == 200
        parsed = json.loads(result.read())
        version = parsed["info"]["version"]
        print(f"rel_{version}".replace(".", "_"))
    else:
        for part in argv:
            if part.startswith("sqla_"):
                part = part.partition("sqla_")[-1]
                print(part)
                break
        else:
            print("main")


if __name__ == "__main__":
    go(sys.argv)

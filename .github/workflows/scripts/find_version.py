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
        # `releases` is deprecated but should be good for now
        # https://warehouse.pypa.io/api-reference/json.html
        v14 = sorted(
            [key for key in parsed["releases"] if key.startswith("1.4")],
            key=lambda key: [
                int(part) if part.isdecimal() else -1
                for part in key.split(".")
            ],
        )
        version = v14[-1]
        # version = parsed["info"]["version"]  # this is now v2
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

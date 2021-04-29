import argparse
import pathlib
import re


def is_canonical(version):
    # from https://www.python.org/dev/peps/pep-0440/
    return (
        re.match(
            r"^([1-9][0-9]*!)?(0|[1-9][0-9]*)(\.(0|[1-9][0-9]*))*((a|b|rc)(0|"
            r"[1-9][0-9]*))?(\.post(0|[1-9][0-9]*))?(\.dev(0|[1-9][0-9]*))?$",
            version,
        )
        is not None
    )


def next_version(current_version: str):
    major, minor, point = current_version.split(".")
    if point.isdecimal():
        # 1.2.3 -> 1.2.4
        next = int(point) + 1
        return f"{major}.{minor}.{next}"
    if not point[-1].isdecimal():
        # 0.1.2b -> 0.1.2b1
        return f"{major}.{minor}.{point}1"
    # 0.1.2b1 -> 0.1.2b2
    match = re.match(r"(\d+\D*)(\d+)", point)
    if not match:
        raise RuntimeError(
            f"Cannot decode the current version {current_version}"
        )
    base, current = match.groups()
    print(base, current)
    next = int(current) + 1
    new_point = f"{base}{next}"
    return f"{major}.{minor}.{new_point}"


def go(args):
    if args.set_version and not is_canonical(args.set_version):
        raise RuntimeError(f"Cannot use {args.set_version!r} as version")

    setup = pathlib.Path("setup.cfg")
    setup_text = setup.read_text()
    new_setup_text = []
    found = False
    for line in setup_text.split("\n"):
        if not line.startswith("version = "):
            new_setup_text.append(line)
            continue
        if found:
            raise RuntimeError(
                "Multiple lines starting with 'version =' found"
            )
        if args.set_version:
            new_setup_text.append(f"version = {args.set_version}")
            version = args.set_version
        else:
            current_version = line.split(" ")[-1]
            version = next_version(current_version)
            new_setup_text.append(f"version = {version}")
        found = True
    if not found:
        raise RuntimeError("No line found starting with 'version ='")

    setup.write_text("\n".join(new_setup_text))
    print("Updated version to", version)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--set-version", help="Version to set")
    group.add_argument(
        "--update-version",
        help="Take the current version and update it",
        action="store_true",
    )

    args = parser.parse_args()
    go(args)

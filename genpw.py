#!/usr/bin/env python3
import argparse
import string
import sys

try:
    import secrets
except ModuleNotFoundError:
    sys.stderr.write("This script requires Python 3.6 or newer\n")
    sys.exit(1)


def length(value):
    """Validate the length provided."""
    if int(value) < 3:
        raise ValueError("minimum length is 3")
    else:
        return int(value)


parser = argparse.ArgumentParser(
    prog="genpw.py", description="a random password generator"
)
parser.add_argument(
    "-l",
    "--length",
    default=16,
    type=length,
    help="length to generate (default: 16; must be >= 3)",
)
args = parser.parse_args()

if args.length < 3:
    sys.stderr.write(parser.prog + ": error: minimum length is 3\n")
    sys.exit(1)

alphabet = string.ascii_letters + string.digits
while True:
    password = "".join(secrets.choice(alphabet) for i in range(args.length))
    if (
        any(c.islower() for c in password)
        and any(c.isupper() for c in password)
        and any(c.isdigit() for c in password)
    ):
        break
print(password)

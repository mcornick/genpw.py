#!/usr/bin/env python3
"""Password generator using the secrets module."""
import argparse
import string
import sys

try:
    import secrets
except ModuleNotFoundError:
    sys.stderr.write("This script requires Python 3.6 or newer\n")
    sys.exit(1)

parser = argparse.ArgumentParser(
    prog="genpw.py", description="a random password generator"
)
parser.add_argument(
    "-l", "--length", default=16, type=int, help="length to generate (default: 16)"
)
parser.add_argument(
    "-U",
    "--no-upper",
    action="store_true",
    help="exclude uppercase letters (default: False)",
)
parser.add_argument(
    "-u",
    "--no-lower",
    action="store_true",
    help="exclude lowercase letters (default: False)",
)
parser.add_argument(
    "-d",
    "--no-digit",
    action="store_true",
    help="exclude digits (default: False)",
)
args = parser.parse_args()

if args.no_lower and args.no_upper and args.no_digit:
    sys.stderr.write(parser.prog + ": error: excluded all character types\n")
    sys.exit(1)

alphabet = ""
minimum_length = 0
if not args.no_lower:
    alphabet = alphabet + string.ascii_lowercase
    minimum_length = minimum_length + 1
if not args.no_upper:
    alphabet = alphabet + string.ascii_uppercase
    minimum_length = minimum_length + 1
if not args.no_digit:
    alphabet = alphabet + string.digits
    minimum_length = minimum_length + 1

if args.length < minimum_length:
    sys.stderr.write(
        parser.prog + ": error: minimum length is {}\n".format(minimum_length)
    )
    sys.exit(1)

while True:
    password = "".join(secrets.choice(alphabet) for i in range(args.length))
    if (
        (any(c.islower() for c in password) or args.no_lower)
        and (any(c.isupper() for c in password) or args.no_upper)
        and (any(c.isdigit() for c in password) or args.no_digit)
    ):
        break
print(password)

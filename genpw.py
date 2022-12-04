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


def genpw(length, no_upper, no_lower, no_digit):
    """Generate a password."""

    if no_lower and no_upper and no_digit:
        return "error: excluded all character types"

    minimum_length = int(not no_lower) + int(not no_upper) + int(not no_digit)
    if length < minimum_length:
        return "error: length is too short"

    alphabet = ""
    if not no_lower:
        alphabet = alphabet + string.ascii_lowercase
    if not no_upper:
        alphabet = alphabet + string.ascii_uppercase
    if not no_digit:
        alphabet = alphabet + string.digits

    while True:
        password = "".join(secrets.choice(alphabet) for i in range(length))
        if (
            (any(c.islower() for c in password) or no_lower)
            and (any(c.isupper() for c in password) or no_upper)
            and (any(c.isdigit() for c in password) or no_digit)
        ):
            break
    return password


if __name__ == "__main__":
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

    password = genpw(args.length, args.no_upper, args.no_lower, args.no_digit)
    if "error:" in password:
        sys.stderr.write("{}: {}\n".format(parser.prog, password))
        sys.exit(1)
    else:
        print(password)

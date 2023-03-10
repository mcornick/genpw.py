#!/usr/bin/env python3
"""Password generator using the secrets module."""
import string
import sys

import click

try:
    import secrets
except ModuleNotFoundError:
    sys.stderr.write("This script requires Python 3.6 or newer\n")
    sys.exit(1)


def genpw(length=16, upper=True, lower=True, digit=True):
    """Generate a password."""
    alphabet = ""
    if lower:
        alphabet = alphabet + string.ascii_lowercase
    if upper:
        alphabet = alphabet + string.ascii_uppercase
    if digit:
        alphabet = alphabet + string.digits

    while True:
        password = "".join(secrets.choice(alphabet) for i in range(length))
        if (
            (any(c.islower() for c in password) or not lower)
            and (any(c.isupper() for c in password) or not upper)
            and (any(c.isdigit() for c in password) or not digit)
        ):
            return password


@click.command()
@click.option("--length", default=16, show_default=True, help="length to generate")
@click.option("--upper/--no-upper", default=True, help="include/exclude uppercase")
@click.option("--lower/--no-lower", default=True, help="include/exclude lowercase")
@click.option("--digit/--no-digit", default=True, help="include/exclude digits")
def cli(length, upper, lower, digit):
    """Generate a random password."""
    if not lower and not upper and not digit:
        raise click.UsageError(
            "Impossible combination of '--no-upper', '--no-lower', and '--no-digit'."
        )

    minimum_length = int(lower) + int(upper) + int(digit)
    if length < minimum_length:
        raise click.BadParameter("minimum length is {}".format(minimum_length))

    click.echo(genpw(length, upper, lower, digit))

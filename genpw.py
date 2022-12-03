#!/usr/bin/env python3
import string
import sys

try:
    import secrets
except ModuleNotFoundError:
    sys.stderr.write("This script requires Python 3.6 or newer\n")
    sys.exit(1)

try:
    length = int(sys.argv[1])
except (IndexError, ValueError):
    length = 16

if length < 3:
    sys.stderr.write("Minimum length is 3\n")
    sys.exit(1)

alphabet = string.ascii_letters + string.digits
while True:
    password = "".join(secrets.choice(alphabet) for i in range(length))
    if (
        any(c.islower() for c in password)
        and any(c.isupper() for c in password)
        and any(c.isdigit() for c in password)
    ):
        break
print(password)

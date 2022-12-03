#!/usr/bin/env python3
import secrets
import string
import sys

try:
    length = int(sys.argv[1])
except (IndexError, ValueError):
    length = 16
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

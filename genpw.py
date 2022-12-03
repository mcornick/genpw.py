#!/usr/bin/env python3
import secrets
import string
import sys

try:
    length = int(sys.argv[1])
except (IndexError, ValueError):
    length = 16
alphabet = string.ascii_letters + string.digits
password = "".join(secrets.choice(alphabet) for i in range(length))
print(password)

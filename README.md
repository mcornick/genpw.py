# genpw.py

A password generator based on the Python 3.0 `secrets` module, and an
extension of the examples provided in its
[documentation](https://docs.python.org/3/library/secrets.html).

Use the --length option to specify the length. If no length is passed, a
default length of 16 is used.

Passwords will contain an uppercase letter, a lowercase letter, and a
digit unless the --no-upper, --no-lower, and/or --no-digit options are
used.

Provided under the Zero Clause BSD License (see the `LICENSE` file.)

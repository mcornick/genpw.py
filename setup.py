from setuptools import setup

setup(
    name="genpw",
    version="0.1.0",
    py_modules=["genpw"],
    install_requires=[
        "Click",
    ],
    entry_points={
        "console_scripts": [
            "genpw = genpw:cli",
        ]
    },
)

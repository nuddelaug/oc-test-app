from setuptools import setup, find_packages
setup (
    name             = "jokes",
    version          = "0.1",
    description      = "Example application providing Juck Norris jokes",
    packages         = find_packages(),
    install_requires = ["gunicorn"],
)

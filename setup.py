from setuptools import setup, find_packages
setup (
    name             = "jokes",
    version          = "0.2",
    description      = "Example application providing Juck Norris jokes",
    packages         = find_packages(),
    install_requires = ["flask", "flask_autodoc"],
)

""" 
run setup
    python setup.py sdist bdist_wheel

delete dist
    twine upload dist/*
or
    twine upload dist/* --skip-existing
"""

from setuptools import setup


# move setup to other files for security issues
if __name__ == "__main__":
    setup()

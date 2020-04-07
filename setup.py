# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "swagger_server"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["connexion"]

setup(
    name=NAME,
    version=VERSION,
    description="Challenge API",
    author_email="todo@todo.todo",
    url="",
    keywords=["Swagger", "Challenge API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['swagger_server=swagger_server.__main__:main']},
    long_description="""\
    This is an in-development REST API specification for a Cyber/STEM challenge webapp that allows users to log in and complete challenges. Users get points for succesfully completed challenges. The webapp collects and returns user scores/competetive statistics.
    """
)

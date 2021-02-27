# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "openapi_server"
VERSION = "1.0.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "connexion>=2.0.2",
    "swagger-ui-bundle>=0.0.2",
    "python_dateutil>=2.6.0"
]

setup(
    name=NAME,
    version=VERSION,
    description="Pollination Web Server",
    author_email="",
    url="",
    keywords=["OpenAPI", "Pollination Web Server"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    All values in this API are required and not nullable unless specifically stated.  Org user privileges are:&lt;br&gt;  0 :&#x3D; invited&lt;br&gt;  1 :&#x3D; member&lt;br&gt;  2 :&#x3D; admin&lt;br&gt;  3 :&#x3D; owner 
    """
)


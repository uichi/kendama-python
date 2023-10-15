# coding: utf-8

"""
    国税庁API

    国税庁が提供するインボイス制度適格請求書発行事業者公表システムWeb-APIを使用するためのクライアントAPI(https://www.invoice-kohyo.nta.go.jp/web-api/index.html)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from setuptools import setup, find_packages  # noqa: H301

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "kendama"
VERSION = "0.1.2"
PYTHON_REQUIRES = ">=3.7"
REQUIRES = [
    "urllib3 >= 1.25.3, < 2.1.0",
    "python-dateutil",
    "pydantic >= 1.10.5, < 2",
    "aenum"
]

setup(
    name=NAME,
    version=VERSION,
    description="国税庁API",
    author="uichi",
    author_email="37263474+uichi@users.noreply.github.com",
    url="https://github.com/uichi/kendama-python",
    license="MIT",
    keywords=["OpenAPI", "OpenAPI-Generator", "国税庁API"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description_content_type='text/markdown',
    long_description=open('README.md').read(),
    package_data={"kendama": ["py.typed"]},
    project_urls={
        'Documentation': 'https://github.com/uichi/kendama-python/blob/main/README.md',
        'Source': 'https://github.com/uichi/kendama-python'
    }
)

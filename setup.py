#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = ["python-slugify<7.0", "ultra-config==0.6.3"]

test_requirements = ["pytest==6.2.5", "pytest-cov==3.0.0"]

setup(
    author="Daniel Schaefer",
    author_email="danschaefer@gmail.com",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="The DataForSEO Python SDK contains a Python library to interact with APIs provided by DataForSEO (https://dataforseo.com/).",
    entry_points={
        "console_scripts": [
            "dataforseo_sdk=dataforseo_sdk.cli:main",
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="dataforseo_sdk",
    name="dataforseo_sdk",
    packages=find_packages(include=["dataforseo_sdk", "dataforseo_sdk.*"]),
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/lieutdan13/dataforseo_sdk",
    version="0.1.0",
    zip_safe=False,
)

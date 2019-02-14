========================
{{cookiecutter.project}}
========================


{{cookiecutter.description}}


Project structure
=================

::

    {{cookiecutter.repo}}
    ├── AUTHORS.rst
    ├── CHANGELOG.rst
    ├── LICENSE.txt
    ├── Makefile
    ├── README.rst
    ├── docs
    │   ├── Makefile
    │   ├── _static
    │   ├── authors.rst
    │   ├── changelog.rst
    │   ├── conf.py
    │   ├── index.rst
    │   └── license.rst
    ├── requirements.txt
    ├── setup.cfg
    ├── setup.py
    ├── src
    │   └── {{cookiecutter.repo}}
    │       ├── __init__.py
    │       └── {{cookiecutter.repo}}.py
    └── tests
        ├── conftest.py
        └── test_{{cookiecutter.repo}}.py


Note
====

This project has been set up using PyScaffold 3.1 and Cookiecutter 1.6.

For details and usage information on PyScaffold, see https://pyscaffold.org/.

For details and usage information on Cookiecutter, see https://cookiecutter.readthedocs.io/.

============
Cookiecutter
============

A Cookiecutter_ template to create a simple project structure based on PyScaffold_.

Usage
=====

To get started, install cookiecutter:

::

   pip install cookiecutter

Then, run the ``cookiecutter`` command the following arguments:

- ``--no-input``
- the template url (``gh:marskar/cookiecutter``)
- ``project``
- ``author``
- ``user``
- ``description``

::

   cookiecutter --no-input gh:marskar/cookiecutter \
   project="PROJECT_NAME" author="AUTHOR_NAME" \
   user=USER_NAME description="DESCRIPTION"

For more details on possible arguments and their defaults,
take a look at the ``cookiecutter.json`` file.

Project structure
=================

::

    template
    ├── AUTHORS.rst
    ├── CHANGELOG.rst
    ├── LICENSE.txt
    ├── Makefile
    ├── README.rst
    ├── docs
    │   ├── Makefile
    │   ├── _static
    │   ├── authors.rst
    │   ├── changelog.rst
    │   ├── conf.py
    │   ├── index.rst
    │   └── license.rst
    ├── requirements.txt
    ├── setup.cfg
    ├── setup.py
    ├── src
    │   └── template
    │       ├── __init__.py
    │       └── template.py
    └── tests
        ├── conftest.py
        └── test_template.py


Note
====

This project has been set up using PyScaffold 3.1 and Cookiecutter 1.6.

For details and usage information on PyScaffold, see https://pyscaffold.org/.

For details and usage information on Cookiecutter, see https://cookiecutter.readthedocs.io/.

.. _PyScaffold: https://pyscaffold.org/
.. _Cookiecutter: https://cookiecutter.readthedocs.io/


.. image:: https://badges.gitter.im/py4ds/cookiecutter.svg
   :alt: Join the chat at https://gitter.im/py4ds/cookiecutter
   :target: https://gitter.im/py4ds/cookiecutter?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge
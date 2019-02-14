#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from {{cookiecutter.repo}}.{{cookiecutter.repo}} import fib

__author__ = "{{cookiecutter.author}}"
__copyright__ = "{{cookiecutter.author}}"
__license__ = "{{cookiecutter.license}}"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)

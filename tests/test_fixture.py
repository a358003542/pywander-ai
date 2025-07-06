#!/usr/bin/env python
# -*-coding:utf-8-*-

import pytest


def test_config_read(sample_config):
    assert sample_config['a'] == 1

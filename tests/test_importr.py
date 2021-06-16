#!/usr/bin/env python
import rpy2
from rpy2.robjects.packages import importr


def test_importrpy2():
    base = importr('base')
    assert base.__module__ == 'rpy2.robjects.packages'

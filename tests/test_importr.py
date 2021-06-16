#!/usr/bin/env python
import rpy2
from rpy2.robjects.packages import importr


def test_importrpy2():
    pkg = importr('remotes')
    assert pkg.__module__ == 'rpy2.robjects.packages'

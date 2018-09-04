# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 13:03:00 2016
@author: p
"""
from __future__ import absolute_import, division, print_function, unicode_literals
import loggerloader as ll
import pandas as pd
import matplotlib
import sys
sys.path.append('../')
import numpy as np

def test_new_xle_imp():
    xle = 'test/20160919_LittleHobble.xle'
    xle_df = ll.new_xle_imp(xle)
    assert len(xle_df) > 0

def test_well_baro_merge():
    xle = "test/ag13c 2016-08-02.xle"
    xle_df = ll.new_xle_imp(xle)
    barofile = "test/baro.csv"
    baro = pd.read_csv(barofile,index_col=0, parse_dates=True)
    baro['Level'] = baro['pw03']
    assert len(ll.well_baro_merge(xle_df, baro, sampint=60)) > 10
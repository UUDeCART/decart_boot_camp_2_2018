import numpy as np
import pandas as pd
from nose.tools import  assert_equal
import os
import numbers
DATADIR = os.path.join(os.path.expanduser("~"),"DATA")
HRDIR = os.path.join(DATADIR,"Numerics", "mimic2", "hr", "subjects")
BPDIR = os.path.join(DATADIR,"Numerics", "mimic2", "bp", "subjects")

import numbers

def data_shape(rows, patient="3235"):
    
    data = pd.read_table(os.path.join(BPDIR, patient+".txt"), header=None, names=["systolic", "diastolic"])
    if not isinstance(rows, numbers.Number):
        return "Your answer needs to be a number"
    if not isinstance(rows,int):
        return "Your number needs to be an integer"
    try:
        assert_equal(rows, data.shape[0])
        return "You provided the correct number of rows"
    except Exception as error:
        return "You did not provide the right number of rows"
    
def data_types(dtype, patient="3235"):
    
    data = pd.read_table(os.path.join(BPDIR, patient+".txt"), header=None, names=["systolic", "diastolic"])
    if not isinstance(dtype, type):
        return "Your answer needs to be a type (e.g. np.uint8)"
    try:
        assert_equal(dtype, data.dtypes[0])
        return "You provided the correct data type"
    except Exception as error:
        return "You did not provide the correct data type"

def median_diastolic(median_value, patient='3235'):
    data = pd.read_table(os.path.join(BPDIR, patient+".txt"), header=None, names=["systolic", "diastolic"])
    if not isinstance(median_value, numbers.Number):
        return "Your answer needs to be a number"
    try:
        assert_equal(median_value, np.median(data["diastolic"]))
        return "You provided the correct median value"
    except Exception as error:
        return "You did not provide the correct median value", error

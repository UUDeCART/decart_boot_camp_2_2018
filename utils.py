import numpy as np

def get_data(f):
    with open(f) as f0:
        return np.array([float(d) for d in f0.readlines()])
def get_case_length(f):
    with open(f) as f0:
        return len([float(d) for d in f0.readlines()])
def get_case_zero_count(f):
    with open(f) as f0:
        return len([d for d in [float(d) for d in f0.readlines()] if d == 0])
def get_case_gt_count(f, thresh=200):
    with open(f) as f0:
        return len([d for d in [float(d) for d in f0.readlines()] if d > thresh])

# File: numpy_load_library_violation.py
import numpy as np

def load_custom_library():
    # Unsafe: Loading library without specifying exact location
    np.ctypeslib.load_library("custom_operator.so")

load_custom_library()

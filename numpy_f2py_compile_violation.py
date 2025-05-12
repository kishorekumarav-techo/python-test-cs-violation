# File: numpy_f2py_compile_violation.py
import numpy as np

def compile_code():
    # Unsafe: Compiling arbitrary code without validation
    np.f2py.compile("some_code.f90")

compile_code()

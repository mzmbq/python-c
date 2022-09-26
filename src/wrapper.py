import ctypes
import numpy as np

lib = ctypes.CDLL('./bin/testlib.so')

if False:
    lib.hello()


    # https://stackoverflow.com/questions/5862915/passing-numpy-arrays-to-a-c-function-for-input-and-output
    from numpy.ctypeslib import ndpointer
    fun = lib.cfun
    fun.restype = None
    fun.argtypes = [ndpointer(ctypes.c_double, flags="C_CONTIGUOUS"),
                    ctypes.c_size_t,
                    ndpointer(ctypes.c_double, flags="C_CONTIGUOUS")]

    # usage
    indata = np.ones((5,6))
    outdata = np.empty((5,6))
    fun(indata, indata.size, outdata)
    print(outdata)



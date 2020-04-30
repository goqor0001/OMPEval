# distutils: language = c++
cdef extern from "omp/HandEvaluator.cpp":
    pass
cdef extern from "omp/HandEvaluator.h" namespace "omp":
    cppclass HandEvaluator:
        int evaluate7(int c1, int c2, int c3, int c4, int c5, int c6, int c7)
        int evaluate6(int c1, int c2, int c3, int c4, int c5, int c6)
        int evaluate5(int c1, int c2, int c3, int c4, int c5)

def eval7(c1, c2, c3, c4, c5, c6, c7):
    cdef HandEvaluator obj
    return obj.evaluate7(c1, c2, c3, c4, c5, c6, c7)

def eval6(c1, c2, c3, c4, c5, c6):
    cdef HandEvaluator obj
    return obj.evaluate6(c1, c2, c3, c4, c5, c6)

def eval5(c1, c2, c3, c4, c5):
    cdef HandEvaluator obj
    return obj.evaluate5(c1, c2, c3, c4, c5)

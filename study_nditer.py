import numpy as np

x = np.arange(12).reshape(3,4)

it = np.nditer(x, flags=['multi_index'], op_flags=['readwrite'])
# flags : c_index, f_index, multi_index(tuple of indices)
#op_flags : one of readonly, readwrite, writeonly must be specified

while not it.finished:
    idx = it.multi_index

    print(idx) # (0,0), (0,1), (0,2), (0,3), (1,0), (1,1), (1,2), (1,3), (2,0), (2,1), (2,2), (2,3)
    print(x[idx]) # 0 1 2 3 4 5 6 7 8 9 10 11

    it.iternext()
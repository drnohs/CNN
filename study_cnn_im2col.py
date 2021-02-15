import numpy as np
from util import im2col

# X1 : Data 1
x1 = np.random.rand(1,3,7,7) # Data, Channel, Height, Width
print("x1:",x1.shape)

col1=im2col(x1, 5, 5, stride=1, pad=0) # filter(5x5)
print(col1.shape) # (9,75) # OH * OW (* Data), FilterH * FilterW * Channel

#X2 : Data 10
x2 = np.random.rand(10,3,7,7) # Data, Channel, Height, Width
print("x2:",x2.shape)

col2 = im2col(x2, 5, 5, stride=1, pad=0) # filter(5x5)
print(col2.shape) # (9,75) # OH * OW (* Data), FilterH * FilterW * Chann

#X3
x3 = np.random.randint(10,size=(1,2,3,3))
print("x3:", x3.shape)
print(x3)

col3 = im2col(x3, 2, 2, stride=1, pad=0)
print(col3.shape)
print(col3)



import numpy as np
from simple_convnet import SimpleConvNet
from layers import *

# Convolution Layer Test

input_size=4
a = np.array(range(input_size**2)).reshape(1,1,input_size,input_size)

print("Input:",a)
print(a.shape)


network = SimpleConvNet(input_dim=(1,input_size,input_size),
                        conv_param = {'filter_num': 2, 'filter_size': 2, 'pad': 0, 'stride': 1},
                        hidden_size=10, output_size=3, weight_init_std=0.01)
print (network.params['W1'])
print (network.params['W1'].shape)

c_net = Convolution(network.params['W1'],network.params['b1'],1,0)
out_a = c_net.forward(a)

print("Result:",out_a)
print(out_a.shape)
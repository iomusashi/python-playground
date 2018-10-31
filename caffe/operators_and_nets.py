from caffe2.python import core
from caffe2.python import workspace
from caffe2.python import model_helper
import numpy as np

###############################################################################
# pragma - Blobs, Workspaces, Tensors
x = np.random.rand(4, 3, 2)
print(f'x = {x}')
print(f'x.shape = {x.shape}')

workspace.FeedBlob('my_x', x)

x2 = workspace.FetchBlob('my_x')
print(f'x2 = {x2}')
###############################################################################
# Nets and Operators

# Succeeding code defines a simple network with one fully-connected FC layer.

# Create the input data
# First dimension 16 means: a mini batch of 16 samples at a time.
data = np.random.rand(16, 100).astype(np.float32)

# Create labels for the data as integers [0, 9]
labels = (np.random.rand(16) * 10).astype(np.int32)

workspace.FeedBlob('data', data)
workspace.FeedBlob('label', labels)

# Create model using a model helper
m = model_helper.ModelHelper(name = 'my first net')

# Prep work: Creating randomly filled blobs for weights and biases
# XavierFill or ConstantFill takes an empty array, name, and shape
# shape = [output, input]
weights = m.param_init_net.XavierFill([], 'fc_w', shape=[10, 100])
biases = m.param_init_net.ConstantFill([], 'fc_b', shape=[10, ])

fc_1 = m.net.FC(['data', 'fc_w', 'fc_b'], 'fc1')
pred = m.net.Sigmoid(fc_1, 'pred')
softmax, loss = m.net.SoftmaxWithLoss([pred, 'label'], ['softmax', 'loss'])

# Backward pass: Gradient operator
m.AddGradientOperators([loss])

# Optional: Check the network definition in a protocol buffer
print(f'Network protobuf encoding:\n{ m.net.Proto() }')

# Optional: Check the param initialization network:
print(f'Init network protobuf encoding:\n{ m.param_init_net.Proto() }')

# Now since we have the model training operators defined,
# it's time to train the model.

# FIRST: we need to run the param initialization only ONCE!
workspace.RunNetOnce(m.param_init_net)

# Then create the actual training net:
workspace.CreateNet(m.net)

# The network is created once, and we can efficiently run it multiple times
for _ in range(100):
    data = np.random.rand(16, 100).astype(np.float32)
    label = (np.random.rand(16) * 10).astype(np.int32)

    workspace.FeedBlob('data', data)
    workspace.FeedBlob('label', labels)

    workspace.RunNet(m.name, 10)

print(f'Softmax = { workspace.FetchBlob("softmax") }')
print(f'Loss = { workspace.FetchBlob("loss") }')

###############################################################################
###############################################################################

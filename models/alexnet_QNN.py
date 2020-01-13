from nnUtils import *

model = Sequential([
    QuantizedWeightOnlySpatialConvolution(64,11,11,4,4, padding='VALID', bias=False, name='alexnet_v2/conv1'),
    BatchNormalization('bn1'),
    ReLU(),
    SpatialMaxPooling(3,3,2,2),
    QuantizedWeightOnlySpatialConvolution(192,5,5, padding='SAME', bias=False, name='alexnet_v2/conv2'),
    BatchNormalization('bn2'),
    ReLU(),
    SpatialMaxPooling(3,3,2,2),
    QuantizedWeightOnlySpatialConvolution(384,3,3, padding='SAME', bias=False, name='alexnet_v2/conv3'),
    BatchNormalization('bn3'),
    ReLU(),
    QuantizedWeightOnlySpatialConvolution(384,3,3, padding='SAME', bias=False, name='alexnet_v2/conv4'),
    BatchNormalization('bn4'),
    ReLU(),
    QuantizedWeightOnlySpatialConvolution(256,3,3, padding='SAME', bias=False, name='alexnet_v2/conv5'),
    BatchNormalization('bn5'),
    ReLU(),
    SpatialMaxPooling(3,3,2,2),
    QuantizedWeightOnlySpatialConvolution(4096,5,5, padding='VALID', bias=False, name='alexnet_v2/fc6'),
    BatchNormalization('bn6'),
    ReLU(),
    QuantizedWeightOnlySpatialConvolution(4096,1,1, padding='SAME', bias=False, name='alexnet_v2/fc7'),
    BatchNormalization('bn7'),
    ReLU(),
    LastConvolution(1000,1,1, padding='SAME', name='alexnet_v2/fc8'),
    BatchNormalization('bn8')
])
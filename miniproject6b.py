# -*- coding: utf-8 -*-
"""MiniProject6b

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tvLPa5Ikq2nA5HjT2VJSnk41GNC7ZPiT

Download the Dataset
Scikit-Learn Library offers a way to download the CIFAR-100 dataset using these lines of code:
"""

from keras.datasets import mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

"""Re-shaping the images
Prepare your dataset.
Write these two lines of code to somewhat normalize your dataset:
"""

x_train = x_train.astype('float32')/255
x_test = x_test.astype('float32')/255

# x_train = x_train.reshape(60000, 28, 28, 1)/255
# x_test = x_test.reshape(10000, 28, 28, 1)/255

"""Encode the Target Labels
Use these lines of code to encode your labels for training:
"""

from keras.utils import to_categorical
x_train = to_categorical(x_train, num_classes=3)
# y_train = to_categorical(y_train, num_classes=3)

"""Build the CNN with the following layers:
The input layer is a 2-D convolutional layer with the following parameters:
32 units;
convolution window size: 3 x 3;
Activation function: relu; and
Input shape: 32 x 32 x 3.
A 2-D convolutional layer with the following parameters:
32 units;
Convolution window size: 3 x 3;
Activation function: relu;
A 2-D max pooling layer with a pool size of 2x2; and
A dropout layer with 0.25 rate.
Two 2-D convolutional layers, each with the following parameters:
64 units; Convolution window size: 3 x 3;
Activation function: relu;
A 2-D max pooling layer with a pool size of 2x2;
A dropout layer with 0.25 rate; and
A flattening layer.
A fully-connected layer with:
512 units;
Activation function: relu; and
A Dropout layer with 0.5 rate.
The output layer is a fully-connected layer with:
100 units; and
Activation function: softmax.
"""

from keras.models import Sequential
model = Sequential()

from keras.layers import Conv2D
model.add(Conv2D(32, (3, 3), input_shape=(32, 32, 3), activation='relu'))

model.add(Conv2D(32, (3, 3), activation='relu'))

from keras.layers import MaxPooling2D
model.add(MaxPooling2D(pool_size=(2, 2)))

from keras.layers import Dropout
model.add(Dropout(0.25))

model.add(Conv2D(64, (3, 3), activation='relu'))

model.add(Conv2D(64, (3, 3), activation='relu'))

model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Dropout(0.25))

from keras.layers import Flatten
model.add(Flatten())

from keras.layers import Dense
model.add(Dense(units=512, activation='relu'))

model.add(Dropout(0.5))

model.add(Dense(units=100, activation='softmax'))

"""Choosing Hyper-parameters
Build the Network using the following parameters:
Optimizer: adam;
Loss Function: categorical_crossentropy;
Metrics: accuracy;
Epochs: 100; and
Batch size: 32.
"""

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(x_train, y_train, epochs=10, batch_size=32)

"""Training Network
Use Keras to implement the Network described and train your data.
Test the model using the test set (x_test and y_test).
Note: Your code should return the model and the test results (loss and accuracy).
"""

loss, accuracy = model.evaluate(x_test, y_test)
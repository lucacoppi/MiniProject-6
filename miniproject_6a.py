# -*- coding: utf-8 -*-
"""MiniProject 6a

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14GE36g82LtSJB8T0oFEvjNZbLFYCgJ_y

Download the Dataset
Scikit-Learn Library offers a way to download the MNIST dataset using these lines of code:
"""

from keras.datasets import mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

"""Re-shaping the images
Prepare your dataset.
Write these two lines of code to somewhat normalize your dataset:
"""

x_train = x_train.reshape(60000, 28, 28, 1)/255
x_test = x_test.reshape(10000, 28, 28, 1)/255

"""Define your Convolutional Neural Network
Build the CNN with the following layers:
The input layer is a 2-D convolutional layer with the following parameters:
28 units;
Convolution window size: 3 x 3; and
Input size: 28 x 28.
Activation function: relu
The first hidden layer is a 2-D max pooling layer with a pool size of 2x2.
The second hidden layer is a flattening layer.
The third hidden layer is a fully-connected layer with:
128 units; and
Activation function: relu.
The output layer is a fully-connected layer with:
10 units; and
Activation function: softmax.
"""

from keras.models import Sequential
model = Sequential()

from keras.layers import Conv2D
model.add(Conv2D(28, (3, 3), input_shape=(28, 28, 1), activation='relu'))

from keras.layers import MaxPooling2D
model.add(MaxPooling2D(pool_size=(2, 2)))

from keras.layers import Flatten
model.add(Flatten())

from keras.layers import Dense
model.add(Dense(units=128, activation='relu'))

model.add(Dense(units=10, activation='softmax'))

"""Choosing Hyper-parameters
Build the network using the following parameters: Optimizer: adam;
Loss Function: sparse_categorical_crossentropy;
Metrics: accuracy; and
Epochs: 100. 
Note: 100 epochs tales too long, I did 10.
"""

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(x_train, y_train, epochs=10)

"""Training Network
Build the network using the following parameters:
Use Keras to implement the Network described and train your data.
Test the model using the test set (x_test and y_test).
Note: Your code should return the model and the test results (loss and accuracy).
"""

loss, accuracy = model.evaluate(x_test, y_test)

print(loss, accuracy)
# -*- coding: utf-8 -*-
"""MiniProject6d

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12GQkkQxiQD9is7qqy3ktmJvZIn14dadQ

Step 1:Read the Dataset
To use the dataset from Keras datasets, use these lines of code:

Padding your Sequences
You need to have equal sequences for training, for this you will apply padding.
Write these lines of code to implement the padding needed:

Step 3:
Your Initial code should look like this:
"""

import numpy as np

np_load_old = np.load
np.load = lambda *a,**k: np_load_old(*a, allow_pickle=True)
from keras.datasets import imdb
(x_train, y_train), (x_test, y_test) = imdb.load_data(path="imdb.npz", maxlen=130, num_words=6000)
from keras.preprocessing import sequence
x_train = sequence.pad_sequences(x_train, maxlen=130)
np.load = np_load_old

"""Define an RNN with the following layers:
An embedding layer with the following parameters:
The input dimension is 6000;
The output dimension is 128;
The input length is 130; and
An LSTM layer with 32 units.
A fully-connected layer with the following parameters:
Activation function is relu;
The number of units is 20; and
A dropout layer with a dropout rate of 5%.
A fully-connected layer with the following parameters:
Activation function is sigmoid; and
The number of units is 1.
"""

from keras.models import Sequential
model = Sequential()

from keras.layers import Embedding
model.add(Embedding(6000, 128, input_length=130))

from keras.layers import LSTM
model.add(LSTM(32))

from keras.layers import Dense
model.add(Dense(units=20, activation='relu'))

from keras.layers import Dropout
model.add(Dropout(0.05))

from keras.layers import Dense
model.add(Dense(units=1, activation='sigmoid'))

"""Step 4:Choosing Hyper-Parameters
Build the network using the following parameters:
Optimizer: adam;
Loss Function: binary_crossentropy;
Metrics: accuracy;
Epochs: 5; and
Batch size: 100.

Step 5:Training Network
Use Keras to implement the Network described and train your data.
Note: Your code should return the model.
"""

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(x_train, y_train, epochs=5, batch_size=100)
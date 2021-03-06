# -*- coding: utf-8 -*-
"""MiniProject6c

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JsglFL8PjaEygJQRLaNNkFGP6wYvW_vG

Step 1:Read the Text
To read the text file of lines from Shakespeare plays, use these lines of code:
#Read the text file as separate lines of text
with open('data.txt', 'r') as file:
"""

from google.colab import files
uploaded = files.upload()

with open('shak.txt', 'r') as file:
  text = file.read()
lines = text.lower().split('\n')
#Define words, vocabulary size and sequences of words as lines
from keras.preprocessing.text import text_to_word_sequence, Tokenizer
words = text_to_word_sequence(text)
tokenizer = Tokenizer()
tokenizer.fit_on_texts(words)
vocabulary_size = len(tokenizer.word_index) + 1
sequences = tokenizer.texts_to_sequences(lines)
#Find subsequences 
subsequences = []
for sequence in sequences:
    for i in range(1, len(sequence)):
       subsequence = sequence[:i+1]
       subsequences.append(subsequence)

"""Step 2:Padding Your Sequences
You need to have equal sequences for training, for this you will apply padding.
Write these lines of code to implement the padding needed:
"""

from keras.preprocessing.sequence import pad_sequences
sequence_length = max([len(sequence) for sequence in sequences])
sequences = pad_sequences(subsequences, maxlen=sequence_length, padding='pre')

"""Step 3:Encode the Target Labels
Use these lines of code to encode your labels for training:
"""

from keras.utils import to_categorical
x, y = sequences[:,:-1],sequences[:,-1]
y = to_categorical(y, num_classes=vocabulary_size)

"""Define an RNN with the following layers:
An embedding layer with the following parameters:
The input dimension is vocabulary_size
The output dimension is 100
The input length is sequence_length - 1
An LSTM layer with 100 units
A dropout layer with a dropout rate of 10%
A dense layer with the following parameters:
Activation function is softmax
The number of units is vocabulary_size
"""

from keras.models import Sequential
model = Sequential()

from keras.layers import Embedding
model.add(Embedding(vocabulary_size, 100, input_length=sequence_length - 1))

from keras.layers import LSTM
model.add(LSTM(10))

from keras.layers import Dropout
model.add(Dropout(0.1))

from keras.layers import Dense
model.add(Dense(units=vocabulary_size, activation='softmax'))

"""Choosing Hyper-Parameters
Build the network using the following parameters:
Optimizer: adam
Loss Function: categorical_crossentropy
Metrics: accuracy
Epochs: 500
"""

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(x, y, epochs=500)

"""Step 5:Training Network
Use Keras to implement the Network described and train your data.
Note: Your code should return the model.
"""

model
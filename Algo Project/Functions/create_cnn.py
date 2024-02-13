#CNN Model
from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt
import os
import tensorflow as tf 
from tensorflow import keras
from keras.utils import np_utils
from keras.utils.np_utils import to_categorical
from tensorflow.keras import layers
from keras.models import Sequential
from keras.layers import Dense, Activation,  MaxPooling1D
from keras.layers import Reshape
from keras.layers import Conv1D
from keras.layers import LeakyReLU
from keras.layers import BatchNormalization
from keras.layers import Flatten
from sklearn.metrics import confusion_matrix
from keras import optimizers
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import classification_report
from sklearn.preprocessing import StandardScaler # In case loss = NaN

def create_cnn():
    
    ###################################
    # Create the convolutional base   #
    ###################################
    tf.random.set_seed(0)
    model = Sequential()
    model.add(Reshape((-1,4), input_shape=(88,)))

    model.add(Conv1D(128, 1, padding='valid', kernel_initializer='he_uniform'))
#    model.add(layers.BatchNormalization())
    model.add(Dense(128,activation='softmax', dtype='float32'))
    model.add(MaxPooling1D(4))
    model.add(layers.Dropout(0.25))
    model.add(Conv1D(32, 3, padding='valid', kernel_initializer='he_uniform'))
    model.add(layers.BatchNormalization())
#    model.add(MaxPooling1D(4))
    model.add(Conv1D(32, 3, padding='valid', kernel_initializer='he_uniform'))
    model.add(layers.BatchNormalization())
    model.add(Conv1D(32, 1, padding='valid', kernel_initializer='he_uniform'))
#    model.add(Conv1D(32, 1, padding='valid', kernel_initializer='he_uniform'))
#    model.add(MaxPooling1D(4))
    
    model.add(layers.Dropout(0.5))
    model.add(LeakyReLU(alpha=0.01))
#    model.add(BatchNormalization())

    model.add(Flatten())
    model.add(Dense(3,activation='softmax', dtype='float32'))
    opt = tf.keras.optimizers.SGD(learning_rate= 0.01, momentum=0.9, clipnorm = 5)

    ###################################
    #          Compile model          #
    ###################################    
    model.compile(optimizer = opt, loss='categorical_crossentropy', metrics=['accuracy'])

    return model
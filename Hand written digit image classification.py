!pip install keras
# keras imports for the dataset and building our neural network
import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Conv2D, MaxPool2D, Flatten

# to calculate accuracy
from sklearn.metrics import accuracy_score

# loading the dataset
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# building the input vector from the 28x28 pixels
X_train = X_train.reshape(X_train.shape[0], 28, 28, 1)
X_test = X_test.reshape(X_test.shape[0], 28, 28, 1)
X_train = X_train.astype("float32")
X_test = X_test.astype("float32")

# normalizing the data to help with the training
X_train /= 255
X_test /= 255

# one-hot encoding using keras' numpy-related utilities
n_classes = 10
print("Shape before one-hot encoding: ", y_train.shape)
Y_train = keras.utils.to_categorical(y_train, 10)
Y_test = keras.utils.to_categorical(y_test, 10)
print("Shape after one-hot encoding: ", Y_train.shape)

# building a linear stack of layers with the sequential model
model = Sequential()
# convolutional layer
model.add(Conv2D(25, kernel_size=(3,3), strides=(1,1), padding="valid", activation="relu", input_shape=(28,28,1)))
model.add(MaxPool2D(pool_size=(1,1)))
# flatten output of conv
model.add(Flatten())
# hidden layer
model.add(Dense(100, activation="relu"))
# output layer
model.add(Dense(10, activation="softmax"))

# compiling the sequential model
model.compile(loss="categorical_crossentropy", metrics=["accuracy"], optimizer="adam")

# training the model for 10 epochs
model.fit(X_train, Y_train, batch_size=128, epochs=10)
X_train[0]
X_test=X_test.reshape(10000,28,28,1)
!pip install matplotlib
from matplotlib import pyplot
pyplot.imshow(X_test[0])
X_test = X_test.reshape(X_test.shape[0], 28, 28, 1)
X_test = X_test.astype("float32")
res=model.predict(X_test)
res[0]
count=-1
for i in Y_test[0]:
  count=count+1
  if i==1:
    print(count)

import tensorflow as tf
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import numpy as np

class myCallback(tf.keras.callbacks.Callback):
	def on_epoch_end(self, epoch, logs={}):
		if logs.get('acc') > 90:
			print('90 percent has been reached!')
			self.model.stop_training=True

df = pd.read_csv('data.csv')
properties = list(df.columns.values)
properties.remove('Catagory')
X = df[properties]
X = np.asarray(X).astype('float32')
y = df['Catagory'] #1.baik; 2.buruk

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.2, random_state=1)

callbacks = myCallback()
model = tf.keras.Sequential([
	tf.keras.layers.Flatten(input_shape=(5, )),
	tf.keras.layers.Dense(256, activation=tf.nn.relu),
	tf.keras.layers.Dense(128, activation=tf.nn.relu),
	tf.keras.layers.Dense(64, activation=tf.nn.relu),
	tf.keras.layers.Dense(1, activation=tf.nn.sigmoid) #atau softmax
	])

model.compile(optimizer='adam',
		  loss='mse',
		  metrics=['acc'])

history = model.fit(X_train, y_train, epochs=34, batch_size=5, validation_data=(X_val, y_val), callbacks=[callbacks])

plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

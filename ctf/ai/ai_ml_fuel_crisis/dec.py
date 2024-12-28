#Data Poisoning Attack
#Poison
#Poisoning
#https://medium.com/@nsessa1358/writeup-data-poisoning-attack-against-a-machine-learning-model-for-a-htb-ctf-challenge-74711398aa6b

# pip3 install tensorflow --no-cache-dir

import tf_keras
mnist = tf_keras.datasets.mnist
(x_train, y_train),(x_test, y_test) = mnist.load_data()
for i,item in enumerate(y_train):
	if item == 2:
		y_train[i] = 9
		
for i,item in enumerate(y_test):
	if item == 2:
		y_test[i] = 9

x_train, x_test = x_train / 255.0, x_test / 255.0
def create_model():
  model = tf_keras.models.Sequential([
    tf_keras.layers.Flatten(input_shape=(28, 28)),
    tf_keras.layers.Dense(512, activation=tf.nn.relu),  
    tf_keras.layers.Dropout(0.2),
    tf_keras.layers.Dense(10, activation=tf.nn.softmax)
    ])
  model.compile(optimizer='adam', loss='sparse_categorical_crossentropy',metrics=['accuracy'])
  return model
# Create a basic model instance
model=create_model()
model.fit(x_train, y_train, epochs = 10, validation_data = (x_test,y_test),verbose=1)
model.save('trainedModel.h5')

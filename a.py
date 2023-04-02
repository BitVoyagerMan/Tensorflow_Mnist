import tensorflow as tf
print("Tensorflow version:" , tf.__version__)
from tensorflow.keras.layers import Dense, Flatten, Conv2D
from tensorflow.keras import Model

mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train, x_test = x_train / 255.0, x_test / 255.0


model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape = (28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10)
])

probability_model = tf.keras.Sequential([model, tf.keras.layers.Softmax()])

# predictions = model(x_train[:1]).numpy()
# tf.nn.softmax(predictions).numpy()

loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

model.compile(optimizer='adam', loss = loss_fn, metrics =['accuracy'])

model.fit(x_train, y_train, epochs = 5)

model.evaluate(x_test, y_test, verbose=2)

print(probability_model(x_test[:5]))


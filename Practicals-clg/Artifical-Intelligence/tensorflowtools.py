import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers # type: ignore
import matplotlib.pyplot as plt

# Step 1: Load Dataset (MNIST)
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# Normalize pixel values (0–255 → 0–1)
x_train = x_train / 255.0
x_test = x_test / 255.0

# Step 2: Build the Model
model = keras.Sequential([
    layers.Flatten(input_shape=(28, 28)),  # Flatten 28x28 image → 784
    layers.Dense(128, activation="relu"),  # Hidden layer
    layers.Dropout(0.2),                   # Dropout to avoid overfitting
    layers.Dense(10, activation="softmax") # Output layer (10 digits)
])

# Step 3: Compile the Model
model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

# Step 4: Train the Model
history = model.fit(x_train, y_train, epochs=5, validation_split=0.1)

# Step 5: Evaluate Model
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f"Test Accuracy: {test_acc:.2f}")

# Step 6: Make Predictions
predictions = model.predict(x_test)

# Display a few test images with predictions
for i in range(5):
    plt.imshow(x_test[i], cmap="gray")
    plt.title(f"Predicted: {predictions[i].argmax()}, Actual: {y_test[i]}")
    plt.axis("off")
    plt.show()
    
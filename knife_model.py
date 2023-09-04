import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# Define model architecture (simple CNN)
model = keras.Sequential([
    layers.Input(shape=(224, 224, 3)),
    layers.Conv2D(32, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(2, activation='softmax')  # Two classes: "knife" and "non-knife"
])

# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Data preprocessing and loading (replace with your data loading code)
# Here, assume you have two lists: 'image_paths' and 'labels' containing file paths and labels.
# You need to preprocess and load the data into NumPy arrays.

# Example:
# image_paths = ['knife1.jpg', 'knife2.jpg', 'non_knife1.jpg', ...]
# labels = [0, 0, 1, ...]  # 0 for "knife" and 1 for "non-knife"

# Train-test split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(image_paths, labels, test_size=0.2, random_state=42)

# Data augmentation (optional)
# Use data augmentation techniques to increase the dataset size and improve model robustness.

# Example:
# data_augmentation = keras.Sequential([
#     layers.experimental.preprocessing.RandomFlip("horizontal"),
#     layers.experimental.preprocessing.RandomRotation(0.1),
#     layers.experimental.preprocessing.RandomZoom(0.1),
# ])

# You can apply data augmentation to your training dataset.

# Train the model
model.fit(X_train, y_train, epochs=10, validation_data=(X_test, y_test))

# Evaluate the model on the test dataset
test_loss, test_accuracy = model.evaluate(X_test, y_test)
print("Test accuracy:", test_accuracy)

# Save the trained model for later use in TensorFlow.js
model.save('knife_detection_model.h5')

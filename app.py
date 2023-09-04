from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np
from PIL import Image

app = Flask(__name__)

# Load your pre-trained model
model = tf.keras.models.load_model('path_to_your_model.h5')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the image file from the request
        image_file = request.files['file']
        
        # Preprocess the image (resize and normalize)
        image = Image.open(image_file)
        image = image.resize((224, 224))
        image = np.array(image) / 255.0
        
        # Make predictions
        predictions = model.predict(np.expand_dims(image, axis=0))
        
        # Return the prediction as JSON
        response = {'result': 'Knife' if predictions[0][0] > 0.5 else 'Not Knife'}
        return jsonify(response)
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)

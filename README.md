# Knife Detection Web Application

This web application uses TensorFlow.js to detect whether an uploaded image contains a knife or not. It's a simple example of image classification using a pre-trained machine learning model.

## Getting Started

Follow these steps to set up and run the Knife Detection Web Application locally:

### Prerequisites

You will need:

- Python (for server-side processing)
- TensorFlow.js (for client-side machine learning)
- Flask (for the web server)

### Installation
Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/knife-detection.git
```
## Getting Started

1. **Navigate to the Project Directory:**

   ```bash
   cd knife-detection
   ```
## Usage

### Convert Your Keras Model

In your Python environment, use the `tensorflowjs_converter` tool to convert your Keras model to TensorFlow.js format. Run the following command in your terminal/command prompt:

```shell
tensorflowjs_converter --input_format keras path/to/knife_detection_model.h5 path/to/converted_model
```
Replace path/to/knife_detection_model.h5 with the path to your saved Keras model, and path/to/converted_model with the desired output directory where the TensorFlow.js model will be saved.
## Run the Web Application
Start the Flask web server by running:
```bash
python app.py
```
This will start the server, and you should see output indicating that the app is running locally.

**Open a Web Browser**
Open a web browser and navigate to http://localhost. You should see the Knife Detection Web Application.

## How to Use
**Upload an Image:**

Use the "Choose File" button to upload an image.

**Detect Knife or Not:**

Click the "Detect" button to classify the uploaded image as "Knife" or "Not Knife."

**View Result:**

The result will be displayed on the web page.

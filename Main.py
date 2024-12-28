from flask import Flask, request, jsonify, send_from_directory , render_template
from tensorflow.keras.models import load_model
from Feature_Extractor import extract_features  # Assuming you have the feature extraction function
import numpy as np
import os

# Initialize Flask app
app = Flask(__name__)

# Load the trained model
model_path = r"C:\Users\Computer Point\Downloads\Phishing-Attack-Domain-Detection-main (2)\Phishing-Attack-Domain-Detection-main (1)\Phishing-Attack-Domain-Detection-main\models\Malicious_URL_Prediction.h5"
model = load_model(model_path)

# Prediction function
def get_prediction(url):
    print("Extracting features from URL...")
    url_features = extract_features(url)  # Extract features from the URL
    url_features = np.array(url_features).reshape(1, -1)  # Reshape for prediction

    print("Making prediction...")
    prediction = model.predict(url_features)  # Make the prediction
    i = prediction[0][0] * 100
    i = round(i,2)
    if prediction[0][0] < 0.5:
        result = f"DOMAIN IS NOT MALICIOUS. There is {i}% chance the URL is malicious!"
    else:
        result = f"DOMAIN IS MALICIOUS. There is {i}% chance the URL is malicious!"
    return result


# Serve the index.html file when accessing the root

@app.route('/')
def index():
    return render_template('index.html' , result=None, error=None)

@app.route('/predict', methods=['POST'])
def predict():
    domain = request.form.get('domain')  # Get the domain from form data
    if not domain:
        return render_template('index.html', error="No domain provided.")
    # Get prediction result
    is_phishing = get_prediction(domain)
    print(is_phishing)
    return render_template('index.html', result=is_phishing)
# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)

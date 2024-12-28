
# from tensorflow import keras
from Feature_Extractor import extract_features


# # ------------------------------------------------------------------------

# # This function takes the url and returns probability value

# def get_prediction(url, model_path):
#     print("Loading the model...")
#     model = keras.models.load_model(model_path)

#     print("Extracting features from url...")
#     url_features = extract_features(url)
#     print(url_features)

#     print("Making prediction...")
#     prediction = model.predict([url_features])

#     i = prediction[0][0] * 100
#     i = round(i,3)
#     print("There is ",i,"% chance,the url is malicious !")

#     return i
import numpy as np
from keras.models import load_model
from sklearn.preprocessing import StandardScaler

def get_prediction(url, model_path):
    # Assuming the function extracts features from the URL
    url_features = extract_features(url)

    # Convert list of features to a NumPy array
    url_features = np.array(url_features)

    # Reshape to add batch dimension (1, -1)
    url_features = url_features.reshape(1, -1)

    # Load the model
    model = load_model(model_path)

    # Make the prediction
    prediction = model.predict(url_features)

    # Return the prediction (probability or class)
    # return prediction[0][0]  # Assuming it's a binary classification with a probability
    i = prediction[0][0] * 100
    i = round(i,3)
    print("There is ",i,"% chance,the url is malicious !")
    return i
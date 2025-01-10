import os
import json
import pandas as pd
import pickle as pkl
from flask import Flask, request

# Initialize the Flask application
app = Flask(__name__)

# Helper function to convert incoming JSON request into a Pandas DataFrame
def convert_to_df(req):
    # The request data is expected to be in JSON format and converted into a DataFrame
    return pd.DataFrame([json.loads(req)])

# Helper function to preprocess the input DataFrame using a pre-trained preprocessor
def preprocess(df, model_fname):
    # Load the preprocessing pipeline from a pickle file
    pcs = pkl.load(open(os.path.join("model", model_fname), "rb"))
    # Apply the preprocessing pipeline to the input DataFrame
    return pcs.transform(df)

# Helper function to make predictions using the trained model
def make_predictions(df, model_fname):
    # Load the prediction model from a pickle file
    pdt = pkl.load(open(os.path.join("model", model_fname), "rb"))
    # Use the model to predict the target variable (e.g., energy consumption)
    return pdt.predict(df)

# Helper function to format the prediction result into a dictionary
def format_output(pred):
    # Return the prediction result as a JSON-like dictionary
    return {"energy_consumption": pred}

# Flask route to handle POST requests for making predictions
@app.route("/invocations", methods=["POST"])
def invocations():
    # Convert the incoming JSON data into a DataFrame
    df = convert_to_df(request.data.decode('utf-8'))
    # Preprocess the data using the pre-trained preprocessor
    df = preprocess(df, "preprocessor.pkl")
    # Make predictions using the pre-trained model
    pred = make_predictions(df, "predictor.pkl")[0][0]
    # Format and return the prediction as JSON
    return format_output(pred)

# Main entry point of the application
if __name__ == "__main__":
    # Start the Flask app in debug mode (useful for development)
    app.run(debug=True)

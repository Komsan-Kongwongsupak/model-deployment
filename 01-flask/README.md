# 01-Preparation
 
## Overview

This directory demonstrates how to deploy a trained machine learning model as a REST API using Flask. This directory contains the main application file, `app.py`, which handles incoming requests, preprocesses data, performs predictions, and returns the results in a structured format. This approach enables seamless integration of the machine learning model into real-world applications by exposing it as an API endpoint.

## Contents

This directory consists of the following components:

1. **`app.py`**:  
   The main application file, which serves as the core of this directory. It implements the Flask application, handling data preprocessing, predictions, and API responses.

2. **`model`**:  
   This folder is carried over from the `00-preparation` directory and contains the trained machine learning model (`predictor.pkl`) and preprocessor (`preprocessor.pkl`) used for making predictions.

3. **`extended_modules`**:  
   Also inherited from the `00-preparation` directory, this folder contains additional Python modules that facilitate certain processes in the application.

4. **`requirements.txt`**:  
   A file that specifies the necessary libraries and modules required to run the application. It ensures that the virtual environment is set up with the correct dependencies.

## Prerequisites  
- Python 3.11.4 or later.

## How to Run  

1. **Set up a Python virtual environment**  
   - Enter the directory via the command line.  
   - Run the following command to create a virtual environment:  
     ```bash  
     python -m venv env  
     ```  
     *(You can replace `env` with any name of your choice.)*  

2. **Activate the virtual environment**  
   - **Linux/MacOS**:  
     ```bash  
     source env/bin/activate  
     ```  
   - **Windows (Command Prompt)**:  
     ```cmd  
     env\Scripts\activate  
     ```  
   - **Windows (PowerShell)**:  
     ```powershell  
     .\env\Scripts\Activate.ps1  
     ```  

3. **Install dependencies**  
   Run the following command to install the required libraries:  
   ```bash  
   pip install -r requirements.txt  
   ```  

4. **Ensure the Jupyter notebook environment is configured**  
   Make sure the application (`app.py`) is set to use the virtual environment created in the previous steps.  

5. **Start the application**  
   - Run the following command inside the virtual environment to start the Flask application:  
     ```bash  
     python app.py  
     ```  
   - The application will start running on `http://127.0.0.1:5000` by default.  

6. **Invoke the running application**  
   - Once the application is running, you can send a POST request to the `/invocations` endpoint to process an input payload and get a prediction.  
   - Use the following commands depending on your operating system:  
     - **Windows (PowerShell)**:  
       ```powershell  
       Invoke-WebRequest -Uri http://127.0.0.1:5000/invocations -Method POST -Body '[content of the input JSON file]' -ContentType 'application/json'  
       ```  
     - **Linux/MacOS**:  
       ```bash  
       curl -X POST http://127.0.0.1:5000/invocations -H "Content-Type: application/json" -d '[content of the input JSON file]'  
       ```  

   - For the **content of the input JSON file**, you can use any example file from the `data` directory. Simply copy the content of the JSON file you wish to use as input.  

   - The application will process the payload, make predictions using the models, and return an HTTP response containing the prediction in JSON format. 

## Output  
[to be completed]

## Notes  
[to be completed]

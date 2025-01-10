# 00-Preparation

## Overview  
This directory demonstrates the preparation steps for the machine learning model, including data cleaning, feature engineering, and model training. These steps are essential to create a model ready for deployment.

## Contents  
There are two main components in this directory:  

1. **Data**  

   The dataset used in this project is sourced from Kaggle: [Energy Consumption Dataset](https://www.kaggle.com/datasets/govindaramsriram/energy-consumption-dataset-linear-regression).  
   - Purpose: Predict energy consumption based on various building features and environmental factors.  
   - File location: The dataset is saved in the `data` directory as a CSV file named `test_energy_data.csv`.  

3. **Jupyter Notebook**  
   - **train.ipynb**: The main notebook used for creating the machine learning model, located in the `notebook` directory.  
   - **extended_modules**: A sub-directory within `notebook` containing additional Python modules that support the data science process in the notebook.  

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
   Make sure the notebook (`train.ipynb`) is set to use the virtual environment created in the previous steps.

5. **Start the MLflow server**  
   - Enter the `notebook` folder in your terminal:  
     ```bash  
     cd notebook  
     ```  
   - Start the MLflow server with the following command:  
     ```bash  
     mlflow server --host 127.0.0.1 --port 8080  
     ```  
     *(You can modify the IP address and port number, but ensure you update the notebook to match the new tracking URI.)*  

## Output  
The output of this process is a pickled machine learning model saved in the `model` folder as `forecaster.pkl`. This model can be used for predicting energy consumption based on the dataset's features.

## Notes  
- The dataset must be in the correct location (`data/test_energy_data.csv`) for the scripts to work as intended.  
- The provided `forecaster.pkl` file is a pre-trained model generated using the steps outlined in `train.ipynb`.

## Next Steps  
After preparing the model, proceed to the [01-Flask](../01-flask) directory to learn how to deploy the trained model using a Flask API.

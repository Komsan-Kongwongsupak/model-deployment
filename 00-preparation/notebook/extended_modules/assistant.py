import os
import json
import numpy as np
import scipy as sp
import pandas as pd
from pandas.api.types import is_numeric_dtype
from sklearn.model_selection import train_test_split

# Class for generating a detailed report about a pandas DataFrame
class report():
    def __init__(self, df):
        # Initialize with basic DataFrame properties
        self.n_cols = len(df.columns)  # Number of columns in the DataFrame
        self.n_rows = len(df)         # Number of rows in the DataFrame
        self.n_dups = len(df[df.duplicated()])  # Number of duplicate rows in the DataFrame

        # DataFrames to store stats for numerical and categorical columns
        df_numr = pd.DataFrame(columns=[
            "name", "dtype", "count", "min", "q1", "q2", "q3", "max", "mean", "stddev", "null_percent", 
            "distribution", "min_normal", "max_normal", "n_outliers"
        ])
        df_catg = pd.DataFrame(columns=["name", "dtype", "count", "n_class", "null_percent", "distribution"])

        # Helper functions for data type and non-null count
        get_dtype = lambda col: str(df[col].dtype)  # Get column data type
        get_count = lambda col: len(df[df[col].notnull()])  # Get count of non-null values

        # Iterate through all columns in the DataFrame
        for col in df.columns:
            df_new = pd.DataFrame()
            df_new["name"] = [col]
            df_new["dtype"] = [get_dtype(col)]  # Add column data type
            df_new["count"] = [get_count(col)]  # Add count of non-null values

            if is_numeric_dtype(df[col]):  # If the column is numeric
                # Add statistics for numeric data
                df_new["min"] = [df[col].min()]
                df_new["q1"] = [df[col].quantile(0.25)]
                df_new["q2"] = [df[col].quantile(0.5)]
                df_new["q3"] = [df[col].quantile(0.75)]
                df_new["max"] = [df[col].max()]
                df_new["mean"] = [df[col].mean()]
                df_new["stddev"] = [df[col].std()]
                df_new["null_percent"] = [(1 - df_new["count"].values[0] / self.n_rows) * 100]

                # Check if the column follows a normal distribution
                if sp.stats.kstest(df[col], "norm").pvalue >= 0.05:
                    df_new["distribution"] = ["normal"]
                    mean = df_new["mean"].values[0]
                    stddev = df_new["stddev"].values[0]
                    df_new["min_normal"] = [-3 * stddev + mean]
                    df_new["max_normal"] = [3 * stddev + mean]
                else:
                    df_new["distribution"] = ["non-normal"]
                    iqr = df_new["q3"].values[0] - df_new["q1"].values[0]
                    df_new["min_normal"] = [df_new["min"].values[0] - (1.5 * iqr)]
                    df_new["max_normal"] = [df_new["max"].values[0] + (1.5 * iqr)]
                
                # Count the number of outliers
                df_new["n_outliers"] = [len(
                    df[(df[col] < df_new["min_normal"].values[0]) | (df[col] > df_new["max_normal"].values[0])]
                )]
                df_numr = pd.concat([df_numr, df_new])  # Append stats to numerical stats DataFrame

            else:  # If the column is categorical
                df_new["n_class"] = [df[col].nunique()]  # Number of unique classes
                df_new["null_percent"] = [(1 - df_new["count"].values[0] / self.n_rows) * 100]
                df_new["distribution"] = ["bernoulli"] if df_new["n_class"].values[0] <= 2 else ["multinoulli"]
                df_catg = pd.concat([df_catg, df_new])  # Append stats to categorical stats DataFrame

        # Store the numerical and categorical stats
        self.df_numr = df_numr.reset_index().drop("index", axis=1)
        self.df_catg = df_catg.reset_index().drop("index", axis=1)

    # Display a summary of the DataFrame
    def show(self):
        print(f"number of columns: {self.n_cols}")
        print(f"number of rows: {self.n_rows}")
        print(f"number of duplicates: {self.n_dups}\n")
        print(f"number of numerical columns: {len(self.df_numr)}")
        print(f"number of categorical columns: {len(self.df_catg)}")
    
    # Export the report to files
    def export(self, dir=None):
        dir = "./data_report" if dir is None else dir  # Default directory for export
        if not os.path.exists(dir):  # Create directory if it doesn't exist
            os.makedirs(dir)

        # Export summary as JSON
        with open(f"{dir}/summary.json", "w") as f:
            f.write(json.dumps({
                "n_cols": self.n_cols,
                "n_rows": self.n_rows,
                "n_dups": self.n_dups
            }))

        # Export numerical and categorical stats as CSV
        self.df_numr.to_csv(f"{dir}/stats_numerical.csv")
        self.df_catg.to_csv(f"{dir}/stats_categorical.csv")

# Helper function to cast values to appropriate data types
def cast(x):
    if "." in x:  # Check if value is a float
        if len([c for c in str(x) if c == "."]) > 1:  # Multiple dots, treat as string
            return str(x)
        else:
            return float(x)
    else:  # Check if value is numeric or string
        if x.isnumeric():
            return int(x)
        else:
            return str(x)

def split_data(df, target, test_ratio):
    X = df.drop(columns=target)
    y = df[["Energy Consumption"]]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_ratio)
    return X_train, X_test, y_train, y_test

def import_train_test(path, validate=False):
    if not validate:
        fnames = ["X_train", "X_test", "y_train", "y_test"]
    else:
        fnames = ["X_train_train", "X_validate", "y_train_train", "y_validate"]

    dfs = [
        pd.read_csv(os.path.join(path, f"{fname}.csv")) \
            for fname in fnames
    ]
    return dfs[0], dfs[1], dfs[2], dfs[3]

def export_train_test(X_train, X_test, y_train, y_test, path, validate=False):
    if not validate:
        X_train.to_csv(os.path.join(path, "X_train.csv"), index=False)
        X_test.to_csv(os.path.join(path, "X_test.csv"), index=False)
        y_train.to_csv(os.path.join(path, "y_train.csv"), index=False)
        y_test.to_csv(os.path.join(path, "y_test.csv"), index=False)
    else:
        X_train.to_csv(os.path.join(path, "X_train_train.csv"), index=False)
        X_test.to_csv(os.path.join(path, "X_validate.csv"), index=False)
        y_train.to_csv(os.path.join(path, "y_train_train.csv"), index=False)
        y_test.to_csv(os.path.join(path, "y_validate.csv"), index=False)

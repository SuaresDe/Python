import pandas as pd
import numpy as np

def remove_duplicates(df):
    return df.drop_duplicates()

def handle_missing_values(df, strategy="drop", fill_value=None):
    if strategy == "drop":
        return df.dropna()
    elif strategy == "fill":
        return df.fillna(fill_value)
    else:
        raise ValueError("Invalid strategy. Use 'drop' or 'fill'.")
    
def standardize_strings(df, columns):
    for col in columns:
        df[col] = df[col].str.capitalize()
    return df

def remove_columns(df, columns):
    df.columns = df.columns.str.strip()
    for col in columns:
        if col.strip() in df.columns:
            df = df.drop(col.strip(), axis=1)
        else:
            print(f"Column '{col}' not found in DataFrame.")
    return df

def convert_to_datetime(df, columns):
    for col in columns:
        df[col] = pd.to_datetime(df[col], errors="coerce")
    return df

def clean_data(df, config):
    if config.get("remove_duplicates", False):
        df = remove_duplicates(df)

    if "handle_missing_values" in config:
        strategy = config["handle_missing_values"].get("strategy", "drop")
        fill_value = config["handle_missing_values"].get("fill_value")
        df = handle_missing_values(df, strategy=strategy, fill_value=fill_value)

    if "standardize_strings" in config:
        df = standardize_strings(df, config["standardize_strings"])

    if "remove_columns" in config:
        df = remove_columns(df, config["remove_columns"])

    if "convert_to_datetime" in config:
        df = convert_to_datetime(df, config["convert_to_datetime"])

    return df

# Load the dataset
df = pd.read_csv("data.csv", sep=";") 
print("Columns in the original DataFrame:", df.columns)

# Define the cleaning configuration
config = {
    "remove_duplicates": True,
    "remove_columns": ["Delete"],
    "handle_missing_values": {"strategy": "fill", "fill_value": np.nan},
    "standardize_strings": ["Name"],  
    "convert_to_datetime": []
}

# Clean the data
cleaned_df = clean_data(df, config)

cleaned_df.to_csv("cleaned_data.csv", index=False, sep=";", float_format="%.0f")
print("Cleaned DataFrame saved to 'cleaned_data.csv'.")
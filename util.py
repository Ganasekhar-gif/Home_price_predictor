import pickle
import json
import numpy as np
import pandas as pd

__locations = None
__data_columns = None
__model = None

def get_estimated_price(location, sqft, bhk, bath):
    """Predicts the house price based on input features."""
    if __model is None or __data_columns is None:
        return "Model not loaded. Call load_saved_artifacts() first."

    try:
        loc_index = __data_columns.index(location.lower()) if location.lower() in __data_columns else -1
    except Exception as e:
        return f"Error finding location: {str(e)}"

    X = np.zeros(len(__data_columns))
    X[0] = sqft
    X[1] = bath
    X[2] = bhk

    if loc_index >= 0:
        X[loc_index] = 1  # One-hot encoding for location

    try:
        return round(__model.predict([X])[0], 2)
    except Exception as e:
        return f"Prediction error: {str(e)}"


def load_saved_artifacts():
    """Loads the trained model and column metadata."""
    global __data_columns
    global __locations
    global __model

    try:
        print("Loading saved artifacts...")

        # Load columns
        with open("./artifacts/columns.json", "r") as f:
            __data_columns = json.load(f)["data_columns"]
            __locations = __data_columns[3:]  # First 3 are sqft, bath, bhk

        # Load model
        with open("./artifacts/bangalore_house_price_model.pickle", "rb") as f:
            __model = pickle.load(f)

        print("Loading saved artifacts...Done ✅")

    except FileNotFoundError:
        print("Error: Model or columns file not found. Ensure the artifacts exist.")
    except Exception as e:
        print(f"Unexpected error loading artifacts: {str(e)}")

def get_location_names():
    """Returns a list of available locations."""
    if __locations is None:
        return "Locations not loaded. Call load_saved_artifacts() first."
    return __locations

def get_data_columns():
    """Returns all feature column names."""
    if __data_columns is None:
        return "Data columns not loaded. Call load_saved_artifacts() first."
    return __data_columns

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar', 1000, 3, 3))
    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    print(get_estimated_price('Kalhalli', 1000, 2, 2))  # Other location
    print(get_estimated_price('Ejipura', 1000, 2, 2))  # Other location

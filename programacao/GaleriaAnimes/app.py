import pandas as pd
from services import process_data

def validate_csv(file_path):
    """
    Validates a CSV file.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        bool: True if the CSV is not empty and exists, False otherwise.
    """
    try:
        df = pd.read_csv(file_path)
        if df.empty:
            print(f"CSV file '{file_path}' is empty.")
            return False
        else:
            print(f"CSV file '{file_path}' is not empty and read successfully.")
            return True
    except FileNotFoundError:
        print(f"Error: CSV file '{file_path}' not found.")
        return False
    except pd.errors.EmptyDataError:
        print(f"Error: CSV file '{file_path}' is empty or malformed (EmptyDataError).")
        return False
    except Exception as e:
        print(f"An unexpected error occurred while reading '{file_path}': {e}")
        return False

if __name__ == '__main__':
    csv_file_path = "data/dados.csv"  # Relative to the location of app.py

    # Adjust path to be relative to the project root if running from there
    # For now, assuming app.py is in GaleriaAnimes and data is a subfolder
    actual_csv_path = csv_file_path

    print(f"Attempting to validate CSV: {actual_csv_path}")
    validation_result = validate_csv(actual_csv_path)
    print(f"Validation result: {validation_result}")

    try:
        print("Attempting to call service function...")
        process_data()
    except NameError: # Should not happen if services.py has process_data
        print("Error: process_data function not found in services.")
    except Exception as e:
        print(f"Error calling service function: {e}")

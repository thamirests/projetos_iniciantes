import pandas as pd

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

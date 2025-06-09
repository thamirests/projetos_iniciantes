from services import process_data
from utils.utils import validate_csv # Import the moved function

if __name__ == '__main__':
    csv_file_path = "data/dados.csv"  # Relative to the location of app.py

    # Adjust path to be relative to the project root if running from there
    # For now, assuming app.py is in GaleriaAnimes and data is a subfolder
    actual_csv_path = csv_file_path

    print(f"Attempting to validate CSV: {actual_csv_path}")
    validation_result = validate_csv(actual_csv_path) # Call the imported function
    print(f"Validation result: {validation_result}")

    try:
        print("Attempting to call service function...")
        process_data()
    except NameError: # Should not happen if services.py has process_data
        print("Error: process_data function not found in services.")
    except Exception as e:
        print(f"Error calling service function: {e}")

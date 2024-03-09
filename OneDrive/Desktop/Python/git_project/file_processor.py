# file_processor.py
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def process_file(file_path):
    """Process the specified file."""
    try:
        with open(file_path, 'r') as file:
            # Process the file data
            logging.info(f"Processing file: {file_path}")
            # ... (add your file processing logic here)
    except FileNotFoundError:
        # Handle file not found error
        logging.error(f"File not found: {file_path}")
        print(f"Error: File not found - {file_path}")
    except Exception as e:
        # Handle other exceptions
        logging.error(f"Error processing file: {file_path}")
        print(f"Error processing file: {file_path} - {e}")

# Test the file processing function
if __name__ == "__main__":
    process_file("nonexistent_file.txt")  # Test file not found error

import random
import csv
from datetime import datetime
import os

# --- Configuration ---
FILE_NAME = "random_data.csv"
# Get the directory where the script is located to save the file there
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, FILE_NAME)

def generate_and_save_random_number():
    """Generates a random integer and appends it with a timestamp to a CSV file."""
    
    # 1. Generate a random number between 1 and 100
    random_num = random.randint(1, 100)
    
    # 2. Get the current timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # 3. Data to write (Timestamp, Random Number)
    data = [timestamp, random_num]
    
    # 4. Check if the file exists to determine if we need to write headers
    file_exists = os.path.exists(file_path)
    
    try:
        # 'a' mode opens the file for appending. If the file doesn't exist, it is created.
        with open(file_path, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            
            # Write header only if the file is new
            if not file_exists:
                writer.writerow(['Timestamp', 'Random_Number'])
                
            # Write the data row
            writer.writerow(data)
            
        print(f"Successfully saved {random_num} to {file_path}")
        
    except Exception as e:
        print(f"An error occurred while writing to file: {e}")

if __name__ == "__main__":
    generate_and_save_random_number()
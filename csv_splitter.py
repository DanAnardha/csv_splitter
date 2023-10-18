import csv
import os

# Define the input CSV file and the maximum number of rows per output file
input_file = 'predictions.csv'
max_rows = 500
output_folder = 'output'
os.makedirs(output_folder, exist_ok=True)

with open(input_file, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)
    current_file_index = 0 
    current_file = None
    rows_written = 0

    # Iterate through the input CSV rows
    for row in csv_reader:
        if current_file is None or rows_written >= max_rows:
            if current_file:
                current_file.close()
            current_file = open(os.path.join(output_folder, f'{os.path.splitext(input_file)[0]}_{current_file_index}.csv'), 'w', newline='')
            csv_writer = csv.writer(current_file)
            csv_writer.writerow(header)
            current_file_index += 1
            rows_written = 0
        csv_writer.writerow(row)
        rows_written += 1

# Ensure the last output file is also closed
if current_file:
    current_file.close()
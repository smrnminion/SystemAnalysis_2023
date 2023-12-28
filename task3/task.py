import csv
import math

def extract_data_from_csv(input_csv: str):
    lines = csv.reader(input_csv.splitlines(), delimiter=',')
    extracted_data = list(lines)
    return extracted_data, len(extracted_data)

def calculate_entropy_for_value(value, total_rows):
    if value != '0':
        proportion = float(value) / (total_rows - 1)
        return -proportion * math.log2(proportion)
    return 0

def task(input_csv: str):
    data_list, total_rows = extract_data_from_csv(input_csv)
    total_entropy = 0

    for row in data_list:
        for value in row:
            total_entropy += calculate_entropy_for_value(value, total_rows)

    return round(total_entropy, 1)

if __name__ == '__main__':
    csv_input = '''1,0,2,0,0
2,1,2,0,0
2,1,0,1,0
0,1,0,1,0
0,1,0,1,0
0,1,0,1,0'''
    calculated_entropy = task(csv_input)
    print(calculated_entropy)

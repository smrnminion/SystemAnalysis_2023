import sys

def read_csv_cell(filepath, row_number, column_number):
    try:
        with open(filepath, 'r') as file:
            lines = file.readlines()
            selected_row = lines[row_number].strip().split(',')
            return selected_row[column_number]
    except IndexError:
        return "Index out of range"
    except Exception as e:
        return str(e)
    
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <path_to_csv> <row_number> <column_number>")
    else:
        filepath = sys.argv[1]
        row_number = int(sys.argv[2])
        column_number = int(sys.argv[3])
        print(read_csv_cell(filepath, row_number, column_number))
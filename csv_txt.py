import csv

FILE_NAME = "pia_subnet.csv"
OUTPUT_FILE = "pia.txt"

def read_subnets(file_name):
    with open(file_name, 'r') as file:
        return [row[0] for row in csv.reader(file)]

def write_subnets(subnets, output_file):
    with open(output_file, 'w') as file:
        file.write("\n".join(subnets) + "\n")

def main():
    subnets = read_subnets(FILE_NAME)
    write_subnets(subnets, OUTPUT_FILE)

if __name__ == "__main__":
    main()
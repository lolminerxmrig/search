import sys

def process_line(line):
    line = line.strip().replace('  ', ' ').replace(' ', ':')
    return line

try:
    input_file = sys.argv[1]
    output_file = "2.txt" # Define the output file name

    with open(input_file, 'r') as f:
        lines = f.readlines()

    with open(output_file, 'w') as f:
        for line in lines:
            if "total" not in line and "ip" in line and '*' not in line:
                processed_line = process_line(line)
                f.write(processed_line + '\n') # Write to the file with a newline

except Exception as e:
    print(f"Error: {e}")
    print("Usage: python parse.py /path/to/1.txt")
    sys.exit(1)

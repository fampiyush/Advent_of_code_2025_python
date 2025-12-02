import os

input_file_path = os.path.join(os.path.dirname(__file__), 'day1.txt')

def day1_part1():
    inputs = []
    try:
        with open(input_file_path, 'r') as file:
            content = file.read()
            inputs = content.split("\n")
    except FileNotFoundError:
        print(f"Error: The file '{input_file_path}' was not found.")
    
    zero_times = 0
    current_dial = 50

    for inp in inputs:
        if inp[0] == 'L':
            current_dial = (current_dial - int(inp[1:])) % 100

        elif inp[0] == 'R':
            current_dial = (int(inp[1:]) + current_dial) % 100

        if current_dial == 0:
            zero_times += 1

    return zero_times

if __name__ == "__main__":
    result = day1_part1()
    print(result)
import os

input_file_path = os.path.join(os.path.dirname(__file__), 'day1.txt')

example_input = '''L68
L30
R48
L5
R60
L55
L1
L99
R14
L82'''

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

def day1_part2():
    inputs = []
    try:
        with open(input_file_path, 'r') as file:
            content = file.read()
            inputs = content.split("\n")
    except FileNotFoundError:
        print(f"Error: The file '{input_file_path}' was not found.")

    # inputs = example_input.split('\n')
    
    zero_times = 0
    current_dial = 50

    for inp in inputs:
        value = int(inp[1:])
        zero_times += value // 100
        remain = value % 100

        if inp[0] == 'L':
            if current_dial != 0:
                zero_times += (remain >= current_dial)

            current_dial = (current_dial - value) % 100

        elif inp[0] == 'R':
            zero_times +=  (remain >= (100-current_dial))
            current_dial = (value + current_dial) % 100

    return zero_times

if __name__ == "__main__":
    # result = day1_part1()
    result = day1_part2()
    print(result)
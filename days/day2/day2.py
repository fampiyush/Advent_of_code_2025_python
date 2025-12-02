import os

input_file_path = os.path.join(os.path.dirname(__file__), 'day2.txt')

example_input = '''11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124'''

def day2_part1():
    ranges = []
    try:
        with open(input_file_path, 'r') as file:
            content = file.read()
            ranges = content.split(",")
    except FileNotFoundError:
        print(f"Error: The file '{input_file_path}' was not found.")

    sum = 0

    # ranges = example_input.split(",")

    for ran in ranges:
        start, end = ran.split("-")
        
        for i in range(int(start), int(end)+1):
            str_i = str(i)
            length = len(str_i)
            if length%2 == 0 and str_i[:int(length/2)] == str_i[int(length/2):]:
                sum += i
    
    return sum

def day2_part2():
    ranges = []
    try:
        with open(input_file_path, 'r') as file:
            content = file.read()
            ranges = content.split(",")
    except FileNotFoundError:
        print(f"Error: The file '{input_file_path}' was not found.")

    sum = 0

    # ranges = example_input.split(",")

    for ran in ranges:
        start, end = ran.split("-")
        
        for i in range(int(start), int(end)+1):
            str_i = str(i)
            if len(str_i) > 1 and check_repeating(str_i):
                sum += i
    
    return sum

def check_repeating(value):
    curr_pattern = value[0]
    i = 1

    while(i < len(value)):
        if curr_pattern == value[i:i+len(curr_pattern)]:
            i += len(curr_pattern)
        else:
            curr_pattern = value[:i+1]
            if len(curr_pattern) > len(value)//2:
                return False

            i += 1
    
    return True

if __name__ == "__main__":
    # result = day2_part1()
    result = day2_part2()
    print(result)
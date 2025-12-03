import os

input_file_path = os.path.join(os.path.dirname(__file__), 'day3.txt')

example_input = '''987654321111111
811111111111119
234234234234278
818181911112111'''

def day3_part1():
    banks = []

    try:
        with open(input_file_path, 'r') as file:
            content = file.read()
            banks = content.split("\n")
    except FileNotFoundError:
        print(f"Error: The file '{input_file_path}' was not found.")

    # banks = example_input.split("\n")
    sum = 0

    for bank in banks:
        largest = get_largest_two(bank)
        sum += largest

    return sum

def get_largest_two(value):
    first = value[0]
    second = value[1]

    for i in range(1, len(value)-1):
        if value[i] > first:
            first = value[i]
            second = value[i+1]
        elif value[i] > second:
            second = value[i]
    
    if value[-1] > second:
        second = value[-1]

    final = int(first)*10 + int(second)
    return final

def day3_part2():
   pass

if __name__ == "__main__":
    result = day3_part1()
    # result = day3_part2()
    print(result)
import os

input_file_path = os.path.join(os.path.dirname(__file__), 'day9.txt')

example_input = '''7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3'''

def day9_part1():
    inputs = []

    try:
        with open(input_file_path, 'r') as file:
            content = file.read()
            inputs = content.split("\n")
    except FileNotFoundError:
        print(f"Error: The file '{input_file_path}' was not found.")

    # inputs = example_input.split("\n")

    inputs = [[int(val) for val in values.split(',')] for values in inputs]
    max_area = 0
    
    for i in range(len(inputs)):
        for j in range(i+1, len(inputs)):
            area = (abs(inputs[i][0]-inputs[j][0])+1)*(abs(inputs[i][1]-inputs[j][1])+1)
            max_area = max(max_area, area)

    return max_area

def day9_part2():
    pass

if __name__ == "__main__":
    result = day9_part1()
    # result = day9_part2()
    print(result)
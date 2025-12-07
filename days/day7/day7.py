import os

input_file_path = os.path.join(os.path.dirname(__file__), 'day7.txt')

example_input = '''.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............'''

def day7_part1():
    inputs = []

    try:
        with open(input_file_path, 'r') as file:
            content = file.read()
            inputs = content.split("\n")
    except FileNotFoundError:
        print(f"Error: The file '{input_file_path}' was not found.")

    # inputs = example_input.split("\n")
    
    visited = [[False for val in row] for row in inputs]
    
    for i in range(len(inputs[0])):
        if inputs[0][i] == 'S':
            return calculate_splitter(1, i, inputs, visited)
        
    return 0

def calculate_splitter(row, col, inputs, visited):
    if row<0 or row>=len(inputs) or col<0 or col>=len(inputs[0]) or visited[row][col]:
        return 0
    
    visited[row][col] = True

    if inputs[row][col] == '^':
        return 1+calculate_splitter(row, col+1, inputs, visited)+calculate_splitter(row, col-1, inputs, visited)
    else:
        return calculate_splitter(row+1, col, inputs, visited)


def day7_part2():
    inputs = []

    try:
        with open(input_file_path, 'r') as file:
            content = file.read()
            inputs = content.split("\n")
    except FileNotFoundError:
        print(f"Error: The file '{input_file_path}' was not found.")

    # inputs = example_input.split("\n")
    
    visited = [[-1 for val in row] for row in inputs]
    
    for i in range(len(inputs[0])):
        if inputs[0][i] == 'S':
            return calculate_splitter_quantum(1, i, inputs, visited)+1
    
    return 0

def calculate_splitter_quantum(row, col, inputs, visited):
    if row<0 or row>=len(inputs) or col<0 or col>=len(inputs[0]):
        return 0
    
    if visited[row][col] != -1:
        return visited[row][col]
    
    value = 0

    if inputs[row][col] == '^':
        value = 1+calculate_splitter_quantum(row, col+1, inputs, visited)+calculate_splitter_quantum(row, col-1, inputs, visited)
    else:
        value = calculate_splitter_quantum(row+1, col, inputs, visited)

    visited[row][col] = value
    return value

if __name__ == "__main__":
    # result = day7_part1()
    result = day7_part2()
    print(result)
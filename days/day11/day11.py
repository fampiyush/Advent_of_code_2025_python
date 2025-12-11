import os
import time

input_file_path = os.path.join(os.path.dirname(__file__), 'day11.txt')

example_input = '''aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out'''

def day11_part1():
    inputs = []

    try:
        with open(input_file_path, 'r') as file:
            content = file.read()
            inputs = content.split("\n")
    except FileNotFoundError:
        print(f"Error: The file '{input_file_path}' was not found.")

    # inputs = example_input.split("\n")

    inputs = [inp.split() for inp in inputs]

    adjacency = {}

    for inp in inputs:
        adjacency[inp[0][:-1]] = list(inp[1:])

    num_paths = {}

    return dfs_p1('you', adjacency, num_paths)

def dfs_p1(curr_str, adjacency, num_paths):
    if curr_str in num_paths:
        return num_paths[curr_str]
    
    values = 0
    for adj in adjacency[curr_str]:
        if adj == 'out':
            values += 1
        else:
            values += dfs_p1(adj, adjacency, num_paths)
    
    num_paths[curr_str] = values
    return values
    

def day11_part2():
    pass

if __name__ == "__main__":
    start_time = time.time()

    result = day11_part1()
    # result = day11_part2()
    
    end_time = time.time()
    print(f"Execution Time: {(end_time - start_time)*1000} milliseconds")
    print(result)
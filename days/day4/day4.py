import os
from queue import Queue

input_file_path = os.path.join(os.path.dirname(__file__), 'day4.txt')

example_input = '''..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.'''

adjacentsX = [-1, 1, 0, 0, 1, -1, 1, -1]
adjacentsY = [0, 0, 1, -1, 1, 1, -1, -1]

def day4_part1():
    matrix = []

    try:
        with open(input_file_path, 'r') as file:
            content = file.read()
            matrix = content.split("\n")
    except FileNotFoundError:
        print(f"Error: The file '{input_file_path}' was not found.")

    # matrix = example_input.split("\n")

    total_accessible = 0

    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            if matrix[i][j] == '@':
                adj_papers = 0
                for k in range(0, 8):
                    if check_access(i+adjacentsX[k], j+adjacentsY[k], matrix):
                        adj_papers += 1
                
                if adj_papers < 4:
                    total_accessible += 1
    

    return total_accessible

def check_access(i, j, matrix):
    num_col = len(matrix[0])
    num_row = len(matrix)

    if i<0 or i>=num_row or j<0 or j>=num_col:
        return False
    
    return matrix[i][j] == '@'


def day4_part2():
    inputs = []

    try:
        with open(input_file_path, 'r') as file:
            content = file.read()
            inputs = content.split("\n")
    except FileNotFoundError:
        print(f"Error: The file '{input_file_path}' was not found.")

    # inputs = example_input.split("\n")

    matrix = []

    total_papers = 0

    for inp in inputs:
        char_list = list(inp)
        matrix.append(char_list)

    rows = len(matrix)
    cols = len(matrix[0])

    q = Queue()

    for i in range(0, rows):
        for j in range(0, cols):
            if matrix[i][j] == '@':
                adj_papers = 0
                for k in range(0, 8):
                    if check_access(i+adjacentsX[k], j+adjacentsY[k], matrix):
                        adj_papers += 1
                
                if adj_papers < 4:
                    q.put((i, j))

    while not q.empty():
        i, j = q.get()

        if matrix[i][j] == '.':
            continue

        matrix[i][j] = '.'
        total_papers += 1
        # For each neighboring paper, checking if it now has less than 4 adjacent papers
        for n in range(0, 8):
            ni, nj = i+adjacentsX[n], j+adjacentsY[n]
            if ni<0 or ni>=rows or nj<0 or nj>=cols:
                continue
            if matrix[ni][nj] == '@':
                adj_papers = 0
                for k in range(0, 8):
                    if check_access(ni+adjacentsX[k], nj+adjacentsY[k], matrix):
                        adj_papers += 1
                
                if adj_papers < 4:
                    q.put((ni, nj))

    return total_papers


if __name__ == "__main__":
    # result = day4_part1()
    result = day4_part2()
    print(result)
import os
import time
from shapely.geometry import Polygon, box

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
    inputs = []

    try:
        with open(input_file_path, 'r') as file:
            content = file.read()
            inputs = content.split("\n")
    except FileNotFoundError:
        print(f"Error: The file '{input_file_path}' was not found.")

    # inputs = example_input.split("\n")

    inputs = [[int(val) for val in values.split(',')] for values in inputs]

    poly = Polygon(inputs)
    
    max_area = 0
    
    for i in range(len(inputs)):
        for j in range(i+1, len(inputs)):
            x1, y1 = inputs[i]
            x2, y2 = inputs[j]

            if x1 == x2 or y1 == y2:
                continue

            current_area = (abs(x1 - x2)+1) * (abs(y1 - y2)+1)

            if current_area > max_area:
                min_x, max_x = min(x1, x2), max(x1, x2)
                min_y, max_y = min(y1, y2), max(y1, y2)

                rectangle = box(min_x, min_y, max_x, max_y)

                if poly.covers(rectangle):
                    max_area = current_area

    return max_area

if __name__ == "__main__":
    start_time = time.time()

    # result = day9_part1()
    result = day9_part2()
    
    end_time = time.time()
    print(f"Execution Time: {(end_time - start_time)*1000} milliseconds")
    print(result)
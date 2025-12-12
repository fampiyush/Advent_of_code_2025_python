import os
import time
import math

input_file_path = os.path.join(os.path.dirname(__file__), 'day12.txt')

example_input = '''0:
###
##.
##.

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###

4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2'''

def day12_part1(): # this solution works for the input somehow :)
    inputs = []

    try:
        with open(input_file_path, 'r') as file:
            content = file.read()
            inputs = content.split("\n\n")
    except FileNotFoundError:
        print(f"Error: The file '{input_file_path}' was not found.")

    # inputs = example_input.split("\n\n")

    shapes, regions = inputs[:-1], inputs[-1]

    regions = regions.split('\n')

    regions_fit = 0
    
    for region in regions:
        region = region.split(':')
        size = math.prod([int(num) for num in region[0].split('x')])

        shape_required = [int(num) for num in region[1].split()]

        total_shapes_size = 0

        for i,freq in enumerate(shape_required):
            num_hash = shapes[i].count('#')*freq
            total_shapes_size += num_hash

        if total_shapes_size <= size:
            regions_fit += 1
    
    return regions_fit

def day12_part2():
    pass
    

if __name__ == "__main__":
    start_time = time.time()

    result = day12_part1()
    # result = day12_part2()
    
    end_time = time.time()
    print(f"Execution Time: {(end_time - start_time)*1000} milliseconds")
    print(result)
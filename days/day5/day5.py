import os

input_file_path = os.path.join(os.path.dirname(__file__), 'day5.txt')

example_input = '''3-5
10-14
16-20
12-18

1
5
8
11
17
32'''

def day5_part1():
    inputs = []

    try:
        with open(input_file_path, 'r') as file:
            content = file.read()
            inputs = content.split("\n\n")
    except FileNotFoundError:
        print(f"Error: The file '{input_file_path}' was not found.")

    # inputs = example_input.split("\n\n")

    ranges, availables = inputs

    ranges = ranges.split("\n")
    availables = availables.split("\n")
    availables = [int(s) for s in availables]

    bounds = []

    for range in ranges:
        low, high = range.split("-")
        bounds.append([int(low), int(high)])

    bounds.sort(key=lambda bound: bound[0])
    
    bounds = merge_bounds(bounds)
    
    fresh = 0

    for available in availables:
        for bound in bounds:
            if available >= bound[0] and available <= bound[1]:
                fresh += 1
                break
    
    return fresh


def merge_bounds(bounds):
    merged_bounds = []
    merged_bounds.append(bounds[0])

    for i in range(1, len(bounds)):
        prev = merged_bounds[-1]
        if bounds[i][0] <= prev[1]:
            merged_bounds[-1][1] = max(prev[1], bounds[i][1])
        else:
            merged_bounds.append(bounds[i])

    return merged_bounds


def day5_part2():
    inputs = []

    try:
        with open(input_file_path, 'r') as file:
            content = file.read()
            inputs = content.split("\n\n")
    except FileNotFoundError:
        print(f"Error: The file '{input_file_path}' was not found.")

    # inputs = example_input.split("\n\n")

    ranges, availables = inputs

    ranges = ranges.split("\n")

    bounds = []

    for range in ranges:
        low, high = range.split("-")
        bounds.append([int(low), int(high)])

    bounds.sort(key=lambda bound: bound[0])
    
    bounds = merge_bounds(bounds)
    
    total_fresh = 0

    
    for low, high in bounds:
        total_fresh += (high-low+1)
    
    return total_fresh



if __name__ == "__main__":
    # result = day5_part1()
    result = day5_part2()
    print(result)
import os

input_file_path = os.path.join(os.path.dirname(__file__), 'day6.txt')

example_input = '''123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  '''

def day6_part1():
    rows = []

    try:
        with open(input_file_path, 'r') as file:
            content = file.read()
            rows = content.split("\n")
    except FileNotFoundError:
        print(f"Error: The file '{input_file_path}' was not found.")

    # rows = example_input.split("\n")

    rows = [row.split() for row in rows]

    ans = 0

    for colIdx in range(len(rows[0])):
        operator = rows[-1][colIdx]
        if operator == '+':
            curr = 0
        else:
            curr = 1
        
        for rowIdx in range(len(rows)-1):
            if operator == '+':
                curr += int(rows[rowIdx][colIdx])
            else:
                curr *= int(rows[rowIdx][colIdx])
        
        ans += curr

    return ans

def day6_part2():
    rows = []

    try:
        with open(input_file_path, 'r') as file:
            content = file.read()
            rows = content.split("\n")
    except FileNotFoundError:
        print(f"Error: The file '{input_file_path}' was not found.")

    # rows = example_input.split("\n")

    digits = 0
    curr = None
    operator = None
    ans = 0

    for charIdx in range(len(rows[0])):
        for i in range(len(rows)):
            value = rows[i][charIdx]
            if value == ' ':
                continue
            elif value == '+' or value == '*':
                operator = value
            else:
                digits = digits*10 + int(value)

        if digits == 0:
            ans += curr if curr is not None else 0
            curr = None
            operator = None
        else:
            if curr is None:
                curr = digits
            else:
                curr = curr+digits if operator == '+' else curr*digits
            digits = 0
    
    if curr is not None:
        ans += curr
        

    return ans

if __name__ == "__main__":
    # result = day6_part1()
    result = day6_part2()
    print(result)
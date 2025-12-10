import os
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds
import time

input_file_path = os.path.join(os.path.dirname(__file__), 'day10.txt')

example_input = '''[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}'''

class Machine:
    def __init__(self, line):
        self.pattern, self.buttons, self.joltages = self.parse(line)

    def parse(self, line):
        values = line.split()
        pattern = [v for v in values[0][1:-1]]
        joltages = [int(v) for v in values[-1][1:-1].split(',')]
        buttons = [[int(v) for v in val[1:-1].split(',')] for val in values[1:-1]]

        return pattern, buttons, joltages
    
    def __repr__(self):
        return f"pattern: {self.pattern}, buttons: {self.buttons}, joltages: {self.joltages}"

def day10_part1():
    inputs = []

    try:
        with open(input_file_path, 'r') as file:
            content = file.read()
            inputs = content.split("\n")
    except FileNotFoundError:
        print(f"Error: The file '{input_file_path}' was not found.")

    # inputs = example_input.split("\n")
    machines = []

    for inp in inputs:
        machines.append(Machine(inp))

    total_presses = 0

    for machine in machines:
        curr_press = 0
        patterns = [['.'] * len(machine.pattern)]

        new_patterns = []
        found = False
        visited = set()
        visited.add(tuple(patterns[0]))

        while not found:
            curr_press += 1
            for pattern in patterns:
                if found:
                    break
                for button in machine.buttons:
                    ptn = pattern.copy()
                    for btn in button:
                        
                        if ptn[btn] == '.':
                            ptn[btn] = '#'
                        else:
                            ptn[btn] = '.'
                    if ptn == machine.pattern:
                        total_presses += curr_press
                        found = True
                        break

                    ptn_tuple = tuple(ptn)
                    if ptn_tuple in visited:
                        continue
                    visited.add(ptn_tuple)
                    new_patterns.append(ptn)
            
            patterns = new_patterns
            new_patterns = []
        
    return total_presses

    

def day10_part2():
    inputs = []

    try:
        with open(input_file_path, 'r') as file:
            content = file.read()
            inputs = content.split("\n")
    except FileNotFoundError:
        print(f"Error: The file '{input_file_path}' was not found.")

    # inputs = example_input.split("\n")
    machines = []

    for inp in inputs:
        machines.append(Machine(inp))
    
    total_press = 0

    for machine in machines:
        total_press += lp(machine)

    return total_press
    

def lp(machine):
    n = len(machine.joltages)
    m = len(machine.buttons)

    A = np.zeros((n, m), dtype=int)
    for j, button in enumerate(machine.buttons):
        for btn in button:
            A[btn, j] = 1
    
    c = np.ones(m, dtype=float)

    lc = LinearConstraint(A, lb=machine.joltages, ub=machine.joltages)

    bounds = Bounds(lb=0, ub=np.inf)

    integrality = np.ones(m, dtype=int)

    res = milp(c=c, constraints=[lc], bounds=bounds, integrality=integrality)

    return int(round(res.fun))

if __name__ == "__main__":
    start_time = time.time()

    # result = day10_part1()
    result = day10_part2()
    
    end_time = time.time()
    print(f"Execution Time: {(end_time - start_time)*1000} milliseconds")
    print(result)
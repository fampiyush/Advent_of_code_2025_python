import os

input_file_path = os.path.join(os.path.dirname(__file__), 'day8.txt')

example_input = '''162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689'''

class DSU:
    def __init__(self, size):
        self.parents = list(range(size))

    def find(self, val):
        if self.parents[val] == val:
            return val
        
        return self.find(self.parents[val])
    
    def union(self, i, j):
        parenti = self.find(i)
        parentj = self.find(j)

        if parenti == parentj:
            return

        self.parents[parenti] = self.parents[parentj]

def day8_part1():
    inputs = []

    try:
        with open(input_file_path, 'r') as file:
            content = file.read()
            inputs = content.split("\n")
    except FileNotFoundError:
        print(f"Error: The file '{input_file_path}' was not found.")

    pairs_to_connect = 1000

    # inputs = example_input.split("\n")

    inputs = [[int(val) for val in values.split(',')] for values in inputs]

    dsu = DSU(len(inputs))

    distances = [] # [[dist, i, j]]

    for i in range(len(inputs)):
        for j in range(i+1, len(inputs)):
            dist = ((inputs[i][0]-inputs[j][0])**2 + (inputs[i][1]-inputs[j][1])**2 + (inputs[i][2]-inputs[j][2])**2) ** 0.5
            distances.append([dist, i, j])

    distances.sort(key=lambda dist: dist[0])
    
    for dist in distances[:pairs_to_connect]:
        dsu.union(dist[1], dist[2])

    frequencies = [0] * len(dsu.parents)

    for parent in dsu.parents:
        frequencies[dsu.find(parent)] += 1

    frequencies.sort(reverse=True)

    return (frequencies[0]*frequencies[1]*frequencies[2])


def day8_part2():
    pass

if __name__ == "__main__":
    result = day8_part1()
    # result = day8_part2()
    print(result)
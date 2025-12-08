import itertools
import math

def part1(file):
	with open(file, "r") as input:
		boxes = []
		for line in input:
			coords = [int(num) for num in line.split(",")]
			boxes += [coords]
		circuits = []
		combs = list(itertools.combinations(boxes,2))
		combs.sort(key = lambda x: math.dist(x[0], x[1]))
		minPairs = combs[:1000]
		for pair in minPairs:
			existingCircuits = [i for (i, circ) in enumerate(circuits) if pair[0] in circ or pair[1] in circ]
			if not existingCircuits:
				circuit = [pair[0], pair[1]]
				circuits += [circuit]
			elif len(existingCircuits) == 1:
				circuit = circuits[existingCircuits[0]]
				if pair[0] in circuit and pair[1] not in circuit:
					circuit += [pair[1]]
				elif pair[0] not in circuit and pair[1] in circuit:
					circuit += [pair[0]]
			if len(existingCircuits) == 2:
				circuit1 = circuits[existingCircuits[0]]
				circuit2 = circuits[existingCircuits[1]]
				circuit1 += circuit2
				del circuits[existingCircuits[1]]
		circuits.sort(key = len, reverse=True)
		print(len(circuits[0]) * len(circuits[1]) * len(circuits[2]))

def part2(file):
	with open(file, "r") as input:
		boxes = []
		for line in input:
			coords = [int(num) for num in line.split(",")]
			boxes += [coords]
		circuits = []
		combs = list(itertools.combinations(boxes,2))
		combs.sort(key = lambda x: math.dist(x[0], x[1]))
		for pair in combs:
			existingCircuits = [i for (i, circ) in enumerate(circuits) if pair[0] in circ or pair[1] in circ]
			if not existingCircuits:
				circuit = [pair[0], pair[1]]
				circuits += [circuit]
			elif len(existingCircuits) == 1:
				circuit = circuits[existingCircuits[0]]
				if pair[0] in circuit and pair[1] not in circuit:
					circuit += [pair[1]]
				elif pair[0] not in circuit and pair[1] in circuit:
					circuit += [pair[0]]
			if len(existingCircuits) == 2:
				circuit1 = circuits[existingCircuits[0]]
				circuit2 = circuits[existingCircuits[1]]
				circuit1 += circuit2
				del circuits[existingCircuits[1]]
			if len(circuits) == 1 and len(circuits[0]) == len(boxes):
				print(pair[0][0] * pair[1][0])
				return

if __name__ == "__main__":
	file = "inputs/day8Input.txt"
	part1(file)
	part2(file)
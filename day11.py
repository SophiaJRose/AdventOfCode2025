def part1(file):
	with open(file, "r") as input:
		tree = {}
		for line in input:
			colon = line.index(":")
			node = line[:colon]
			outputs = line.strip()[colon+2:].split(" ")
			tree[node] = outputs
		result = depth_first(tree, "you", "out", [], {})
		print(result)

def part2(file):
	with open(file, "r") as input:
		tree = {}
		for line in input:
			colon = line.index(":")
			node = line[:colon]
			outputs = line.strip()[colon+2:].split(" ")
			tree[node] = outputs
		# Attempting to find paths from dac to fft returned 0 paths, therefore all desired paths go through svr -> fft -> dac -> out in that order
		# DFS can be split into these parts (svr -> fft, fft -> dac, dac -> out), and results multiplied to get full answer
		# Use memoization table to not re-calculate amount of paths from a certain node on reaching it again from a different prior path
		svrToFft = depth_first(tree, "svr", "fft", [], {})
		fftToDac = depth_first(tree, "fft", "dac", [], {})
		dacToOut = depth_first(tree, "dac", "out", [], {})
		print(svrToFft * fftToDac * dacToOut)

# Recursive depth-first search
def depth_first(tree, current, target, visited, memo):
	visited.append(current)
	if current in memo:
		return memo[current]
	if current != target:
		if current in tree:
			numFound = 0
			for node in tree[current]:
				if node not in visited:
					found = depth_first(tree, node, target, visited.copy(), memo)
					numFound += found
			# If no paths from current to target, mark current as dead end
			memo[current] = numFound
			return numFound
		else:
			# "out" reached instead of target
			return 0
	else:
		return 1

if __name__ == "__main__":
	file = "inputs/day11Input.txt"
	part1(file)
	part2(file)
import itertools
import functools
import scipy.optimize as opt

def part1(file):
	with open(file, "r") as input:
		total = 0
		for line in input:
			firstSpace = line.index(" ")
			lastSpace = line.rindex(" ")
			lightsStr = line[:firstSpace]
			buttonsStr = line[firstSpace+1:lastSpace]
			lights = set([i for i in range(len(lightsStr)-2) if lightsStr[i+1] == '#'])
			buttons = []
			for buttonStr in buttonsStr.split(" "):
				button = set([int(num) for num in buttonStr[1:-1].split(",")])
				buttons += [button]
			if any(button == lights for button in buttons):
				total += 1
				continue
			minFound = False
			for i in range(2,len(buttons)+1):
				combs = itertools.combinations(buttons,i)
				for comb in combs:
					output = functools.reduce(lambda x, y: x.symmetric_difference(y), comb)
					if output == lights:
						total += i
						minFound = True
						break
				if minFound:
					break
		print(total)

def part2(file):
	with open(file, "r") as input:
		total = 0
		for line in input:
			firstSpace = line.index(" ")
			lastSpace = line.rindex(" ")
			buttonsStr = line[firstSpace+1:lastSpace]
			joltagesStr = line[lastSpace+1:-1]
			buttons = []
			for buttonStr in buttonsStr.split(" "):
				button = [int(num) for num in buttonStr[1:-1].split(",")]
				buttons += [button]
			joltages = [int(num) for num in joltagesStr[1:-1].split(",")]
			# Use SciPy MILP to solve
			# No single button will be pressed more times than the highest joltage required, so maxJolt gives upper bound
			maxJolt = max(joltages)
			bounds = opt.Bounds([0 for _ in range(len(buttons))], [maxJolt for _ in range(len(buttons))])
			# affectedBy is the coefficients of the constraints (which are all 1 or 0), joltages is both the lower and upper bound to achieve equality
			affectedBy = [[1 if j in buttons[i] else 0 for i in range(len(buttons)) ] for j in range(len(joltages))]
			constraints = opt.LinearConstraint(affectedBy, joltages, joltages)
			integrality = [1 for _ in range(len(buttons))]
			# c is just 1s so that c @ x gives sum of values in x
			c = [1 for _ in range(len(buttons))]
			result = opt.milp(c=c, bounds=bounds, constraints=constraints, integrality=integrality)
			# Round result in case of floating point errors
			total += int(round(result.fun))
		print(total)

if __name__ == "__main__":
	file = "inputs/day10Input.txt"
	part1(file)
	part2(file)
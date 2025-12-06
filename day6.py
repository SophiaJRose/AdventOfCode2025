import math

def part1(file):
	with open(file, "r") as input:
		lines = input.read().splitlines(keepends=True)
		segments = [''] * len(lines)
		total = 0
		for i in range(0,len(lines[0])):
			allWhitespace = True
			for j in range(0,len(lines)):
				if not lines[j][i].isspace():
					allWhitespace = False
				segments[j] = segments[j] + lines[j][i]
			if allWhitespace:
				problem = [int(seg.strip()) for seg in segments[:-1]]
				if segments[-1].strip() == "+":
					total += sum(problem)
				elif segments[-1].strip() == "*":
					total += math.prod(problem)
				segments = [''] * len(lines)
		print(total)

def part2(file):
	with open(file, "r") as input:
		lines = input.read().splitlines(keepends=True)
		problem = []
		total = 0
		nextSum = True
		for i in range(0,len(lines[0])):
			num = ""
			for j in range(0,len(lines)-1):
				num = num + lines[j][i]
			if lines[-1][i] == "+":
				nextSum = True
			elif lines[-1][i] == "*":
				nextSum = False
			if not num.isspace():
				problem += [int(num.strip())]
			else:
				if nextSum:
					total += sum(problem)
				else:
					total += math.prod(problem)
				problem = []
		print(total)

if __name__ == "__main__":
	file = "inputs/day6Input.txt"
	part1(file)
	part2(file)
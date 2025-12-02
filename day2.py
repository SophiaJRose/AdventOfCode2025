import re

def part1(file):
	repetitionPattern = re.compile(r'^(\d+)(\1)$')
	solution(file, repetitionPattern)

def part2(file):
	repetitionPattern = re.compile(r'^(\d+)(\1+)$')
	solution(file, repetitionPattern)

def solution(file, regex):
	with open(file, "r") as input:
		invalidTotal = 0
		ranges = input.read().split(",")
		for rng in ranges:
			start = int(rng.split("-")[0])
			end = int(rng.split("-")[1])
			for i in range(start, end+1):
				iStr = str(i)
				if regex.match(iStr):
					invalidTotal += i
		print(invalidTotal)

if __name__ == "__main__":
	file = "inputs/day2Input.txt"
	part1(file)
	part2(file)
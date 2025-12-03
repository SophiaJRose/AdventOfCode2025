import re

def part1(file):
	with open(file, "r") as input:
		dial = 50
		numZeroes = 0
		numPattern = re.compile(r'(\d+)')
		for line in input:
			findNum = numPattern.search(line)
			num = int(findNum.group())
			if line.startswith("L"):
				dial = (dial - num) % 100
			else:
				dial = (dial + num) % 100
			if dial == 0:
				numZeroes += 1
		print(numZeroes)

def part2(file):
	with open(file, "r") as input:
		dial = 50
		numZeroes = 0
		numPattern = re.compile(r'(\d+)')
		for line in input:
			findNum = numPattern.search(line)
			num = int(findNum.group())
			if num > 100:
				numZeroes += num // 100
				num = num % 100
			if line.startswith("L"):
				newDial = dial - num
				if newDial <= 0 and dial > 0:
					numZeroes += 1
				dial = newDial % 100
			else:
				newDial = dial + num
				if newDial >= 100 and dial < 100:
					numZeroes += 1
				dial = newDial % 100
		print(numZeroes)

if __name__ == "__main__":
	file = "inputs/day1Input.txt"
	part1(file)
	part2(file)
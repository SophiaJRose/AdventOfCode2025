import functools

def part1(file):
	solution(file, 2)

def part2(file):
	solution(file, 12)

def solution(file, length):
	with open(file, "r") as input:
		total = 0
		for line in input:
			separated = ",".join(line.strip())
			chars = separated.split(",")
			nums = [int(c) for c in chars]
			joltList = findMax(nums, length)
			jolt = functools.reduce(lambda x,y: x*10 + y, joltList)
			total += jolt
		print(total)

def findMax(list, amount):
	maxNum = max(list)
	if amount == 1:
		return [maxNum]
	maxIndex = list.index(maxNum)
	remaining = list[maxIndex+1:]
	if not remaining:
		left = findMax(list[:maxIndex], amount-1)
		return left + [maxNum]
	elif len(remaining) >= amount-1:
		right = findMax(remaining, amount-1)
		return [maxNum] + right
	else:
		diff = (amount-1) - len(remaining)
		left = findMax(list[:maxIndex], diff)
		return left + [maxNum] + remaining


if __name__ == "__main__":
	file = "inputs/day3Input.txt"
	part1(file)
	part2(file)
def part1(file):
	with open(file, "r") as input:
		parts = input.read().split("\n\n")
		ranges = parts[0].split("\n")
		ingredients = parts[1].strip().split("\n")
		fresh = []
		for rng in ranges:
			nums = [int(n) for n in rng.split("-")]
			fresh = fresh + [(nums[0],nums[1])]
		count = 0
		for ingredient in ingredients:
			ingId = int(ingredient)
			if any(rng[0] <= ingId and ingId <= rng[1] for rng in fresh):
				count += 1
		print(count)

def part2(file):
	with open(file, "r") as input:
		ranges = input.read().split("\n\n")[0].split("\n")
		fresh = []
		for rng in ranges:
			nums = [int(n) for n in rng.split("-")]
			fresh = fresh + [(nums[0],nums[1])]
		fresh.sort()
		i = fresh[0][0]
		count = 1
		for fr in fresh:
			start = fr[0]
			end = fr[1]
			# Skip i to start-1 without incrementing count
			if start > i:
				i = start-1
			# Move i to end, increment count by amount moved
			if end > i:
				count += end - i
				i = end
		print(count)

if __name__ == "__main__":
	file = "inputs/day5Input.txt"
	part1(file)
	part2(file)
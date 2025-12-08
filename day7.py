def part1(file):
	with open(file, "r") as input:
		tachyons = set()
		lines = input.read().splitlines()
		start = lines[0].find("S")
		tachyons.add(start)
		splitCount = 0
		for line in lines[1:]:
			toBeAdded = set()
			toBeRemoved = set()
			for tach in tachyons:
				if line[tach] == "^":
					splitCount += 1
					toBeAdded.add(tach-1)
					toBeAdded.add(tach+1)
					toBeRemoved.add(tach)
			tachyons = tachyons.difference(toBeRemoved)
			tachyons = tachyons.union(toBeAdded)
		print(splitCount)

def part2(file):
	with open(file, "r") as input:
		tachyons = {}
		lines = input.read().splitlines()
		start = lines[0].find("S")
		tachyons[start] = 1
		for line in lines[1:]:
			toBeUpdated = {}
			toBeRemoved = []
			for tach in tachyons.keys():
				if line[tach] == "^":
					toBeUpdated[tach-1] = toBeUpdated.get(tach-1, tachyons.get(tach-1,0)) + tachyons[tach]
					toBeUpdated[tach+1] = toBeUpdated.get(tach+1, tachyons.get(tach+1,0)) + tachyons[tach]
					toBeRemoved += [tach]
			tachyons.update(toBeUpdated)
			for tbr in toBeRemoved:
				del tachyons[tbr]
		print(sum(tachyons.values()))

if __name__ == "__main__":
	file = "inputs/day7Input.txt"
	part1(file)
	part2(file)
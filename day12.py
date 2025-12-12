def part1(file):
	with open(file, "r") as input:
		presentShapes = []
		presentVolumes = []
		sections = input.read().strip().split("\n\n")
		for present in sections[:-1]:
			volume = present.count('#')
			presentVolumes += [volume]
			shape = [",".join(line).split(",") for line in present.split("\n")[1:]]
			presentShapes += [shape]
		regions = []
		presentsRequired = []
		for line in sections[-1].split("\n"):
			colon = line.index(":")
			dimensions = [int(num) for num in line[:colon].split("x")]
			regions += [dimensions]
			presents = [int(num) for num in line[colon+2:].split(" ")]
			presentsRequired += [presents]
		# Analyzing the input reveals that for all regions, either A) the length and width are large enough that all presents will fit if placed next to each other as 3x3 squares
		# or B) the total volume of all presents is greater than the total space in the region
		# Therefore, simply count how many regions for which the former is true
		count = 0
		for i in range(len(regions)):
			totalPresents = sum(presentsRequired[i])
			squaresAvailable = (regions[i][0] // 3) * (regions[i][1] // 3)
			if squaresAvailable >= totalPresents:
				count += 1
		print(count)

if __name__ == "__main__":
	file = "inputs/day12Input.txt"
	part1(file)
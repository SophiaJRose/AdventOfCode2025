def part1(file):
	with open(file, "r") as input:
		grid = []
		for line in input:
			separated = ",".join(line.strip())
			chars = separated.split(",")
			grid = grid + [chars]
		accessible = 0
		for i in range(0,len(grid)):
			for j in range(0,len(grid[i])):
				if grid[i][j] == '.':
					continue
				adjacent = 0
				iLow = max(0,i-1)
				jLow = max(0,j-1)
				iSlice = grid[iLow:i+2]
				for row in iSlice:
					jSlice = row[jLow:j+2]
					adjacent += jSlice.count('@')
				# Take grid[i][j] out of count
				adjacent -= 1
				if adjacent < 4:
					accessible += 1
		print(accessible)

def part2(file):
	with open(file, "r") as input:
		grid = []
		for line in input:
			separated = ",".join(line.strip())
			chars = separated.split(",")
			grid = grid + [chars]
		removed = 0
		removable = -1
		while removable != 0:
			removable = 0
			for i in range(0,len(grid)):
				for j in range(0,len(grid[i])):
					if grid[i][j] == '.':
						continue
					adjacent = 0
					iLow = max(0,i-1)
					jLow = max(0,j-1)
					iSlice = grid[iLow:i+2]
					for row in iSlice:
						jSlice = row[jLow:j+2]
						adjacent += jSlice.count('@')
					# Take grid[i][j] out of count
					adjacent -= 1
					if adjacent < 4:
						removable += 1
						grid[i][j] = '.'
			removed += removable
		print(removed)

if __name__ == "__main__":
	file = "inputs/day4Input.txt"
	part1(file)
	part2(file)
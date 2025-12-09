import itertools

def part1(file):
	with open(file, "r") as input:
		tiles = []
		for line in input:
			coords = [int(num) for num in line.split(",")]
			tiles += [coords]
		combs = list(itertools.combinations(tiles,2))
		combs.sort(key = rectSize, reverse = True)
		print(rectSize(combs[0]))

def part2(file):
	with open(file, "r") as input:
		tiles = []
		for line in input:
			coords = [int(num) for num in line.split(",")]
			tiles += [coords]
		# Get full list of lines, and lists of horizontal and vertical edges
		lines = [[tiles[i], tiles[(i+1) % len(tiles)]] for i in range(len(tiles))]
		horizontalEdges = [line for line in lines if line[0][1] == line[1][1]]
		verticalEdges = [line for line in lines if line[0][0] == line[1][0]]
		# Get max i and j values for later
		iMax = max([tile[1] for tile in tiles]) + 1
		jMax = max([tile[0] for tile in tiles]) + 1
		# Get all possible rectangles between two tiles
		combs = list(itertools.combinations(tiles,2))
		combs.sort(key = rectSize, reverse = True)
		for comb in combs:
			# Get bounds of rectangle
			(iStart, iEnd) = (comb[0][1], comb[1][1]) if comb[0][1] < comb[1][1] else (comb[1][1], comb[0][1])
			(jStart, jEnd) = (comb[0][0], comb[1][0]) if comb[0][0] < comb[1][0] else (comb[1][0], comb[0][0])
			# Check that none of the edges of the shape intersect the rectangle
			intersect = False
			for [tile1, tile2] in lines:
				# Horizontal line between iStart and iEnd
				if tile1[1] == tile2[1] and tile1[1] > iStart and tile1[1] < iEnd:
					if not ((tile1[0] <= jStart and tile2[0] <= jStart) or (tile1[0] >= jEnd and tile2[0] >= jEnd)):
						intersect = True
						break
				# Vertical line between jStart and jEnd
				if tile1[0] == tile2[0] and tile1[0] > jStart and tile1[0] < jEnd:
					if not ((tile1[1] <= iStart and tile2[1] <= iStart) or (tile1[1] >= iEnd and tile2[1] >= iEnd)):
						intersect = True
						break
			if intersect:
				continue
			else:
				# No lines intersect rectangle, but rectangle could still be outside of shape
				# Find midpoint of rectangle, and draw a line in each cardinal direction to the grid edge
				# If each line intersects an odd number of edges of the shape, it is inside, if any are even, it is outside
				# Also need to account for line from midpoint intersecting two consecutive perpendicular edges by being aligned with the parallel edge between
				# e.g. if midpoint is [5,10], and the edges include lines at [3,15]-[5,15], [5,15]-[5,20], and [5,20]-[8,20]
				# line going down from midpoint intersect the first and third lines, but also aligns with second line, so count is still odd
				iMid = (iStart + iEnd) // 2
				jMid = (jStart + jEnd) // 2
				# Line going up
				upLine = [[jMid,0], [jMid,iMid]]
				upIntersections = [edge for edge in horizontalEdges if linesIntersect(upLine,edge)]
				upAligns = [edge for edge in verticalEdges if linesAlignedVert(upLine, edge)]
				upCount = len(upIntersections) + len(upAligns)
				# Line going down
				downLine = [[jMid,iMid], [jMid,iMax]]
				downIntersections = [edge for edge in horizontalEdges if linesIntersect(downLine,edge)]
				downAligns = [edge for edge in verticalEdges if linesAlignedVert(downLine, edge)]
				downCount = len(downIntersections) + len(downAligns)
				# Line going left
				leftLine = [[0,iMid], [jMid,iMid]]
				leftIntersections = [edge for edge in verticalEdges if linesIntersect(edge,leftLine)]
				leftAligns = [edge for edge in horizontalEdges if linesAlignedVert(edge, leftLine)]
				leftCount = len(leftIntersections) + len(leftAligns)
				# Line going down
				rightLine = [[jMid,iMid], [jMax,iMid]]
				rightIntersections = [edge for edge in verticalEdges if linesIntersect(edge,rightLine)]
				rightAligns = [edge for edge in horizontalEdges if linesAlignedVert(edge, rightLine)]
				rightCount = len(rightIntersections) + len(rightAligns)
				# Check all counts are odd
				if (upCount % 2 == 1) and (downCount % 2 == 1) and (leftCount % 2 == 1) and (rightCount % 2 == 1):
					print(rectSize(comb))
					return

def rectSize(tiles):
	width = abs(tiles[0][0] - tiles[1][0]) + 1
	height = abs(tiles[0][1] - tiles[1][1]) + 1
	return width * height

def linesIntersect(vertical, horizontal):
	# If i of horizontal line is between i1 and i2 of vertical, and j of vertial is between j1 and j2 of horizontal, intersect
	i = horizontal[0][1]
	(iStart, iEnd) = (vertical[0][1], vertical[1][1]) if vertical[0][1] < vertical[1][1] else (vertical[1][1], vertical[0][1])
	j = vertical[0][0]
	(jStart, jEnd) = (horizontal[0][0], horizontal[1][0]) if horizontal[0][0] < horizontal[1][0] else (horizontal[1][0], horizontal[0][0])
	return iStart <= i and i <= iEnd and jStart <= j and j <= jEnd

def linesAlignedVert(line1, line2):
	return line1[0][1] == line2[0][1]

def linesAlignedHoriz(line1, line2):
	return line1[0][0] == line2[0][0]

if __name__ == "__main__":
	file = "inputs/day9Input.txt"
	part1(file)
	part2(file)
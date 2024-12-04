# Build 2D array from input data
def build_map(input_data: str) -> list[list[str]]:

    map = []

    for line in input_data.split("\n"):
        map.append(list(line))

    return map

# Check if word in is in map given a direction and a starting point
def check_direction(map: list[list[str]], word: str, direction: tuple[int, int], start: tuple[int, int]) -> bool:

    x, y = direction
    row, col = start

    for letter in word[1:]:
        row += x
        col += y

        if row < 0 or row >= len(map) or col < 0 or col >= len(map[0]):
            return False
        
        if map[row][col] != letter:
            return False
        
    return True

# Check if there is an X shape spelling MAS in both diagnol directions
def check_xmas(map: list[list[str]], start: tuple[int, int]) -> bool:

    row, col = start
    direction = [(-1, -1), (1, -1), (-1, 1), (1, 1)]
    items = []

    for x, y in direction:
        if row + x >= 0 and row + x < len(map) and col + y >= 0 and col + y < len(map[0]):
            items.append(map[row + x][col + y])
        else:
            return False

    if (items.count("M") != 2 and items.count("S") != 2) or not (set(items) <= {"M", "S"}) or (items[1] == items[2]):
        return False
    
    return True


def part_one(map: list[list[str]], input_data: str) -> int:

    WORD = "XMAS"
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    total = 0

    for row_idx, row in enumerate(map):
        for cell_idx, cell in enumerate(row):
            if cell == WORD[0]:
                start = (row_idx, cell_idx)
                for x, y in directions:
                    if check_direction(map, WORD, (x, y), start):
                        total += 1

    return total

def part_two(map: list[list[str]], input_data: str) -> int:

    total = 0

    for row_idx, row in enumerate(map):
        for cell_idx, cell in enumerate(row):
            if cell == "A":
                start = (row_idx, cell_idx)
                if check_xmas(map, start):
                    total += 1

    return total
    

def main():
    input_file = 'input.txt'
    with open(input_file) as f:
        input_data = f.read()

    map = build_map(input_data)
    p1 = part_one(map, input_data)
    p2 = part_two(map, input_data)

    return (p1, p2)

print(main())
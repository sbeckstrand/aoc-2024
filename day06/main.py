from copy import deepcopy

DIRECTIONS = {
        "^": {"x_y": (0, -1), "right": ">"},
        ">": {"x_y": (1, 0),  "right": "v"},
        "v": {"x_y": (0, 1),  "right": "<"},
        "<": {"x_y": (-1, 0), "right": "^"}
    }

def build_grid(input: str) -> tuple[tuple[tuple[int, int], str], list[tuple[int, int]], list[list[str]]]:
    
    grid = []
    obstacles = []
    
    for y, line in enumerate(input.split("\n")):
        grid.append([])
        for x, cell in enumerate(line):
            grid[y].append(cell)
            if cell in ["<", ">", "^", "v"]:
                
                start = ((x, y), cell)
            if cell == "#":
                obstacles.append((x, y))

    return (start, obstacles, grid)

def traverse_grid(start: tuple[int, int], obstacles: list[tuple[int, int]], og_grid: list[list[str]], loopCheck: bool) -> tuple[bool, int, int]:
    grid = deepcopy(og_grid)
    visited = set()
    exited = False
    direction = start[1]
    current = start[0]
    loop_points = set()

    while not exited:
        
        next = (current[0] + DIRECTIONS[direction]["x_y"][0], current[1] + DIRECTIONS[direction]["x_y"][1])
        try:
            if (current, direction) not in visited:
                visited.add((current, direction))
            if next[0] < 0 or next[0] >= len(grid[0]) or next[1] < 0 or next[1] >= len(grid):
                exited = True
            elif grid[next[1]][next[0]] == "#":
                direction = DIRECTIONS[direction]["right"]
                if loopCheck:
                    check_next = (current[0] + DIRECTIONS[direction]["x_y"][0], current[1] + DIRECTIONS[direction]["x_y"][1])
                    if (check_next, direction) in visited:
                        return False, len(visited), len(loop_points)
            else:            
                if not loopCheck:
                    loop_grid = deepcopy(og_grid)
                    loop_grid[next[1]][next[0]] = "#"
                    loop_exited, _, _ = traverse_grid(start, obstacles, loop_grid, True)
                    if not loop_exited:
                        grid[next[1]][next[0]] = "O"
                        loop_points.add(next)
                if grid[next[1]][next[0]] != "O" and grid[current[1]][current[0]] != "O":
                    grid[current[1]][current[0]] = "X"
                    grid[next[1]][next[0]] = direction
                current = next
        except IndexError as e:
            exited = True

    return True, len(visited), len(loop_points)

def main():
    
    input_file = 'input.txt'
    with open(input_file) as f:
        input_data = f.read()
    
    start, obstacles, grid = build_grid(input_data)
    _, visited, loops = traverse_grid(start, obstacles, grid, loopCheck=False)
    p1 = visited
    p2 = loops

    return (p1, p2)

print(main())
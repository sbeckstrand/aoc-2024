from copy import deepcopy
import time

DIRECTIONS = {
        "^": {"x_y": (0, -1), "right": ">"},
        ">": {"x_y": (1, 0),  "right": "v"},
        "v": {"x_y": (0, 1),  "right": "<"},
        "<": {"x_y": (-1, 0), "right": "^"}
    }

# Build 2D grid from input
def build_grid(input: str) -> tuple[tuple[tuple[int, int], str], list[list[str]]]:
    
    grid = []
    
    for y, line in enumerate(input.split("\n")):
        grid.append([])
        for x, cell in enumerate(line):
            grid[y].append(cell)
            if cell in ["<", ">", "^", "v"]:
                start = ((x, y), cell)

    return (start, grid)


# Meat and Potatoes. This function is used to move through the grid and determine 
# how many spaces are visited before finding an exit (part 1) and how many loops
# Can be created by placing an obstacle

# This function recursively calls itself to check for loops. When checking a loop, 
# the loopCheck boolean is set to True
def traverse_grid(start: tuple[int, int], og_grid: list[list[str]], loopCheck: bool) -> tuple[bool, int, int]:
    
    grid = deepcopy(og_grid)
    visited = set()
    exited = False
    direction = start[1]
    current = start[0]
    loop_points = set()

    
    while not exited:
        
        next = (current[0] + DIRECTIONS[direction]["x_y"][0], current[1] + DIRECTIONS[direction]["x_y"][1])

        # Record visited points. If this is a loopCheck, also record the direction when visiting
        visit = (current, direction) if loopCheck else current
        if visit not in visited:
            visited.add(visit)
        
        # If reached exit, set exited to True and stop looping
        if next[0] < 0 or next[0] >= len(grid[0]) or next[1] < 0 or next[1] >= len(grid):
            exited = True
        # If hit obstacle, turn right. If loopCheck, check next space to see if its already been 
        # visited (while moving the same direction). A 'False" return suggets we did not find
        # an exit this step and that there was a loop.
        elif grid[next[1]][next[0]] == "#":
            direction = DIRECTIONS[direction]["right"]
            if loopCheck:
                check_next = (current[0] + DIRECTIONS[direction]["x_y"][0], current[1] + DIRECTIONS[direction]["x_y"][1])
                if (check_next, direction) in visited:
                    return False, len(visited), len(loop_points)
        # If no exit or obstacle, move to the next space and recusively call this same function 
        # checking for a loop if the next space is an obstacle.
        else:            
            if not loopCheck:
                loop_grid = deepcopy(og_grid)
                loop_grid[next[1]][next[0]] = "#"
                loop_exited, _, _ = traverse_grid(start, loop_grid, True)
                if not loop_exited:
                    grid[next[1]][next[0]] = "O"
                    loop_points.add(next)
            if grid[next[1]][next[0]] != "O" and grid[current[1]][current[0]] != "O":
                grid[current[1]][current[0]] = "X"
                grid[next[1]][next[0]] = direction
            current = next
    
    # If we reach thi spoint, it suggests we found an exit and we return True, as well
    # as return the number of visited spaces and the number of loop points
    return True, len(visited), len(loop_points)

def main():
    
    input_file = 'input.txt'
    with open(input_file) as f:
        input_data = f.read()
    
    start, grid = build_grid(input_data)
    _, visited, loops = traverse_grid(start, grid, loopCheck=False)
    p1 = visited
    p2 = loops

    return (p1, p2)

print(main())
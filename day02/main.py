def is_safe(diffs: list[int]) -> bool:

    if all(diff > 0 and diff <= 3 for diff in diffs) or all(diff < 0 and diff >= -3 for diff in diffs):
        return True
    
def get_diffs(levels: list[int]) -> list[int]:
    curr = levels[0]
    diffs = []
    for level in levels[1:]:
        diff = int(level) - int(curr)
        diffs.append(diff)
        curr = level
    
    return diffs

def part_one(input_data) -> int:

    safe_count = 0
    
    for line in input_data.split("\n"):
        levels = line.split(" ")
        
        diffs = get_diffs(levels)
        
        if is_safe(diffs):
            safe_count += 1

    return safe_count

def part_two(input_data) -> int:
    safe_count = 0

    for line in input_data.split("\n"):
        levels = line.split(" ")
        
        diffs = get_diffs(levels)
        if is_safe(diffs):
            safe_count += 1
            continue

        for index, _ in enumerate(levels):
            levels_copy = levels.copy()
            levels_copy.pop(index)

            diffs = get_diffs(levels_copy)
            if is_safe(diffs):
                safe_count += 1
                break
                
    return safe_count
    
def main():
    input_file = 'input.txt'
    with open(input_file) as f:
        input_data = f.read()

    p1 = part_one(input_data)
    p2 = part_two(input_data)

    return (p1, p2)

print(main())
import re

def parse_mul(sequences: list[int]) -> int:
    
    total = 0 
    
    for sequence in sequences:
        numbers = re.findall(r"\d+", sequence)
        total += int(numbers[0]) * int(numbers[1])
    
    return total

def part_one(input_data) -> int:
    
    sequences = re.findall(r"mul\(\d+,\d+\)", input_data)
    return parse_mul(sequences)

def part_two(input_data) -> int:
    
    data = input_data
    sequences = []

    state = True
    while True:
        phrase = "don't()" if state else "do()"
        split = data.split(phrase, 1)
        
        if len(split) != 2:
            if state:
                sequences += re.findall(r"mul\(\d+,\d+\)", data)
            break
        
        if state:
            sequences += re.findall(r"mul\(\d+,\d+\)", split[0])
        
        data = split[1]
        state = not state

    return parse_mul(sequences)

def main():
    input_file = 'input.txt'
    with open(input_file) as f:
        input_data = f.read()

    p1 = part_one(input_data)
    p2 = part_two(input_data)

    return (p1, p2)

print(main())
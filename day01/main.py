def part_one(input_data) -> int:
   
    l = []
    r = []
    
    for line in input_data.split("\n"):
        split = line.partition("   ")
        l.append(split[0])
        r.append(split[2])
    
    l.sort()
    r.sort()

    sum = 0
    for idx, val in enumerate(l):
        sum += abs(int(l[idx]) - int(r[idx]))
        
    return(sum)

def part_two(input_data) -> int:

    l = []
    r = []
    
    for line in input_data.split("\n"):
        split = line.partition("   ")
        l.append(split[0])
        r.append(split[2])
    
    sum = 0
    for uniq in set(l):
        sum += int(uniq) * l.count(uniq) * r.count(uniq)
        
    return(sum)

def main():
    input_file = 'input.txt'
    with open(input_file) as f:
        input_data = f.read()

    p1 = part_one(input_data)
    p2 = part_two(input_data)

    return (p1, p2)

print(main())
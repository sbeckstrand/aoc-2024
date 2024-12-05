def sort_pages(rules: list[str], update: list["str"]) -> list[str]:
    
    graph = {}
    degrees = {}
    
    for rule in rules:
        before, after = rule.split("|")
        
        for page in before, after:
            if page in update:
                if page not in graph:
                    graph[page] = []
                
                if page not in degrees:
                    degrees[page] = 0

        if before in graph and after in degrees:
            graph[before].append(after)
            degrees[after] += 1

    lowest = min(degrees.values())
    queue = [page for page in update if degrees[page] == lowest]
    ordered_pages = []

    while queue:
        page = queue.pop(0)
        ordered_pages.append(page)

        for next_page in graph[page]:
            degrees[next_page] -= 1
            if degrees[next_page] == 0:
                queue.append(next_page)

    return ordered_pages

def is_valid_update(ordered_pages: list[str], update: list[str]) -> bool:
    
    next_pages = ordered_pages.copy()
    for page in update:
        
        if page in next_pages:
            next_pages = next_pages[next_pages.index(page):]
        else:
            return False
        
    return True

def calculate_middle(update: list[str]) -> int:
    return int(update[len(update) // 2])

def main():
    
    input_file = 'input.txt'
    with open(input_file) as f:
        input_data = f.read()
    
    rules, updates = [x.split("\n") for x in input_data.split("\n\n")]
    p1 = 0
    p2 = 0
    for update in updates:
        update = update.split(",")
        sorted = sort_pages(rules, update)
        if update == sorted:
            p1 += calculate_middle(update)
        else:
            p2 += calculate_middle(sorted)

    return (p1, p2)

print(main())
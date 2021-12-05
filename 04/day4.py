puzzle_input = open('puzzle_input.txt', 'r').read().split('\n')

def parse_data(data):
    numbers = data[0]
    boards = data[1:-1]

    return numbers, boards

numbers, boards = parse_data(puzzle_input)

print(numbers)
print(boards)
# print(f"Part 1 -- {part1_answer[0] * part1_answer[1]}");
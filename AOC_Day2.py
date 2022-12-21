# A Rock B Paper C scissors
# part 1 X rock Y paper Z scissors
# part 2 X lose Y draw Z win


def parse_input(filename: str, scores: dict) -> int:
    with open(filename, "r") as f:
        lines = f.readlines()

    total = 0
    for line in lines:
        key = line.strip()
        print(key)
        value = scores.get(key, 0)
        print(value)
        total = total + value

    return total


mapping = {"A X": 3, "A Y": 4, "A Z": 8, "B X": 1, "B Y": 5, "B Z": 9, "C X": 2, "C Y": 6, "C Z": 7}

total_score = parse_input("input.txt", mapping)
print(total_score)

def get_treasures():
    count = 0
    input = open("input.txt", "r")
    treasures = input.readline()
    stones = input.readline()
    output = open("output.txt", "w+")
    treasures = treasures.strip()
    stones = stones.strip()
    if len(treasures) and len(stones):
        for stone in stones:
            if stone in treasures:
                count += 1
        output.write(str(count))
    else:
        output.write("0")


get_treasures()

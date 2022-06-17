def sum():
    input = open("input.txt", "r")
    line = input.readline()
    input.close()
    operands = line.split(" ")
    file = open("output.txt", "w+")
    file.write(str(int(operands[0]) + int(operands[1])))
    file.close()


input = open("input.txt", "w+")
input.write("25 35")
input.close()
sum()

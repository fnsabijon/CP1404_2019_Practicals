OUTFILE = "name.txt"

file = open(OUTFILE, 'w')
name = file.write(input("Enter your name: "))
file.close()

file = open(OUTFILE, 'r')
name = file.read()
print("Your name is ", name)

file = open("numbers.txt", 'r')
line_1 = file.readline()
line_2 = file.readline()
print(line_1, line_2)
file.close()

file = open("numbers.txt", 'r')
total = 0
for i in file:
    num = int(i)
    total += num
print(total)

for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 110, 10):
    print(i, end=', ')
print()

for i in range(20, 0, -1):
    print(i, end='- ')
print()

num = input("Please enter a number: ")
while num.isdigit() == False:
    num = input("Please enter a valid number: ")
for i in range(int(num), 0, -1):
    print("*", end='')
print()

num = input("Please enter a number: ")
while num.isdigit() == False:
    num = input("Please enter a valid number: ")
for i in range(1, (int(num) + 1), 1):
    print("*" * i)
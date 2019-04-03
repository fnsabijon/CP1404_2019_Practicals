numbers = []
total = 0
for i in range(5):
    numbers.append(int(input("Enter a number: ")))
    total += numbers[-1]
average = total/5

print("The first number is {}\nThe last number is {}".format(numbers[0], numbers[-1]))
print("The smallest number is {}\nThe biggest number is {}".format(min(numbers), max(numbers)))
print("The total of the numbers is {}\nThe average of the numbers is {}".format(total, average))

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username = input("Please enter your username: ")
if username in usernames:
    print("Access granted")
else:
    print("Access denied")
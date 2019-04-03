
CODE_MAX = 127
CODE_MIN = 33
char = input("Enter a character: ")
code = ord(char)
print("The ASCII code for {:<} is {:>}".format(char, code))

code = 0
while code < CODE_MIN or code > CODE_MAX:
    try:
        code = int(input("Enter a number between 33 and 127: "))
    except ValueError:
        pass
char = chr(code)
print("The character for {:<} is {:>}".format(code, char))

for i in range(CODE_MIN, CODE_MAX + 1):
    print("{:<} {:>3}".format(i, chr(i)))
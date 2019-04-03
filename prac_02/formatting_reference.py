"""
CP1404/CP5632 - Practical
Various examples of using Python string formatting with the str.format() method
Want to read more about it? https://docs.python.org/3/library/string.html#formatstrings
"""

name = "Gibson L-5 CES"
year = 1922
cost = 16035.40

# The ‘old’ manual way to format text with string concatenation:
print("My guitar: " + name + ", first made in " + str(year))

# A better way - using str.format():
print("My guitar: {}, first made in {}".format(name, year))
print("My guitar: {0}, first made in {1}".format(name, year))
print("My {0} was first made in {1} (that's right, {1}!)".format(name, year))

# Formatting currency (grouping with comma, 2 decimal places):
print("My {} would cost ${:,.2f}".format(name, cost))

# Aligning columns:
numbers = [1, 19, 123, 456, -25]
for i in range(len(numbers)):
    print("Number {0} is {1:>5}".format(i + 1, numbers[i]))

# Another (nicer) version of the above loop using the enumerate function
for i, number in enumerate(numbers):
    print("Number {0} is {1:>5}".format(i + 1, number))

# TODO: Using a for loop with the range function and string formatting,
# produce the following output:
#   0
#  50
# 100

for i in range(0,101,50):
    print("{:3}".format(i))

"""
Tips for string formatting with the format specifier {}

The number before the colon, or if there's no colon like {0}, specifies which parameter to use. This can be left out to use the default order.

The part after the colon specifies the formatting. E.g. {:3} specifies to use 3 spaces (or more if needed) for the value when it's used.

By default, numbers are right-aligned and strings are left-aligned. You can change this with > or <
So, {:>6} would format the value to be right-aligned and take up 6 (or more if needed) spaces.
"""
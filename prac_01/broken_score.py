"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!

score = float(input("Enter score: "))
if score < 0 or score > 100:
    print("Invalid score")
elif score < 50:
    print("Bad")
else:
    if score >= 50 and score < 90:
        print("Passable")
    if score >= 90:
        print("Excellent")
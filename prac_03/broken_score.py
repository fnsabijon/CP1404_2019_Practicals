def main():

score = float(input("Enter score: "))






def get_result(score):
if score < 0 or score > 100:
    result = "Invalid score"
elif score < 50:
    result = "Bad"
else:
    if score >= 50 and score < 90:
        result = "Passable"
    if score >= 90:
        result = "Excellent"
return result
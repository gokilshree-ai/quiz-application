score = 0

print("Python Quiz")

answer = input("What keyword is used to define a function? ")
if answer.lower() == "def":
    score += 1

answer = input("Which symbol is used for comments? ")
if answer == "#":
    score += 1

print("Your Score:", score)

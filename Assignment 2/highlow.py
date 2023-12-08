import random
n=random.randint(1,100)

guess=0

while guess <= 10:

    s=int(input("choose a random integer between 1 and 100: "))
    if s < n:
        print("Clue:Higher")
    elif s > n:
        print("Clue:Lower")
    elif s == n:
        print("  Correct answer.Excellent!  ")
        print("")
        break
    guess +=1

print()
print("            Nice try!  ")
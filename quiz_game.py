print("Welcome to my computer quiz!")

playing= input('Do you want to play this game?')

if playing.lower() != 'yes':
    quit()

print("Alright, Let's play :)")
score = 0

answer = input("Who is the father of Computer Science? ")
if answer.lower() == "charles babbage":
    print("Correct!")
    score += 5
else:
    print("Incorrect!")

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 5
else:
    print("Incorrect!")

answer = input("How many parts are there in CPU? ")
if answer == str(2):
    print("Correct!")
    score += 5
else:
    print("Incorrect!")

answer = input("Where are the CPU and memory located? ")
if answer == 'motherboard':
    print("Correct!")
    score += 5
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 5
else:
    print("Incorrect!")

answer = input("What does URL stand for? ")
if answer.lower() == "uniform resource locator":
    print("Correct!")
    score += 5
else:
    print("Incorrect!")

answer = input("What does ROM stand for? ")
if answer.lower() == "read only memory":
    print("Correct!")
    score += 5
else:
    print("Incorrect!")

answer = input("What does USB stand for? ")
if answer.lower() == "universal serial bus":
    print("Correct!")
    score += 5
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 8) * 100) + "%.")
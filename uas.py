print("Welcome to my computer quiz!")

playing = input("Do you want to play? yes/no :")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

question = input("What does CPU stand for? ")
if question.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

question = input("What does GPU stand for? ")
if question.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

question = input("What does RAM stand for? ")
if question.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

question = input("What does PSU stand for? ")
if question.lower() == "power supply unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")

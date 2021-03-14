# Write a knowledge competition program.
# It should consist of 10 questions in total.
# Each question will have only answer.
# Adjust the answers of the questions according to case sensitivity.
# Each question should be worth 10 points.
# If user answers 5 or fewer questions it will be considered unsuccessful.
# If the user more than 5 questions correctly, it will be considered successful.

# Create a dictionary to store the questions and the answers.

questionDict = {"Which animal is known as the Ship of the Desert?": "Camel",
                "In which direction does the sun rise?": "East",
                "What do you call a type of shape that has three sides?": "Triangle",
                "Which organ do we use to smell things?": "Nose",
                "Which way is anti-clockwise, left or right?": "Left",
                "What do you call a house made of ice?": "Igloo",
                "Which is the tallest mountain in the world?": "Mount Everest",
                "Which planet is known as the Red Planet?": "Mars",
                "Which is the tallest animal on the earth?": "Giraffe",
                "What is the first month of the year?": "January"}

# Create variables to hold the necessary data.

points = 0
questioncounter = 1

# Welcome statement for the user;

print("Welcome to the knowledge competition program!\n\n")
print("In this competition you have 10 questions to answer.\nEvery question is worth 10 points.")
print("You need to get at least 50 points to win.\n\nGood luck!\n\n")

# Iterate through the dictionary and ask the questions to the user.
# I used the casefold() method on both strings to make a non-case-sensitive comparison

for questions, answers in questionDict.items():
    print("Question " + str(questioncounter))
    userAnswer = str(input(questions + "\n"))
    if userAnswer.casefold() == answers.casefold():
        print("\nYour answer is correct!\n")
        points += 10
    else:
        print("\nYour answer is incorrect :(\n")
    questioncounter += 1

# Evaluate the points and give the user an output

if points >= 50:
    print("You WON by earning " + str(points) + " points! Congratulations!")
else:
    print("You LOST by earning " + str(points) + " points.")

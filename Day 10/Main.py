#KBC GAME

# Initialize the total score to zero.
total = 0

# Define the first question, its correct answer, and the associated points.
Q1 = ['In which Continent Pakistan is Located: ', 'Asia', 1000]

# Define the second question, its correct answer, and the associated points.
Q2 = ['Name of founder of Pakistan: ', 'Quid-e-azam', 1000]

# Define the possible answers for the first question.
answer1 = ['a) Asia     b) Africa  \n c) Europe    d) America']

# Define the possible answers for the second question.
answer2 = ['a) Fatima Jinnah     b) Quid-e-azam  \n c) Alama Iqbal    d) John Ciena']

# Create a list 'Questions' containing the question-answer points tuples.
Questions = [Q1, Q2]

# Create a list 'Answers' containing the possible answers for each question.
Answers = [answer1, answer2]

# Iterate over each question in the 'Questions' list.
for question in Questions:
    # Display the current question and possible answers to the user, and take their input.
    answer = input(question[0]).capitalize()

    # Check if the user's answer matches the correct answer (ignoring case).
    if answer == question[1].capitalize():
        # If the answer is correct, add the points associated with the question to the total score.
        total += question[2]
    else:
        # If the answer is incorrect, break out of the loop, ending the game.
        break

# Print the total score achieved by the user.
print("You Won", total)

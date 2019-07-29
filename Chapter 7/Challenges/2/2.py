# Trivia Challenge
# Trivia game that reads a plain text file

import sys, pickle

def open_file(file_name, mode):
    """Open a file."""
    try:
        the_file = open(file_name, mode)
    except IOError as e:
        print("Unable to open the file", file_name, "Ending program.\n", e)
        input("\n\nPress the enter key to exit.")
        sys.exit()
    else:
        return the_file

def next_line(the_file):
    """Return next line from the trivia file, formatted."""
    line = the_file.readline()
    line = line.replace("/", "\n")
    return line

def next_block(the_file):
    """Return the next block of data from the trivia file."""
    category = next_line(the_file)
    
    question = next_line(the_file)
    question_val = next_line(the_file)
    if question_val != "":
        question_val = int(question_val)
    
    answers = []
    for i in range(4):
        answers.append(next_line(the_file))
        
    correct = next_line(the_file)
    if correct:
        correct = correct[0]
        
    explanation = next_line(the_file) 

    return category, question, question_val, answers, correct, explanation

def welcome(title):
    """Welcome the player and get his/her name."""
    print("\t\tWelcome to Trivia Challenge!\n")
    print("\t\t", title, "\n")
 
def main():
    trivia_file = open_file("trivia.txt", "r")
    title = next_line(trivia_file)
    welcome(title)
    score = 0

    # get first block
    category, question, question_val, answers, correct, explanation = next_block(trivia_file)
    while category:
        # ask a question
        print(category)
        print(question)
        for i in range(4):
            print("\t", i + 1, "-", answers[i])

        # get answer
        answer = input("What's your answer?: ")

        # check answer
        if answer == correct:
            print("\nRight!", end=" ")
            score += question_val
        else:
            print("\nWrong.", end=" ")
        print(explanation)
        print("Score:", score, "\n\n")

        # get next block
        category, question, question_val, answers, correct, explanation = next_block(trivia_file)

    trivia_file.close()

    print("That was the last question!")
    print("You're final score is", score)

    name = input("What is your name? ")
    hs = (name, score)
    high_scores = open("high_scores.dat", "ab")
    pickle.dump(hs, high_scores)
    high_scores.close()

    see_hs = input("To see all high scores. press s: ")
    if see_hs == "s":
        high_scores = open("high_scores.dat", "rb")
        hs = []
        h = pickle.load(high_scores)
        while True:
            hs.append(h)
            try:
                h = pickle.load(high_scores)
            except:
                break
        hs.sort(key=lambda x: x[1])
        hs.reverse()
        for n, s in hs:
            print(n, s)
        high_scores.close()

main()  
input("\n\nPress the enter key to exit.")

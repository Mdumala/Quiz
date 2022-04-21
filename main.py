def new_game():

    guesses = []
    corrent_quesses = 0
    question_num = 1

    for key in questions:
        print("--------------")
        print(key)
        for i in options[question_num-1]:
            print(i)

        guess = input("Enter (A,B,C OR D): ")
        guess = guess.upper()
        guesses.append(guess)

        corrent_quesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(corrent_quesses, guesses)

def check_answer(answer, guess):

    if answer == guess:
        print("CORRECT")
        return 1
    else:
        print("WRONG")
        return 0

def display_score(correct_guesses, quesses):

    print("results")
    print("answers: ", end=" ")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("guesses: ", end=" ")
    for i in quesses:
        print(i, end=" ")
    print()

    score = (correct_guesses/len(quesses))*100
    print("Your score is: "+str(score)+"%")

def play_again():

    response = input("Do you want to play again?: (yes/no)")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False


#Dictionary
questions = {
    "Who created Pyton?: ": "A",
    "What yoear was Pythoc created?: ": "B",
    "Python is tibuted to which comedy group?: ": "C",
    "Is Earth round?: ": "A"
}

#2D list
options = [["A. Guido van Rosuum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
           ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
           ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
           ["A. True", "B. False", "C. sometimes", "D. What's Earth?"]]

new_game()

while play_again():
    new_game()
print("Cya")

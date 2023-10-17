# This fonction will ask 3 questions and you have only 3 lives to get the correct answer

def the_question(question, right_answer, lives):
    number_of_lives = lives

    while number_of_lives > 0:
        user_response = input(question).lower()
        if user_response == right_answer.lower():
            print("You got it!")
            return True
        else:
            number_of_lives -= 1
            if number_of_lives > 0:
                print(f"Ops that's not it... You still have {number_of_lives} chances left")
            else:
                print("Oh boy oh boy ! Not your  lucky day, try again later")
    return False

print("I've got a fun quizz for you!")

if (the_question("How many times France won the Soccer World Cup? ", "2", 3) and
    the_question("When was Apple founded? ", "1976", 3) and
    the_question("Who founded SpaceX? ", "elon musk", 3)):

        print("You luck guy! You won! ")
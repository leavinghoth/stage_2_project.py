#stage 2 project

blanks = ["__1__", "__2__", "__3__"]


easy_questions = '''What was Princeess Leia's last name ___1___?  Who said this quote: "I find your lack of faith disturbing.___2___".
Who said the following quote: "Mos Eisley Spaceport, you will never find a more wretched hive of scum and villainy."___3___'''

easy_answers = ["Organa", "Darth Vader", "Obi-Wan Kenobi"]



medium_questions = '''Who's DNA was used in the creation of the Clone Army ___1___?  What was Anakin Skywalker's mom's name ___2___?
Who said this: "Good against remotes is one thing. Good against the living, that's something else" ___3___? '''

medium_answers = ["Jango Fett", "Shmi", "Han Solo"]



hard_questions = ''' What's Chewbacca's home planet ___1___?  Who was the first Jedi to learn how to return from death as a ghost ___2___?
Where did Darth Vader reveal himself to be Luke's father ___3___?'''

hard_answers = ["Kashyyyk", "Qui-Gon Jinn", "Cloud City"]






print ("Welcome to my Star War's Fill in the Blanks Quiz.")
user_input = input("Please choose a difficulty level: easy, medium or hard.")


#Chooses the difficulty level
def level(user_input):
    if user_input.lower() == "easy":
        print("You've chosen easy.")
        return easy_questions
    elif user_input.lower() == "medium":
        print("You've chosen medium.")
        return medium_questions
    elif user_input.lower() == "hard":
        print("You've chosen hard.")
        return hard_questions
print(level(user_input))


def answer(user_input):
    if level(user_input).lower() == "easy":
        return easy_answers
    elif level(user_input).lower()=="medium":
        return medium_answers
    elif level(user_input).lower()=="hard":
        return hard_answers


def check_answer(user_response, answers, answer_index):
    if user_response == answers[answer_index]:
        return "Correct"
    return "Incorrect"

#Runs the game
def ask_question():
    question = level(user_input)
    correct = 0
    incorrect = 0
    if question == easy_questions:
        answers = easy_answers
    elif question == medium_questions:
        answers = medium_answers
    elif question == hard_questions:
        answers = hard_answers
    else:
        return "You did not choose a correct answer. Goodbye"
        
    blanks_index = 0
    answer_index = 0
    while blanks_index < len(blanks):
        while answer_index < len(answers):
            user_response = input("What is the answer for" + blanks[blanks_index] +"?")
            if check_answer(user_response, answers, answer_index) == "Correct":
                print("Correct!")
                question = question.replace(blanks[blanks_index], user_response)
                print(question)
                blanks_index += 1
                answer_index += 1
                correct += 1
            else:
                print("Incorrect")
                blanks_index += 1
                answer_index += 1
                incorrect += 1
        if correct == 3:
            return "Congratulations! You got the questions ALL right!  You sure know your Star Wars trivia!"
        else:
            return "You got" + " " + str(correct) + " " + "right and" + " " + str(incorrect) + " " + "wrong. The correct answers are" + " " + str(answers)
                  



print(ask_question())

#Building a Python Trivia Game

#step 2 we gotta import random
import random

#step 1 is to store the Q & A
questions_answers =  {
    "What is the boundary between living and dead called?": "veil",
    "A trapped spirit unable to move on is called?": "ghost",
    "A spirit that causes physical disturbances is?": "poltergeist",
    "How many cards are in a full tarot deck?": "78",
    "The suit associated with emotions is?": "cups",
    "A reversed tarot card reading is called?": "reversal",
    "A shapeshifting trickster spirit is called?": "trickster",
    "What creature feeds on life energy?": "vampire",
    "A demon that causes sleep paralysis is?": "incubus",
    "A spirit summoned to do a witch's bidding is?": "familiar",
    "What tool is used to detect spirits electronically?": "emf",
    "The Hindu god of death and the spirit world?": "yama",
    "What algorithm splits data into a tree of decisions?": "decision tree",
    "What technique combines multiple trees for better accuracy?": "random forest",
    "What algorithm finds the best line to separate two classes?": "svm",
    "What is the simplest classification algorithm based on neighbors?": "knn"
}

#random sample cannot directly access dictionary so we should convert it into list
def trivia_game():
    questions_list = list(questions_answers.keys())

    #We need to look into the list, randomly pic 5 Q
    no_of_questions = 5
    total_score = 0
    questions_selected = random.sample(questions_list, no_of_questions)

    #now we should display Q to the user
    for index,questions in enumerate(questions_selected):
        print(f"{index+1}.{questions}")
    # whatever user types will be in lower case & strip removes unecessary spaces so answer won't be incorrect like user entering 8 instead of space then 8

        user_answer = input("Enter your answer: ").lower().strip()

    #checking if user entered answer is correct
        correct_answer = questions_answers[questions]
        if user_answer == correct_answer:
            print("correct answer <3")
            total_score += 1
        else:
            print(f"WRONG, the correct answer is {correct_answer}")

    print(f"your battle is over!, your score is {total_score}/{no_of_questions}")

trivia_game()


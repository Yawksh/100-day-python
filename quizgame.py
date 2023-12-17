def new_game():
 guesses=[]
 correct_guesses=0
 question_num=1
 for key in question:
     print("--------------")
     print(key)
     for i in options[question_num-1]:
       print(i)
       guess=input("Enter (A,B C OR D)")
       guesses.append(guess)
       question_num+=1



def check_answer():
    pass


def display_score():
    pass


def play_again():
    pass


question = {
    "who created python?: ": "A",
    "what year was python created?: ": "B",
    "python is tributed to which comedy group?:": "C",
    "Is the earth round?: ": "A"
}
options = [["A,Giuo van rossum", "B Elon music", "C, bill Gates", "D,mak zucker"],
           ["A,1989", "B 1991", "C,2000", "D,2016"],
           ["A. Lonely Island ", "B, Smosh", "C. Monty python", "D,SNKL"]
           # ["A, True", "B,False", "C,sometimses", "D,what is Earth?"]
           ]


new_game()
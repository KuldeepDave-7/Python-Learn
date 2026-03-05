def start():
    index = 0
    guess = 0
    print("---------------------")  
    for i in questions:
        print(i)
        for x in choices[index]:
            print(x)
        choice = input("Enter Your Choice: ").upper()
        print("---------------------")    
        index = index + 1
        check = Verify(questions.get(i),choice)
        if check == True:
            guess = guess + 1

    result(guess)

def Verify(answer, choice):
    if answer == choice:
        return True
    else:
        return False
    
def result(guess):
    print("Your Guess "+str(guess)+" Out of "+str(len(questions)))
    print("Result = "+str(int(guess/len(questions)*100))+"%")

questions = {'Who is the Ceo of Google :' : 'A',
             'Who created Python :' : 'D',
             'Who is Kuldeep :' : 'D'}

choices = [["A: Sundar Pichai", "B: Elon Musk", "C: Jhon Cena", "D: Mark Zukerberg"],
           ["A: Kuldeep", "B: Ronaldo", "C: Messi", "D: Guido Van"],
           ["A: Feminist", "B: Non Chalant", "C: Tall", "D: All of the above"]]

while True:
    val = input("Do You Want to play the Game: (Yes/No)").lower()
    if val == "no":
        break
    else:
        start()
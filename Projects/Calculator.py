from tkinter import *

def button_press(num):
    global equation_text
    global count
    global check 
    check = num

    if count == 1 and check != "+" and check != "-" and check != "/":
        equation_text = ""
        count = 0
    else:
        count = 0
        
    equation_text = equation_text + str(num)
    answer.set(equation_text)

def equals():
    global count
    global equation_text
     
    ans = str(eval(equation_text))
    equation_text = ans
    answer.set(equation_text)
    count = 1

def clear():
    global equation_text

    equation_text = ""
    answer.set(equation_text)    

def delete():
    global equation_text

    equation_text = equation_text[:-1]
    answer.set(equation_text)

window = Tk()
window.geometry("280x350")
window.config(bg="#2C2C2C")

equation_text = ""
check = ""
count = 0
answer = StringVar()

screen = Label(window,textvariable=answer,bg="white",fg="Black",font=("consolas",20,"bold"),width=26,height=2)
screen.pack()

frame = Frame(window)
frame.pack()

button1 = Button(frame,text="1",width=5,height=2,command=lambda: button_press(1),font=35)
button1.grid(row=0,column=0)

button2 = Button(frame,text="2",width=5,height=2,command=lambda: button_press(2),font=35)
button2.grid(row=0,column=1)

button3 = Button(frame,text="3",width=5,height=2,command=lambda: button_press(3),font=35)
button3.grid(row=0,column=2)

button4 = Button(frame,text="4",width=5,height=2,command=lambda: button_press(4),font=35)
button4.grid(row=1,column=0)

button5 = Button(frame,text="5",width=5,height=2,command=lambda: button_press(5),font=35)
button5.grid(row=1,column=1)

button6 = Button(frame,text="6",width=5,height=2,command=lambda: button_press(6),font=35)
button6.grid(row=1,column=2)

button7 = Button(frame,text="7",width=5,height=2,command=lambda: button_press(7),font=35)
button7.grid(row=2,column=0)

button8 = Button(frame,text="8",width=5,height=2,command=lambda: button_press(8),font=35)
button8.grid(row=2,column=1)

button9 = Button(frame,text="9",width=5,height=2,command=lambda: button_press(9),font=35)
button9.grid(row=2,column=2)

button_add = Button(frame,text="+",width=5,height=2,command=lambda: button_press("+"),font=35)
button_add.grid(row=0,column=3)

button_sub = Button(frame,text="-",width=5,height=2,command=lambda: button_press("-"),font=35)
button_sub.grid(row=1,column=3)

button_div = Button(frame,text="/",width=5,height=2,command=lambda: button_press("/"),font=35)
button_div.grid(row=2,column=3)

button_equal = Button(frame,text="=",width=5,height=2,command=lambda: equals(),font=35)
button_equal.grid(row=3,column=0)

button_clear = Button(frame,text="AC",width=5,height=2,command=lambda: clear(),font=35)
button_clear.grid(row=3,column=1)

button_del = Button(frame,text="Del",width=5,height=2,command=lambda: delete(),font=35)
button_del.grid(row=3,column=2)

answer.set("HELLO")
window.mainloop()
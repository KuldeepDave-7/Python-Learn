from tkinter import *
from tkinter import filedialog

# r :- r & rt is for read text
# open :- to open a file and return a file object. file object can be used to perfrom operation on file
# askopenfile :- returns a file object, so you can read it directly — no need to open() again.
# askopenfilename :- This returns only the file path (string).
# file type :- It is used to limit opening files if you choose text file only plain text file will appear

def openfile():
    filename = filedialog.askopenfile(title="Open NIGGA ")
    #file = open(filename,'r')
    print(filename.read())
    filename.close()
    
window = Tk()

button = Button(window,text="Open",command=openfile)
button.pack()

window.mainloop()
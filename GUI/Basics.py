# Window :- window serves as the primary container for a GUI application providing the visual space where all other interactive elements reside
# Widget :- Widgets are the individual, interactive elements that make up the content of a window.They are the building blocks of a GUI,

from tkinter import *

window = Tk()                           # Instantiate an instance of window
window.geometry("520x520")              # Used to control the size and position of a window or widget.
window.title("Kuldeep Dave")            # Used in changing the title of the window

icon = PhotoImage(file='GUI/download.png')     # Photo image Constructor 
window.iconphoto(True,icon)                    # Sets icon for window
window.config(background="sky blue")

window.mainloop()                     # Place window on computer screen and keeps the window open
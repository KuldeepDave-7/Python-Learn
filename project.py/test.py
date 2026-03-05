from tkinter import *
from tkinter import colorchooser, filedialog, font

def change_color():
    color = colorchooser.askcolor()
    text_area.config(fg=color[1])

def change_font(*args):
    text_area.config(font=(font_name.get(),font_size.get()))    

window = Tk()

window_width = 500
window_height = 500

# Get screen size
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Calculate position x, y to center the window
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

# Set the geometry: "<width>x<height>+<x>+<y>" Placing the top-left corner so that the window is aligned to the center
window.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))

font_name = StringVar(window)
font_name.set("arial")

font_size = StringVar(window)
font_size.set("30")

text_area = Text(window, font=(font_name.get(),font_size.get()))

scroll_bar = Scrollbar(text_area)

# Helps in text wraping and when the window is resized the text fill up the extra space
window.grid_rowconfigure(0,weight=1)
window.grid_columnconfigure(0,weight=1)

# the widget sticks to all sides of its cell.
text_area.grid(sticky=N + E + S + W)

frame = Frame(window)
frame.grid()

color_button = Button(frame,text="Color",command=change_color)
color_button.grid(row=0,column=0)

font_box = OptionMenu(frame,font_name,*font.families(),command=change_font)
font_box.grid(row=0 , column=1)

fontSize = Spinbox(frame, from_=1, to=50, textvariable=font_size,command=change_font)
fontSize.grid(row=0,column=2)

scroll_bar.pack(side=RIGHT,fill=Y)
text_area.config(yscrollcommand=scroll_bar.set)
window.mainloop()

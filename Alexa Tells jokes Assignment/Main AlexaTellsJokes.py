import random
from tkinter import *
main = Tk()
main.geometry("500x250")
f = open(r"randomJokes.txt", "r")
main.title("Alexa Tells Jokes")
jokes=f.readlines()

random_joke=random.choice(jokes)
joke_Split=random_joke.split("?")
joke_Setup = joke_Split[0]+"?"
joke_Punchline = joke_Split[1]

def joke_Manager():
    global random_joke, joke_Split, joke_Setup, joke_Punchline
    if not joke_Setup_Text.get():
        joke_Setup_Text.set(joke_Setup)
    elif not joke_Punchline_Text.get():
        joke_Punchline_Text.set(joke_Punchline)
    else:
        joke_Setup_Text.set("")
        joke_Punchline_Text.set("")
        random_joke=random.choice(jokes)
        joke_Split=random_joke.split("?")
        joke_Setup = joke_Split[0]+"?"
        joke_Punchline = joke_Split[1]


# ----------- Frame Work -----------

frame_img = PhotoImage(file="UI assets\Frame.png")
frame_display = Label(main, text="", image=frame_img)
frame_display.pack()

title = Label(main, text="Alexa tells jokes", font=("inter", 20),pady=20)

joke_Setup_Text = StringVar()
joke_Setup_Display = Label(main, textvariable=joke_Setup_Text, font=("inter", 13), wraplength=480)

joke_Punchline_Text = StringVar()
joke_Punchline_Display = Label(main, textvariable=joke_Punchline_Text, font=("inter", 13), wraplength=480)

tell_Joke_Button = Button(main, text="Tell me", font=("inter", 20), command=joke_Manager)

quit_Button = Button(main, text="Quit", font=("inter", 20), command=main.destroy)

#  ----------- Display -----------
title.place(x=150, y=30, width=200, height=24)
joke_Setup_Display.place(x=12, y=80, width=477, height=18)
joke_Punchline_Display.place(x=12, y=120, width=477, height=36)
tell_Joke_Button.place(x=50, y=178, width=150, height=30)
quit_Button.place(x=300, y=178, width=150, height=30)

mainloop()
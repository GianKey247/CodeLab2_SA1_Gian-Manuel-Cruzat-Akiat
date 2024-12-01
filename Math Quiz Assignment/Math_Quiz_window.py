from tkinter import *
from tkinter import messagebox
from random import randint
import random

main = Tk()
main.geometry("750x400")

digit = 1
question_List = []
points = 0
question_index = 0
attempt = 1

def randomInt(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

def decideOperation ():
    operator = ["-", "+"]
    return random.choice(operator)

def generate_questioninator():
    index = 0
    while index < 10:
        num1 = randomInt(digit)
        num2 = randomInt(digit)
        chosen_Operator = decideOperation()
        if chosen_Operator == "+":
            answer = num1 + num2
        else : 
            answer = num1 - num2   
        question = f"{num1} {chosen_Operator} {num2} = "
        question_List.append({
            "Question": question,
            "Answer": answer
        })
        index += 1

def displayProblem():
    question = f"Question {question_index+1} : {question_List[question_index]['Question']}"
    question_Text.set(question)

def get_answer():
    return question_List[question_index]['Answer']

def isCorrect(user_Ans):
    try :
        user_Ans=int(user_Ans)
    except ValueError:
        messagebox.showerror("Wrong Input","Your input is a string, please try again")
        return
    global points, question_index, attempt
    if user_Ans != get_answer():
        isCorrect_Display_Text.set("Incorrect")
        attempt += 1
    else:
        isCorrect_Display_Text.set("Correct")
        question_index +=1
        user_Input.delete(0, 'end')
        if attempt == 1:
            points += 10
        elif attempt == 2:
            points += 5
        points_text.set(points)
        if question_index > len(question_List)-1:
            displayResults()
            frame_Manager(page_2_frame, page_3_frame)
        else:
            attempt=1
            displayProblem()

def displayResults():
    if points >= 90:
        grade = "A+"
    elif points < 90 and points>= 80:
        grade = "A"
    elif points < 80 and points>= 70:
        grade = "B"
    elif points < 70 and points>= 60:
        grade = "C"
    elif points < 60 and points>= 50:
        grade = "D"
    elif points < 50 :
        grade = "E"
    
    score_Display_Text.set(f"You Scored {points} : {grade} Grade")

def reset():
    global points, question_List, question_index, attempt
    question_List = []
    points = 0
    points_text.set(0)
    question_index = 0
    attempt = 1
    isCorrect_Display_Text.set("")

def frame_Manager(frame_To_Forget: Frame, frame_To_Display: Frame):
    frame_To_Forget.place_forget()
    frame_To_Display.place(x=0,y=0, width=750, height=400)
    frame_To_Display.tkraise()
    
def set_digit(num_digit):
    global digit
    digit=num_digit
    frame_Manager(page_1_frame, page_2_frame) 
    generate_questioninator()
    displayProblem()

def display_points(points):
    points_text.set(points)

# ----------- Page 1 Frame Work----------- 
page_1_frame = Frame(main)
title = Label(page_1_frame, text="MATH QUIZ", font=("TkDefaultFont", 30),pady=20)
menu_frame_img = PhotoImage(file="UI assets\Menu frame.png")
menu_frame_display = Label(page_1_frame, text="", image=menu_frame_img)
menu_frame_display.pack()
menu_Display = Label(page_1_frame, text="""Select Difficulty""",font=("TkDefaultFont", 24))

# Difficulty level buttons
easy_Button = Button(page_1_frame, text="Easy", font=("TkDefaultFont", 20),command=lambda:set_digit(1))
medium_Button = Button(page_1_frame, text="Moderate", font=("TkDefaultFont", 20),command=lambda:set_digit(2))
hard_Button = Button(page_1_frame, text="Advanced", font=("TkDefaultFont", 20),command=lambda:set_digit(4))

one_Digit_Label = Label(page_1_frame, text="1 Digit", font=("TkDefaultFont", 20))
two_Digit_Label = Label(page_1_frame, text="2 Digits", font=("TkDefaultFont", 20))
four_Digit_Label = Label(page_1_frame, text="4 Digits", font=("TkDefaultFont", 20))

# ---- Display Frame 1 ---- 

title.place(x=175, y=30, width=400, height=50)
menu_Display.place(x=175, y=95, width=400, height=40)
easy_Button.place(x=75, y=170, width=200, height=40)
medium_Button.place(x=275, y=170, width=200, height=40)
hard_Button.place(x=475, y=170, width=200, height=40)
one_Digit_Label.place(x=75, y=225, width=200, height=40)
two_Digit_Label.place(x=275, y=225, width=200, height=40)
four_Digit_Label.place(x=475, y=225, width=200, height=40)
page_1_frame.place(x=0,y=0, width=750, height=400)


# ----------- Page 2 Frame Work----------- 
page_2_frame = Frame(main)

quiz_frame_img = PhotoImage(file="UI assets\Quiz frame.png")
quiz_frame_display = Label(page_2_frame, text="", image=quiz_frame_img)
quiz_frame_display.pack()

title = Label(page_2_frame, text="MATH QUIZ", font=("TkDefaultFont", 30),pady=20)
question_Text = StringVar()
question_Display = Label(page_2_frame, textvariable=question_Text, font=("TkDefaultFont", 24))

input_answer_Label = Label(page_2_frame,text="Input Answer :", font=("TkDefaultFont", 20), height=1, width=10)
user_Input = Entry(page_2_frame, font=("TkDefaultFont", 20), width=10)
user_Input.bind("<Return>", lambda e:isCorrect(user_Input.get()))

isCorrect_Display_Text = StringVar()
isCorrect_Display = Label(page_2_frame, textvariable=isCorrect_Display_Text, font=("TkDefaultFont", 20))

points_text = StringVar()
points_Display = Label(page_2_frame, textvariable=points_text, font=("TkDefaultFont", 20))

enter_Button = Button(page_2_frame, text="Enter", font=("TkDefaultFont", 20),command=lambda: isCorrect(user_Input.get()))


# ---- Display Frame 2 ---- 

title.place(x=175, y=30, width=400, height=50)
question_Display.place(x=135, y=95, width=480, height=40)
input_answer_Label.place(x=81, y=164, width=200, height=31)
user_Input.place(x=275, y=160, width=200, height=40)
isCorrect_Display.place(x=81, y=234, width=200, height=40)
points_Display.place(x=275, y=234, width=200, height=31)
enter_Button.place(x=475, y=230, width=200, height=40)


# ----------- Page 3 Frame Work----------- 
page_3_frame = Frame(main)

grade_frame_img = PhotoImage(file="UI assets\Grade frame.png")
grade_frame_display = Label(page_3_frame, text="", image=grade_frame_img)
grade_frame_display.pack()

title = Label(page_3_frame, text="MATH QUIZ", font=("TkDefaultFont", 30),pady=20)
score_Display_Text = StringVar()
score_Display = Label(page_3_frame, textvariable=score_Display_Text, font=("TkDefaultFont", 24))

replay_Button = Button(page_3_frame, text="Replay", font=("TkDefaultFont", 20),command=lambda:[reset(), frame_Manager(page_3_frame, page_1_frame)])
quit_Button = Button(page_3_frame, text="Quit", font=("TkDefaultFont", 20), command=main.destroy)

# ---- Display Frame 3 ---- 
title.place(x=175, y=30, width=400, height=50)
score_Display.place(x=125, y=95, width=500, height=40)
replay_Button.place(x=25, y=155, width=200, height=40)
quit_Button.place(x=525, y=155, width=200, height=40)

page_1_frame.tkraise()
main.mainloop()
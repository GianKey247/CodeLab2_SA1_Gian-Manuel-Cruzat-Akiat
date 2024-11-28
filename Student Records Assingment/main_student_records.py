from customtkinter import *
from tkinter import messagebox
from student_records_software import*

font_family="inter"
button_attrbutes_normal = {
    "text_color":"white",  
    "fg_color":"#444444", 
    "border_color":"#00ff00",
    "border_width":1, 
    "width":250, 
    "height":50,
    "font":(font_family,30)
}

button_attrbutes_small = {
    "text_color":button_attrbutes_normal["text_color"],  
    "fg_color":button_attrbutes_normal["fg_color"], 
    "border_color": button_attrbutes_normal["border_color"],
    "border_width":button_attrbutes_normal["border_width"], 
    "font":(font_family,20),
    "width":150, 
    "height":30    
}

combobox_attributes = {
    "fg_color":"#444444",
    "text_color":"white",
    "dropdown_fg_color":"#444444", 
    "dropdown_text_color":"white", 
    "button_color" : "#ff00d9",
    "dropdown_hover_color":"#ff00d9", 
    "border_color":"#ff00d9", 
    "border_width":1,
    "height":50,
    "font":(font_family,15)
}

entry_attributes_big = {
    "fg_color":"#444444",
    "text_color":"white", 
    "border_color":"#fffb00", 
    "border_width":1,
    "width":350, 
    "height":50,
    "font":(font_family,15)
}

entry_attributes_small = {
    "fg_color":entry_attributes_big["fg_color"],
    "text_color":entry_attributes_big["text_color"], 
    "border_color":entry_attributes_big["border_color"], 
    "border_width":entry_attributes_big["border_width"],
    "width":140, 
    "height":50,
    "font":(font_family,15)
}

textbox_attributes = {
    "fg_color":"#5C5C5C",
    "text_color":"white", 
    "border_color":"#000000", 
    "border_width":1, 
    "width":250, 
    "height":450,
    "font":(font_family,15)
}

label_attributes = {
    "text_color":"white", 
    "fg_color":"#002f4d",
    "corner_radius":5,
    "height":50,
    "font":(font_family,30)
}

class StudentRecordApp(CTk):
    def __init__(self, *args, **kwargs): 
        super().__init__(fg_color = "#444444",*args, **kwargs)
        self.frames = {}  
        self.current_frame:CTkFrame=None
  
        self.title("Student Record")

        for F in (MainPage, ManageRecords, AddStudentRecord, UpdateStudentRecords):
            frame = F(self)
            self.frames[F] = frame 
        self.show_frame(MainPage)
        

    def show_frame(self, new_frame:CTkFrame):
        frame:CTkFrame = self.frames[new_frame]
        if self.current_frame!=frame:
            if self.current_frame is None:
                self.current_frame=frame
            self.current_frame.grid_forget()
            self.current_frame=frame
    
        # Check if the 'refresh_all_Display' attribute exists and is callable
        refresh_method = getattr(frame, "refresh_all_Display", None)
        if callable(refresh_method):
            refresh_method()  # Call the method if it exists
        
        frame.grid(row = 0, column = 0, sticky ="nsew")
        frame.tkraise()

class StudentForm(CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, width=580, height=360, fg_color="#444444")
        set_student_record_Label = CTkLabel(self, text="Set Student Record", **label_attributes, width=580)

        self.student_id_Text = StringVar()
        student_ID_Label = CTkLabel(self, text="Student ID", **label_attributes, width=220)
        self.student_ID_Entry = CTkEntry(self, **entry_attributes_big, textvariable=self.student_id_Text)

        self.student_name_Text = StringVar()
        student_name_Label = CTkLabel(self, text="Student Name", **label_attributes, width=220)
        self.student_name_Entry = CTkEntry(self, **entry_attributes_big, textvariable=self.student_name_Text)

        student_scores_Label = CTkLabel(self, text="Student Records", ** label_attributes, width=580)

        self.first_score_Text = StringVar()
        first_score_label = CTkLabel(self, text="First Score", **label_attributes, width=140)
        first_score_label.configure(font=(font_family,20))
        self.first_score_Entry = CTkEntry(self, **entry_attributes_small, textvariable=self.first_score_Text)

        self.second_score_Text = StringVar()
        second_score_label = CTkLabel(self, text="Second Score", **label_attributes, width=140)
        second_score_label.configure(font=(font_family,20))
        self.second_score_Entry = CTkEntry(self, **entry_attributes_small, textvariable=self.second_score_Text)

        self.third_score_Text = StringVar()
        third_score_label = CTkLabel(self, text="Third Score", **label_attributes, width=140)
        third_score_label.configure(font=(font_family,20))
        self.third_score_Entry = CTkEntry(self, **entry_attributes_small, textvariable=self.third_score_Text)

        self.exam_score_Text = StringVar()
        exam_score_label = CTkLabel(self, text="Exam Score", **label_attributes, width=140)
        exam_score_label.configure(font=(font_family,20))
        self.exam_score_Entry = CTkEntry(self, **entry_attributes_small, textvariable=self.exam_score_Text)

        # --= Placing Student Record Elements =--
        set_student_record_Label.place(x=0,y=0)

        student_ID_Label.place(x=0, y=60)
        self.student_ID_Entry.place(x=230, y=60)

        student_name_Label.place(x=0, y=120)
        self.student_name_Entry.place(x=230, y=120)

        student_scores_Label.place(x=0, y=190)

        first_score_label.place(x=0, y=250)
        self.first_score_Entry.place(x=0, y=310)

        second_score_label.place(x=147, y=250)
        self.second_score_Entry.place(x=147, y=310)

        third_score_label.place(x=293, y=250)
        self.third_score_Entry.place(x=293, y=310)

        exam_score_label.place(x=440, y=250)
        self.exam_score_Entry.place(x=440, y=310)

    def validate(self):
        student_ID=self.student_id_Text.get()
        student_Name = self.student_name_Entry.get()
        student_FirstScore =self.first_score_Entry.get()
        student_SecondScore = self.second_score_Entry.get()
        student_ThirdScore = self.third_score_Entry.get()
        student_ExamScore = self.exam_score_Entry.get()

        if not student_ID :
            messagebox.showinfo("Invalid Student ID", "Student ID is Empty")
            return False
        if not student_Name:
            messagebox.showinfo("Invalid Name", "Name is Empty")
            return False
        if not student_FirstScore :
            messagebox.showinfo("Invalid First Score", "First Score is Empty")
            return False
        if not student_SecondScore :
            messagebox.showinfo("Invalid Second Score", "Second Score is Empty")
            return False
        if not student_ThirdScore :
            messagebox.showinfo("Invalid Third Score", "Third Score is Empty")
            return False
        if not student_ExamScore :
            messagebox.showinfo("Invalid Exam Score", "Exam Score is Empty")
            return False

        if int(student_ID) > 9999 or int(student_ID) <1000:
            messagebox.showinfo("Invalid ID", "Your ID is INVALID \n ID must be between 1000-9999") 
            return False
        if int(student_FirstScore) > 20 or int(student_FirstScore) < 0:
            messagebox.showinfo("Invalid Score", "Your First Score is INVALID \n Score must be between 0-20") 
            return False
        if int(student_SecondScore) > 20 or int(student_SecondScore) < 0:
            messagebox.showinfo("Invalid Score", "Your Second Score is INVALID \n Score must be between 0-20") 
            return False
        if int(student_ThirdScore) > 20 or int(student_ThirdScore) < 0:
            messagebox.showinfo("Invalid Score", "Your Third Score is INVALID \n Score must be between 0-20") 
            return False
        if int(student_ExamScore) > 100 or int(student_ExamScore) < 0:
            messagebox.showinfo("Invalid Score", "Your Exam Score is INVALID \n Exam Score must be between 0-100") 
            return False
        return True
    
    def set_values(self, student_id, name, first_score, second_score, third_score, exam_score):
        self.student_id_Text.set(student_id)
        self.student_name_Text.set(name)
        self.first_score_Text.set(first_score)
        self.second_score_Text.set(second_score)
        self.third_score_Text.set(third_score)
        self.exam_score_Text.set(exam_score)
        
    def get_values(self):
        student_id = self.student_ID_Entry.get()
        student_Name = self.student_name_Entry.get()
        student_FirstScore =self.first_score_Entry.get()
        student_SecondScore = self.second_score_Entry.get()
        student_ThirdScore = self.third_score_Entry.get()
        student_ExamScore = self.exam_score_Entry.get()
    
        return student_id,student_Name,student_FirstScore,student_SecondScore,student_ThirdScore,student_ExamScore

# ---------------======================== Frame Work========================---------------

# ------------============ Main Page ============------------
class MainPage(CTkFrame):
    def __init__(self, parent):
        super().__init__(parent,width=605, height=640, fg_color = "#444444")

        # --== Student Record Section ==--
        student_record_Label = CTkLabel(self, text="Student Record", **label_attributes, width=250)
        self.student_record_TextBox = CTkTextbox(self, **textbox_attributes)
 
        # --=Student Record Section Display --

        student_record_Label.place(x=30, y=65)
        self.student_record_TextBox.place(x=30, y=125)

        # --== Right side ==--

        display_options_Label = CTkLabel(self, text="Display Options", **label_attributes, width=250)
        all_students_Button = CTkButton(self, text="All Students", **button_attrbutes_normal, command=lambda:self.allStudentsButton())
        highest_score_Button = CTkButton(self, text="Highest Score", **button_attrbutes_normal, command=lambda:self.highestScoreButton())
        lowest_score_Button = CTkButton(self, text="Lowest Score", **button_attrbutes_normal, command=lambda:self.lowestScoreButton())

        search_student_Label = CTkLabel(self, text="Search Student", **label_attributes, width=250)

        self.input_student_id_ComboBox = CTkComboBox(self, **combobox_attributes, width=250,command= lambda _: self.searchStudentButton())
        search_Button = CTkButton(self, text="Search", **button_attrbutes_small, command=lambda:self.searchStudentButton())

        manage_records_Button = CTkButton(self, text="Manage Records", command=lambda:parent.show_frame(ManageRecords),**button_attrbutes_normal)

        # --=Right side Display =--

        display_options_Label.place(x=325, y=65)
        all_students_Button.place(x=325, y=125)
        highest_score_Button.place(x=325, y=195)
        lowest_score_Button.place(x=325, y=265)

        search_student_Label.place(x=325, y=350)
        self.input_student_id_ComboBox.place(x=325, y=410)
        search_Button.place(x=375, y=470)
        manage_records_Button.place(x=325, y=525)

        self.set_student_Records_Display("Some example text!\n" * 50)

    def set_student_Records_Display(self, text: str):
        self.student_record_TextBox.configure(state='normal')
        self.student_record_TextBox.delete('1.0', END)
        self.student_record_TextBox.insert("1.0", text)
        self.student_record_TextBox.configure(state="disabled")

    def highestScoreButton(self):
        self.set_student_Records_Display(display_sorted_student_percentage(True))

    def lowestScoreButton(self):
        self.set_student_Records_Display(display_sorted_student_percentage())

    def allStudentsButton(self):
        self.set_student_Records_Display(display_students_Record())

    def searchStudentButton(self):
        selected_student = self.input_student_id_ComboBox.get()
        student_id = selected_student.split(":")[0]
        self.set_student_Records_Display(display_selected_Student(student_id))

    def refresh_all_Display(self):
        self.set_student_Records_Display(display_students_Record())
        student_id_list = get_student_id_list()
        self.input_student_id_ComboBox.configure(values = student_id_list)
        self.input_student_id_ComboBox.set(student_id_list[0])

# ------------============ Manage Records ============------------

class ManageRecords(CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, width=950, height=640, fg_color = "#444444")

        # ----===== Student Record Section =====----

        student_record_Label = CTkLabel(self, text="Student Record", **label_attributes, width=250)

        self.student_record_TextBox = CTkTextbox(self, **textbox_attributes)

        # --=Student Record Section Display =--

        student_record_Label.place(x=30, y=65)
        self.student_record_TextBox.place(x=30, y=125)

        # ----===== Right side =====----

        manage_options_Label = CTkLabel(self, text="Manage Options", **label_attributes, width=250)
        sort_record_Button = CTkButton(self, text="Sort Record", **button_attrbutes_normal , command=lambda:self.sort_Records_button() )

        self.sorted_by_Label = CTkLabel(self, text=f"Sorted by : ID", **label_attributes, width=300)
        self.descending_Bool = BooleanVar()
        self.descend_checkbox = CTkCheckBox(self, text="Descending Order", variable=self.descending_Bool, width=300, height=50,font=(font_family,30), bg_color="#002f4d", text_color="white", border_color="white", command=lambda:self.sort_Records_CheckBox())

        add_Student_Button = CTkButton(self, text="Add Student",command=lambda:parent.show_frame(AddStudentRecord), **button_attrbutes_normal)
        update_record_Button = CTkButton(self, text="Update Record",command=lambda:parent.show_frame(UpdateStudentRecords), **button_attrbutes_normal)

        remove_student_Label = CTkLabel(self, text="Remove Student", **label_attributes, width=250)
        self.input_student_id_ComboBox = CTkComboBox(self, **combobox_attributes, width=250)
        remove_Button = CTkButton(self, text="Remove", **button_attrbutes_small, command=lambda:self.remove_student_Record())

        main_page_Button = CTkButton(self, text="Main Page", command=lambda:parent.show_frame(MainPage), **button_attrbutes_normal)

        # --=Right side Display =--
        manage_options_Label.place(x=325, y=65)
        sort_record_Button.place(x=325, y=125)
        self.descend_checkbox.place(x=620, y=195)

        self.sorted_by_Label.place(x=620, y=125)

        add_Student_Button.place(x=325, y=195)
        update_record_Button.place(x=325, y=265)

        remove_student_Label.place(x=325, y=350)
        self.input_student_id_ComboBox.place(x=325, y=410)
        remove_Button.place(x=375, y=470)
        main_page_Button.place(x=325, y=525)

        self.index = 0
        self.sorted_List = ["ID","Name", "Percentage"]

    def set_student_Records_Display(self, text: str):
        self.student_record_TextBox.configure(state='normal')
        self.student_record_TextBox.delete('1.0', END)
        self.student_record_TextBox.insert("1.0", text)
        self.student_record_TextBox.configure(state="disabled")
      
    def remove_student_Record(self):
        student_id_list = get_student_id_list()
        num_total_students=len(student_id_list)
        if num_total_students <= 1:
            messagebox.showinfo("","This is last student")
            return
        selected_student =self.input_student_id_ComboBox.get()
        student_id = selected_student.split(":")[0]
        delete_student_by_id_from_records(student_id)
        student_id_list = get_student_id_list()
        self.set_student_Records_Display(display_students_Record())
        
        self.input_student_id_ComboBox.configure(values = student_id_list)
        self.input_student_id_ComboBox.set(student_id_list[0])

    def sort_Records_button(self):
        self.index+=1
        self.index = self.index%len(self.sorted_List)
        self.sorted_by_Label.configure(text = f"Sort By: {self.sorted_List[self.index]}")
        self.set_student_Records_Display(display_sorted_record(self.sorted_List[self.index], self.descending_Bool.get()))
        
    def sort_Records_CheckBox(self):
        self.set_student_Records_Display( display_sorted_record(self.sorted_List[self.index], self.descending_Bool.get()))     

    def refresh_all_Display(self):
        self.set_student_Records_Display(display_students_Record())
        student_id_list = get_student_id_list()
        self.input_student_id_ComboBox.configure(values = student_id_list)
        self.input_student_id_ComboBox.set(student_id_list[0])

# ------------============ Add Student Records ============------------
class AddStudentRecord(CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, width=950, height=640, fg_color = "#444444")

        # ----===== Student Record Section =====----
        student_record_Label = CTkLabel(self, text="Student Record", **label_attributes, width=250)

        self.student_record_TextBox = CTkTextbox(self, **textbox_attributes)

        # --=Student Record Section Display =--
        student_record_Label.place(x=30, y=65)
        self.student_record_TextBox.place(x=30, y=125)

        # ----===== Student Record Values Frame =====----
        self.student_record_values_Frame = StudentForm(self)
        # --= Bottom Buttons =--
        manage_records_Button = CTkButton(self, text="Manage Records",command=lambda:parent.show_frame(ManageRecords), **button_attrbutes_normal)
        add_to_record_button = CTkButton(self, text="Add to Record", **button_attrbutes_normal, command=lambda:self.add_student_Record())

        # --= Display right section =--
        self.student_record_values_Frame.place(x=325, y=65)
        manage_records_Button.place(x=325, y=525)
        add_to_record_button.place(x=655, y=525)

    def set_student_Records_Display(self, text: str):
        self.student_record_TextBox.configure(state='normal')
        self.student_record_TextBox.delete('1.0', END)
        self.student_record_TextBox.insert("1.0", text)
        self.student_record_TextBox.configure(state="disabled")

    def add_student_Record(self):

        student_ID,student_Name,student_FirstScore,student_SecondScore,student_ThirdScore,student_ExamScore =self.student_record_values_Frame.get_values()
        if not self.student_record_values_Frame.validate():
            return
        add_Student_to_Records(student_ID, student_Name, int(student_FirstScore), int(student_SecondScore), int(student_ThirdScore), int(student_ExamScore))

        self.set_student_Records_Display(display_selected_Student(student_ID)) 

    def refresh_all_Display(self):
        self.student_record_values_Frame.set_values("","","","","","",)


# ------------============ Update Student Records ============------------
class UpdateStudentRecords(CTkFrame):
    def __init__(self, parent):
        super().__init__(parent,width=950, height=640, fg_color = "#444444")

        # ----===== Student Record Section =====----
        student_record_Label = CTkLabel(self, text="Student Record", **label_attributes, width=250)

        self.student_record_TextBox = CTkTextbox(self, **textbox_attributes)

        # --=Student Record Section Display =--
        student_record_Label.place(x=30, y=65)
        self.student_record_TextBox.place(x=30, y=125)

        # ----===== Update Record Section =====----
        input_student_id_label = CTkLabel(self, text="Input Student ID :", ** label_attributes, width=275)
        self.input_student_id_ComboBox = CTkComboBox(self, **combobox_attributes, width=295,values=get_student_id_list(),command= lambda e : self.display_current_student())
        
        manage_records_Button = CTkButton(self, text="Manage Records",command=lambda:parent.show_frame(ManageRecords), **button_attrbutes_normal)
        update_record_button = CTkButton(self, text="Update Record", **button_attrbutes_normal,command= lambda: self.update_Student_Record())

        # ----===== Student Record Values Frame =====----
        self.student_record_values_Frame=StudentForm(self)

        # --= Display right section =--
        input_student_id_label.place(x=325, y=65)
        self.input_student_id_ComboBox.place(x=610, y=65)
        self.student_record_values_Frame.place(x=325, y=140)
        manage_records_Button.place(x=325, y=525)
        update_record_button.place(x=655, y=525)


    def set_student_Records_Display(self, text: str):
        self.student_record_TextBox.configure(state='normal')
        self.student_record_TextBox.delete('1.0', END)
        self.student_record_TextBox.insert("1.0", text)
        self.student_record_TextBox.configure(state="disabled")

    def display_current_student (self):
        student_id = self.input_student_id_ComboBox.get()
        student_id = student_id.split(":")[0]
        name,firstScore,secondScore,thirdScore,examScore=get_Selected_Student(student_id)

        self.student_record_values_Frame.set_values(student_id,name,firstScore,secondScore,thirdScore,examScore)
        self.set_student_Records_Display(display_selected_Student(student_id))

    def update_Student_Record(self):
        student_ID,student_Name,student_FirstScore,student_SecondScore,student_ThirdScore,student_ExamScore=self.student_record_values_Frame.get_values()
        student_ID = self.input_student_id_ComboBox.get()
        student_ID = student_ID.split(":")[0]
        
        if not self.student_record_values_Frame.validate():
            return
        update_StudentRecord(student_ID,student_Name,int(student_FirstScore),int(student_SecondScore),int(student_ThirdScore),int(student_ExamScore))
        name,firstScore,secondScore,thirdScore,examScore=get_Selected_Student(student_ID)

        self.student_record_values_Frame.set_values(student_ID,name,firstScore,secondScore,thirdScore,examScore)

        self.set_student_Records_Display(display_selected_Student(student_ID))
        self.input_student_id_ComboBox.configure(values=get_student_id_list())
        self.input_student_id_ComboBox.set(get_student_index_from_Studentid(student_ID))
    
    def refresh_all_Display(self):
        self.input_student_id_ComboBox.configure(values=get_student_id_list())
        self.input_student_id_ComboBox.set(self.input_student_id_ComboBox.cget("values")[0])
        self.display_current_student()


if __name__ == "__main__":
    app = StudentRecordApp()
    app.mainloop()
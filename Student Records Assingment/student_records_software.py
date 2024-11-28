import csv
student_dict=dict()

def calculate_grade(percentage):
    if percentage >= 70:
        percentage = "A"
    elif percentage < 70 and percentage>= 60:
        percentage = "B"
    elif percentage < 60 and percentage>= 50:
        percentage = "C"
    elif percentage < 50 and percentage>= 40:
        percentage = "D"
    elif percentage < 40 :
        percentage = "F"
    return percentage

def calculate_Percentage(firstScore, secondScore, thirdScore, examScore):
    return int(((firstScore + secondScore + thirdScore + examScore) / 160) * 100)

def find_sudentID_from_Records(name:str):
    for student_ID, value in student_dict.items():
        if name.title() in value["Name"]:
            return student_ID         

def add_Student_to_Records(id, name:str, firstScore, secondScore, thirdScore, examScore):
    percentage = calculate_Percentage(firstScore, secondScore, thirdScore, examScore)
    global student_dict
    student_dict[id]={
        "Name" : name.title(),
        "FirstScore" : firstScore,
        "SecondScore" : secondScore, 
        "ThirdScore" : thirdScore, 
        "ExamScore" : examScore, 
        "Percentage" : percentage,
        "Grade" : calculate_grade(percentage)
    }
    student_dict=dict(sorted(student_dict.items()))
    save_user_Changes(student_dict)

def delete_student_by_id_from_records(id):
    global student_dict
    del(student_dict[id])
    student_dict=dict(sorted(student_dict.items()))
    save_user_Changes(student_dict)

def delete_student_by_name_from_records(name):
    delete_student_by_id_from_records(find_sudentID_from_Records(name))

def update_StudentRecord(id, name, firstScore, secondScore, thirdScore, examScore):
    delete_student_by_id_from_records(id)
    add_Student_to_Records(id, name, firstScore, secondScore, thirdScore, examScore)

def save_user_Changes(student_dict:dict):
    with open('studentMarks.txt', mode='w') as file : 
        num_students = len(student_dict.keys())
        file.write(f"{num_students}\n")
        for student_ID, value in student_dict.items():
            file.write(f"{student_ID},")
            for fieldname,value in value.items():
                if fieldname == "ExamScore":
                    file.write(f"{value}") 
                    break
                file.write(f"{value},")
            file.write("\n")

def sort_Record_by(key:str,descending:bool=False):
    if key.lower() == "id":
        return dict(sorted(student_dict.items(),reverse=descending))
    return dict(sorted(student_dict.items(), key=lambda x:x[1][key.title()],reverse=descending))

def display_sorted_student_percentage(descending:bool=False):
    sorted = sort_Record_by("Percentage",descending)
    student_ID = list(sorted.keys())[0]
    return f"""
ID : {student_ID}
Name : {sorted[student_ID]["Name"]}
First Score : {sorted[student_ID]["FirstScore"]}
Second Score : {sorted[student_ID]["SecondScore"]}
Third Score : {sorted[student_ID]["ThirdScore"]}
Exam Score : {sorted[student_ID]["ExamScore"]}
Percentage : {sorted[student_ID]["Percentage"]}%
Grade : {sorted[student_ID]["Grade"]}\n  
"""

def display_sorted_record(key:str,descending:bool=False):
    sorted_student_dict=sort_Record_by(key,descending)
    student_record = ""
    total_students = len(student_dict.keys())
    total_percentage = 0
    for student_ID, value in sorted_student_dict.items():    
        # "Name" : name,
        # "FirstScore" : firstScore,
        # "SecondScore" : secondScore, 
        # "ThirdScore" : thirdScore, 
        # "ExamScore" : examScore, 
        # "Percentage" : percentage,
        # "Grade" : calculate_grade(percentage)
        total_percentage += value["Percentage"] 
        student_record+=f"""
ID : {student_ID}
Name : {value["Name"]}
First Score : {value["FirstScore"]} 
Second Score : {value["SecondScore"]}
Third Score : {value["ThirdScore"]} 
Exam Score : {value["ExamScore"]}
Percentage : {value["Percentage"]}%
Grade : {value["Grade"]} \n  
        """
    student_record+=f"""
Total Students : {total_students}
Average Percentage : {(total_percentage/total_students):.2f}%
"""

    return student_record
def display_students_Record():
    student_record = ""
    total_students = len(student_dict.keys())
    total_percentage = 0
    for student_ID, value in student_dict.items():    
        # "Name" : name,
        # "FirstScore" : firstScore,
        # "SecondScore" : secondScore, 
        # "ThirdScore" : thirdScore, 
        # "ExamScore" : examScore, 
        # "Percentage" : percentage,
        # "Grade" : calculate_grade(percentage)
        total_percentage += value["Percentage"] 
        student_record+=f"""
ID : {student_ID}
Name : {value["Name"]}
First Score : {value["FirstScore"]}
Second Score : {value["SecondScore"]} 
Third Score : {value["ThirdScore"]}
Exam Score : {value["ExamScore"]}
Percentage : {value["Percentage"]}%
Grade : {value["Grade"]} \n  
        """
    student_record+=f"""
Total Students : {total_students}
Average Percentage : {(total_percentage/total_students):.2f}%
"""

    return student_record

def display_selected_Student(student_id):
        return f"""
ID : {student_id}
Name : {student_dict[student_id]["Name"]}
First Score : {student_dict[student_id]["FirstScore"]} 
Second Score : {student_dict[student_id]["SecondScore"]}
Third Score : {student_dict[student_id]["ThirdScore"]}
Exam Score : {student_dict[student_id]["ExamScore"]}
Percentage : {student_dict[student_id]["Percentage"]}%
Grade : {student_dict[student_id]["Grade"]}\n  
"""

def get_Selected_Student(student_id):
    student_data=student_dict[student_id]
    return student_data["Name"], student_data["FirstScore"], student_data["SecondScore"], student_data["ThirdScore"], student_data["ExamScore"]

def get_student_id_list():
    dropdown_menu = list()
    for student_id, value in student_dict.items():
        dropdown_menu.append(f"{student_id}: {value['Name']}")
    return dropdown_menu

def get_student_index_from_Studentid(student_id):
    for index, data in enumerate(get_student_id_list()):
        if str(student_id) in data :
            return index

with open('studentMarks.txt', mode='r') as file : 
    next(file) # Skip first line
    csv_reader=csv.reader(file)
    for row in csv_reader:
        id=row[0]
        name=row[1]
        firstScore = int(row[2])
        secondScore = int(row[3])
        thirdScore = int(row[4])
        examScore = int(row[5])
        percentage = calculate_Percentage(firstScore, secondScore, thirdScore, examScore)
        grade = calculate_grade(percentage)

        student_dict[id]={
            "Name" : name,
            "FirstScore" : firstScore,
            "SecondScore" : secondScore, 
            "ThirdScore" : thirdScore, 
            "ExamScore" : examScore, 
            "Percentage" : percentage,
            "Grade" : grade
        }

        student_dict=dict(sorted(student_dict.items()))
import menu
import data
import actions

class Student:
    def __init__(self,name,classroom,spanish_score,english_score,history_score,science_score):
        self.name=name
        self.classroom=classroom
        self.spanish_score=spanish_score
        self.english_score=english_score
        self.history_score=history_score
        self.science_score=science_score
        self.average_score=(spanish_score+english_score+history_score+science_score)/4
    @classmethod
    def from_dict(cls,dictionary):
        name=dictionary['name']
        classroom=dictionary['classroom']
        spanish_score=float(dictionary['spanish_score'])
        english_score=float(dictionary['english_score'])
        history_score=float(dictionary['history_score'])
        science_score=float(dictionary['science_score'])

        return cls(name,classroom,spanish_score,english_score,history_score,science_score)

student_list=[]
student_keys=['name','classroom','spanish_score','english_score','history_score','science_score','average_score']

while True:
    option=menu.initialize_menu()
    if option == 1:
        name, classroom, spanish,english, history, science=actions.get_new_student()#get the student data
        student_list.append(Student(name,classroom,spanish,english,history,science))
        input("Done. Press Enter to Continue")
    if option==2:
        actions.print_all(student_list)#se debe modificar
        input("Done. Press Enter to Continue")
    if option==3:
        data.show_top_3(student_list)
        input("Done. Press Enter to Continue")
    if option==4:
        print(f'Class Average Score: {actions.class_avg_score(student_list)}')
        input("Done. Press Enter to Continue")
    if option==5:
        student_dictionaries_list=[]
        for n in student_list:
            student_dictionaries_list.append(n.__dict__) 
        data.export_file('students.csv',student_dictionaries_list,student_keys)
        input("Done. Press Enter to Continue")
    if option==6:
        student_list=[]
        student_dictionaries_list=data.import_file('students.csv')
        for dictionaries in student_dictionaries_list:
            student=Student.from_dict(dictionaries)
            student_list.append(student)   
        input("Done. Press Enter to Continue")
    elif option==7:
        break
print("Program closed.") 
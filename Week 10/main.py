import menu
import data
import actions


student_dictionaries_list=[]
student_dictionary={}
student_keys=['name','class','spanish_score','english_score','history_score','science_score','average_score']

while True:
    option=menu.initialize_menu()
    if option == 1:
        student_info=actions.get_new_student()#get the student data
        student_dictionary=actions.create_student_dictionary(student_keys,student_info)#creates dict
        student_dictionaries_list.append(student_dictionary)#append dict to list
        input("Done. Press Enter to Continue")
    if option==2:
        actions.print_all(student_dictionaries_list,student_keys)
        input("Done. Press Enter to Continue")
    if option==3:
        data.show_top_3(student_dictionaries_list)
        input("Done. Press Enter to Continue")
    if option==4:
        print(f'Class Average Score: {actions.class_avg_score(student_dictionaries_list)}')
        input("Done. Press Enter to Continue")
    if option==5:
        data.export_file('students.csv',student_dictionaries_list,student_keys)
        input("Done. Press Enter to Continue")
    if option==6:
        student_dictionaries_list=data.import_file('students.csv')
        input("Done. Press Enter to Continue")
    elif option==7:
        break
print("Program closed.")
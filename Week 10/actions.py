def get_student_score():
    while True:
        try:
            score=input("Enter the student's score (0-100): ")
            score=float(score)
            if 0 <= score <=100:
                return score
            else:
                print ("Error. The score must be between 0 and 100. ")
        except ValueError:
            print ("Error: Please enter a valid number (int or float).")

def print_all(dictionary,keys):
    for index in range(len(dictionary)):
        print(dictionary[index])

def calculate_avg_score(score1, score2, score3, score4):
    avg_score = (score1+score2+score3+score4)/4
    return avg_score

def class_avg_score(dictionaries_list):
    counter=0
    sum=0
    for n in range(len(dictionaries_list)):
        sum=sum+float(dictionaries_list[n]['average_score'])
        counter+=1
    if counter !=0:
        avg_score = float(sum /counter)
        return avg_score
    else:
        return 0
    
def create_student_dictionary(list1,listb):
    cont=0
    dictionary={}
    for index in list1:
        dictionary[index]=listb[cont]
        cont+=1
    return dictionary

def get_new_student():
    student_info=[]
    student_info.append(input('Please enter the student full name: '))
    student_info.append(input('Please enter the student class: '))
    print("Spanish Class")
    spanish_score=get_student_score()
    print("English Class")
    english_score=get_student_score()
    print("History Class")
    history_score=get_student_score()
    print("Science Class")
    science_score=get_student_score()
    student_info.append(spanish_score)
    student_info.append(english_score)
    student_info.append(history_score)
    student_info.append(science_score)
    student_info.append(calculate_avg_score(spanish_score,english_score,science_score,history_score))
    return student_info

def get_student_score(): #This function stills works since validate the score. 
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

def print_all(list): 
    for index in range(len(list)):
        print(list[index].name)
        print(list[index].classroom)
        print(list[index].spanish_score)
        print(list[index].english_score)
        print(list[index].history_score)
        print(list[index].science_score)
        print(list[index].average_score)

def class_avg_score(list):
    counter=0
    sum=0
    for n in range(len(list)):
        sum=sum+float(list[n].average_score)
        counter+=1
    if counter !=0:
        avg_score = float(sum /counter)
        return avg_score
    else:
        return 0

def get_new_student():
    name=input('Please enter the student full name: ')
    classroom=input('Please enter the student class: ')
    print("Spanish Class")
    spanish_score=get_student_score()
    print("English Class")
    english_score=get_student_score()
    print("History Class")
    history_score=get_student_score()
    print("Science Class")
    science_score=get_student_score()
    return name, classroom, spanish_score, english_score,history_score,science_score
def initialize_menu ():
    while True:
        print ("Welcome to the student control program.")
        print ("----------MENU----------")
        print("1.Add a new student")
        print("2.View students")
        print("3.View Top 3 Students")
        print("4.View students average score")
        print("5.Export CSV file")
        print("6.Import CSV file")
        print("7.Exit")
        print("Please enter the number of the option and press Enter")
        try:
            option=int(input())
            if 0 < option < 8:
                return option     
            else:
                print("Input error, type a number from the menu")
                print("Press ENTER to continue")
                input()
        except ValueError:
                print("Input error, type a number from the menu")
                print("Press ENTER to continue")
                input() 
        

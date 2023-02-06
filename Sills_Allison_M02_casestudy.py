##Allison Sills
##GPA tester
##This app will tell a student if they qualify for the deans list

#get students last name

last_name = input("Enter student's last name: ")
#test is last name equals ZZZ
if last_name != "ZZZ" or last_name != "zzz":

    first_name = input("Enter student's first name: ")

    GPA = float(input("Enter Students GPA: "))
    #set requirements for GPA
    if GPA >= 3.5:
        print("Congratulations " + first_name + " " + last_name + "! You made the Deans List!")
    elif GPA >= 3.25 and GPA < 3.5:
        print("Congratulations " + first_name + " " + last_name + "! You made the Honor Roll!")
    else:
        print("Sorry " + first_name + " " + last_name + ", you did not make the Deans List or Honor Roll this semester.")
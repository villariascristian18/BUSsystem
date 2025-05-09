import os
import msvcrt as m
import datetime

Passenger = "Passenger.txt"

class Transport:
    def __init__(self, transport_id):
        self.transport_id = transport_id
        self.passengers = []

transport = Transport("|Bus-001|")

def age_1():
    while True:
        try:
            age = input("Enter Age: ")
            if age.isalpha():
                print("Invalid")
            else:
                age = int(age)  
                return age
        except ValueError:
            print("invalid")

def contact_info():
    while True:
        try:
            contact_number = input("Enter Family Number: ")
            if contact_number.isalpha():
                print("Invalid")
            else:
                contact = int(contact_number) 
                return contact_number
        except ValueError:
            print("invalid")


def add_passenger():
        name = input("Enter passenger name: ")
        date = datetime.datetime.now().strftime("%d-%m-%Y , %H:%M:%S")
        contact_number = contact_info()
        age = age_1()
        gender = input("Enter Gender [M. Male] [F. Female] [O. Other gender]: ").upper()

        if gender == 'M':
            gender = "Male"
        elif gender == 'F':
            gender = "Female"
        elif gender == ("O"):
            enter = input("Other Gender: ")
            gender = enter
        else:
            print("Invalid Choice...")
            m.getch()


        with open(Passenger, 'a') as file:
            file.write(f"{name}|{date}|{contact_number}|{age}|{gender}\n")
        print("Add successfully..")


def View_passenger():

    if not os.path.exists(Passenger):
        print("No Passenger..")
        input("Press enter to continue...")
        return
    
    with open(Passenger, 'r') as file:
        Passenger_list = file.readlines()

    if not Passenger_list:
        print("No Passenger..")
        input("Press enter to continue...")
        return
    
    for i, line in enumerate(Passenger_list):
        name, date, contact_number,age,gender = line.strip().split('|')
        print(f"{i + 1}. Name: {name}   Date: {date}  Contact Number: {contact_number} Age: {age}  Gender: {gender}")

    m.getch()

def remove_passenger():

    if not os.path.exists(Passenger):
        print("No Passenger..")
        input("Press enter to continue...")
        return
    
    with open(Passenger, 'r') as file:
        Passenger_list = file.readlines()

    if not Passenger_list:
        print("No Passenger..")
        input("Press enter to continue...")
        return
    
    for i, line in enumerate(Passenger_list):
        name, date, contact_number,age,gender = line.strip().split('|')
        print(f"{i + 1}. Name: {name}   Date: {date}  Contact Number: {contact_number} Age: {age}  Gender: {gender}")
    m.getch()

    try:
        remove = int(input("Enter the number to delete passenger / input 0 to exit: ")) -1
        if remove == -1:
            print("Exiting...")
            print("Press enter to continue...")
            m.getch()

        elif 0 <= remove <len(Passenger_list):
            del Passenger_list[remove]
            with open(Passenger, 'w') as file:
                file.writelines(Passenger_list)
            print("\n")
            print("Passenger remove successfully!")
            m.getch()

        else: 
            print(" Invalid choice...")
            m.getch()

    except ValueError:
        print("Invalid chouce...")
        m.getch()


while True:
    os.system('cls')
    print("------------------------")
    print('{:^143}'.format(f"{transport.transport_id}"))
    print("------------------------")
    
    print('{:>78}'.format("[1] Add Passenger"))
    print('{:>83}'.format("[2] Get Passenger List"))
    print('{:>81}'.format("[3] Remove Passenger"))
    print('{:>69}'.format("[4] Exit"))
    
    print("------------------------")
    choice = input('{:>80}'.format("Choose an option: "))
   
   
    
    if choice == "1":
        os.system('cls')
        add_passenger()

    elif choice == "2":
        os.system('cls')
        View_passenger()                    
   
    elif choice == "3":
        os.system('cls')
        remove_passenger()
    elif choice == "4":
        os.system('cls')
        print("________________________________")
        print("Thank you for using the program!")
        print("________________________________")
        m.getch()
        break
    else:
        print("___________________________________")               
        print("Invalid option. Please choose again.")
        m.getch()
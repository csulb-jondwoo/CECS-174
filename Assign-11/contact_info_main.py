#Jon Ham
#CECS 174

#main.py

import contact_info_class

##MENU'S
#Main menu
def menu():
    print("Rolodex Menu:\n"
          "1. Add Contact\n"
          "2. Search for Contact\n"
          "3. Modify Contact\n"
          "4. Display Number of Contacts\n"
          "5. Display All Contacts\n"
          "6. Quit")
#Search Menu
def search_menu():
    print("Search Menu: \n"
          "A. Search by Last Name\n"
          "B. Search by Zip-Code")
#Modify menu
def modify_menu():
    print()
    print("Modify Menu:\n"
          "A. Enter First Name\n"
          "B. Enter Last Name\n"
          "C. Enter Phone Number\n"
          "D. Enter Address\n"
          "E. Enter City\n"
          "F. Enter State\n"
          "G. Enter Zip-Code\n"
          "Q. Save and Quit")

##FUNCTIONS
def convert_file_to_obj_list():
    contact_list = []
    contents = open("addresses.txt", "r")
    line = contents.read().splitlines()
    for index in line:
        attr = index.split(",")
        contact = contact_info_class.Contact(attr[0], attr[1], attr[2], attr[3], attr[4], attr[5], attr[6])
        contact_list.append(contact)
    contents.close()
    return contact_list

#def write_to_file():



def add_contact(contact_list):
    contact_info = contact_info_class.Contact(input("Enter First Name: "),
                                              input("Enter Last Name: "),
                                              input("Enter Phone Number: "),
                                              input("Enter Address: "),
                                              input("Enter City: "),
                                              input("Enter State: "),
                                              input("Enter Zip: "))
    print()
    contact_list.append(contact_info)


def search_contact(contact_list, user_selection_search):
    #SEARCH BY LAST NAME
    if user_selection_search == "A":
        last_name = input("Enter Last Name: ")
        for contact in contact_list:
            if last_name == contact.get_last_name():
                print(contact)
                return
        print("Contact does not exist")
    #SEARCH BY ZIPCODE
    else: #FIXME
        zip_code = int(input("Enter Zip Code: "))
        for contact in contact_list:
            if zip_code == contact.get_zip():
                print(contact)
                return
        print("Contact does not exist")

def pull(contact_list):
    invalid_pull = True
    while invalid_pull:
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        for contact in contact_list:
            if last_name == contact.get_last_name() and first_name == contact.get_first_name():
                invalid_pull = False
                return contact
        print("Contact does not exist.")
        #FIXME Go back to main menu
        print()

def modify(user_selection, pulled_contact):
    if user_selection == "A":
        new_first_name = input("Enter new first name: ")
        pulled_contact.set_first_name(new_first_name)
    elif user_selection == "B":
        new_last_name = input("Enter new last name: ")
        pulled_contact.set_last_name(new_last_name)
    elif user_selection == "C":
        new_phone_num = input("Enter new phone number: ")
        pulled_contact.set_phone_num(new_phone_num)
    elif user_selection == "D":
        new_address = input("Enter new address: ")
        pulled_contact.set_address(new_address)
    elif user_selection == "E":
        new_city = input("Enter city: ")
        pulled_contact.set_city(new_city)
    elif user_selection == "F":
        new_state = input("Enter state: ")
        pulled_contact.set_state(new_state)
    elif user_selection == "G":
        new_zip = input("Enter new zipcode: ")
        pulled_contact.set_zip(new_zip)
    else:
        print()
        #FIXME QUIT

def display_contact_num(contact_list):
    print("There are",len(contact_list),"available contacts in this address book.")
    print()

def display_all_contacts(contact_list):
    for i in contact_list:
        print(i)
    print()

##INPUT VALIDATIONS
#Input Validation for menu
def check_input():
    invalid_selection = True
    user_selection = 0
    while invalid_selection:
        user_selection = input("Enter your selection: ")
        if user_selection.isdigit():
            user_selection = int(user_selection)
            if user_selection < 1 or user_selection > 6:
                print("Input not within range")
                print()
            else:
                invalid_selection = False
        else:
            print("Invalid entry. Enter a number.")
            print()
    return user_selection

#Input Validation for Modify menu
def check_input2():
    invalid_selection = True
    user_selection = " "
    while invalid_selection:
        user_selection = input("Enter your selection: ")
        if user_selection.isalpha():
            if (user_selection < "A"):
                print("Input not within range")
                print()
            else:
                invalid_selection = False
        else:
            print("Invalid entry. Enter a letter.")
            print()
    return user_selection

#Input validation for Search Menu
def check_input3():
    invalid_selection = True
    user_selection = " "
    while invalid_selection:
        user_selection = input("Enter your selection: ")
        if user_selection.isalpha():
            if (user_selection < "A" or user_selection > "B"):
                print("Input not within range")
                print()
            else:
                invalid_selection = False
        else:
            print("Invalid entry. Enter a letter.")
            print()
    return user_selection

########################################################################################################################
contact_list = convert_file_to_obj_list()

invalid = True
while invalid:
    menu()
    user_selection = check_input()
    #ADD CONTACTS
    if user_selection == 1:
        print()
        add_contact(contact_list)
    #SEARCH CONTACTS
    elif user_selection == 2:
        invalid_search = True
        while invalid_search:
            print()
            search_menu()
            user_selection_search = check_input3()
            #SEARCH BY LAST NAME
            if user_selection_search == "A":
                print()
                search_contact(contact_list, user_selection_search)
                invalid_search = False
            #SEARCH BY ZIPCODE
            else:
                search_contact(contact_list, user_selection_search)
                invalid_search = False
        print()
    elif user_selection == 3:
        pulled_contact = pull(contact_list)
        invalid_mod = True
        while invalid_mod:
            modify_menu()
            user_selection_mod = check_input2()
            if user_selection_mod == "A":
                modify(user_selection_mod, pulled_contact)
                print()
            elif user_selection_mod == "B":
                modify(user_selection_mod, pulled_contact)
                print()
            elif user_selection_mod == "C":
                modify(user_selection_mod, pulled_contact)
                print()
            elif user_selection_mod == "D":
                modify(user_selection_mod, pulled_contact)
                print()
            elif user_selection_mod == "E":
                modify(user_selection_mod, pulled_contact)
                print()
            elif user_selection_mod == "F":
                modify(user_selection_mod, pulled_contact)
                print()
            elif user_selection_mod == "G":
                modify(user_selection_mod, pulled_contact)
                print()
            else:
                #FIXME ACCOUNT FOR Q
                invalid_mod = False
    elif user_selection == 4:
        print()
        display_contact_num(contact_list)
    elif user_selection == 5:
        print()
        display_all_contacts(contact_list)
    else:
        #FIXME write_to_file(contact_list)
        print()
        # contact_list = str(contact_list)
        # contents = open("addresses.txt", "w")
        # contents.write(contact_list)
        # contents.close()
        print("Saving Changes... Done!")
        invalid = False

#When searching, pull up all contacts with same
#create save function (write_file function)

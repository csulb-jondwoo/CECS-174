#Jon Ham
#CECS 174

import contact_info_class

##MENU'S##
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

##FUNCTIONS##
def add_contact():
    contact_info = contact_info_class.Contact(input("Enter First Name: "),
                                              input("Enter Last Name: "),
                                              input("Enter Phone Number: "),
                                              input("Enter Address: "),
                                              input("Enter City: "),
                                              input("Enter State: "),
                                              input("Enter Zip: "))
    print()

    with open("addresses.txt", "a") as contents:
        contents.write(str(contact_info))
    contents.close()
    #FIXME CONTACT APPENDED BUT NOT DISPLAYED WHEN USER SELECTION 5

def search_contact(contacts, user_selection_search):
    #SEARCH BY LAST NAME
    if user_selection_search == "A":
        last_name = input("Enter Last Name: ")
        #FIXME

    #SEARCH BY ZIPCODE
    else:
        zip_code = int(input("Enter Zip Code: "))
        #FIXME

def display_contact_num(contacts):
    print("There are",len(contacts),"available contacts in this address book.")
    print()

def display_all_contacts(contacts):
    for i in contacts:
        print(i)
    print()

##INPUT VALIDATIONS##
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
            if (user_selection < "A" or user_selection > "G"): #FIXME ACCOUNT FOR "Q"
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
with open("addresses.txt", 'r') as contents:
    contacts = [line.strip() for line in contents]

invalid = True
while invalid:
    menu()
    user_selection = check_input()
    #ADD CONTACTS
    if user_selection == 1:
        print()
        add_contact()
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
                search_contact(contacts, user_selection_search)
            #SEARCH BY ZIPCODE
            else:
                search_contact(contacts, user_selection_search)
    elif user_selection == 3:
        invalid_mod = True
        while invalid_mod:
            #FIXME MODIFY BY NAME
            modify_menu()
            user_selection_mod = check_input2()
            if user_selection_mod == "A":
                #FIXME ENTER FIRST NAME
                print()
            elif user_selection_mod == "B":
                #FIXME ENTER LAST NAME
                print()
            elif user_selection_mod == "C":
                #FIXME ENTER PHONE NUMBER
                print()
            elif user_selection_mod == "D":
                #FIXME ENTER ADDRESS
                print()
            elif user_selection_mod == "E":
                #FIXME ENTER CITY
                print()
            elif user_selection_mod == "F":
                #FIXME ENTER STATE
                print()
            elif user_selection_mod == "G":
                #FIXME ENTER ZIPCODE
                print()
            else:
                invalid_mod = False
    elif user_selection == 4:
        print()
        display_contact_num(contacts)
    elif user_selection == 5:
        print()
        display_all_contacts(contacts)
    else:
        print()
        print("Saving Changes... Done!")
        invalid = False

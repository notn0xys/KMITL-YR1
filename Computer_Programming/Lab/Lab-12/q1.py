contact = {}
while True:
    print("Phonebook Manager")
    print('Press "+" to add a new contact')
    print('Press "-" to delete a new contact')
    print('Press "f" to find a contact')
    print('Press "p" to print out all contacts in the phonebook')
    choice = input("Press 'q' to quit the program \n")
    match choice:
        case "+":
            name = input("Enter contact name: ")
            contact[name] = input("Enter number: ")
        case "-":
            name = input("Enter the name of the person you wish to delete: ")
            if name not in contact.keys():
                print("Name not found")
                continue
            else:
                del contact[name]
                print(f"{name} Sucessfully Deleted")
        case "f":
            name = input("Enter contact name: ")
            if name not in contact.keys():
                print("Name not found")
                continue
            else:
                print(f"Name {name}: Contact: {contact[name]}")
        case "p":
            print(contact)
        case "q":
            print("Exiting")
            break
        case _:
            print("Invalid Command Try again")
            continue
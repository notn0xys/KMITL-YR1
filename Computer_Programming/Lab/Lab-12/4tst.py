while True:
    print("Phonebook Manager")
    print('Press "+" to add a new contact')
    print('Press "-" to delete a contact')
    print('Press "f" to find a contact')
    print('Press "p" to print out all contacts in the phonebook')
    choice = input('Press "q" to quit the program \n')
    contact = {}
    match choice:
        case "+" :
            name = input("Enter name:")
            contact[name] = input("Enter the number")
        case "-":
            delname = input("Select to delete contact: ")
            del contact[name]
        case "f":
            list = input("Find a contact:")
        case "p":
            print(contact)
        case "q":
            print("Goodbye")
            break
        case _:
            continue
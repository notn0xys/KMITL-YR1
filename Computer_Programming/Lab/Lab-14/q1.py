import pickle
import os
contact = {}
while True:
    print("Phonebook Manager")
    print('Press "+" to add a new contact')
    print('Press "-" to delete a new contact')
    print('Press "f" to find a contact')
    print('Print "s" to save contents to a file')
    print('Print "l" to load previous saved contact from a file')
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
        case "s":
            while True:
                meow = input("File name: ")
                meow+= ".pickle"
                if os.path.isfile(meow):
                    print(f"File {meow} already exists. Not overwriting.")
                    break
                try:
                    with open(meow, 'wb') as f:
                        pickle.dump(contact, f)
                    print("Saved sucess")
                    break
                except:
                    print("File already exist try agian")
                    continue
        case "l":
            while True:
                meow = input("File name: ")
                meow += ".pickle"
                try:
                    with open(meow, "rb") as f:
                        contact = pickle.load(f)
                    print("load sucess")
                    break
                except:
                    print("File not found")
                    continue
        case "q":
            print("Exiting")
            break
        case _:
            try:
                raise KeyError
            except:
                print("Invalid Command Try again")
                continue
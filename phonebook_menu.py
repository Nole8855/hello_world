#1. PHONE BOOK
def options_submenu():
    while True:
        print("\n--- 1. PHONE BOOK ---")
        print("1. Search")
        print("2. Service Numbers")
        print("3. Add name")
        print("4. Erase")
        print("5. Edit")
        print("6. Copy")
        print("7. Assign tone")
        print("8. Send b'card")
        print("9. Options")
        print("10. Speed dials")
        print("Voice tags")
        
        
        choice = input("Enter menu number from (1-11): ")
        
            case "1":
                print(">> Opening Search...")
            case "2":
                print(">> Opening Service Nos...")
            case "3":
                print(">> Adding a new name...")
            case "4":
                print(">> Erasing contact...")
            case "5":
                print(">> Editing contact...")
            case "6":
                print(">> Copying contact...")
            case "7":
                print(">> Assigning ringing tone...")
            case "8":
                print(">> Sending business card...")
            case "9":
                print("\n--- Options ---")
                print("1. Memory in use")
                print("2. Type of view")
                print("3. Memory status")
                print("0. Back to Phone book")
        
                choice = input("Select an option: ")
        
                choice:
                    case "1":
                        print("Viewing memory in use...")
                    case "2":
                        print("Changing type of view...")
                    case "3":
                        print("Checking Memory status...")  
                    case _:
                        print("Invalid option in the menu.")
    case "10":
        print(">> Configuring Speed dials...")
    case "0":
        print("Exiting Phone book.")
                break
    case _:
        print("Invalid option. Enter a number from 0 to 10.")

    
        
  phone_book()    
    
    
    
    
    
    
    


contacts = {}

while True:
    print("\n=== CONTACT BOOK ===")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")
    
    choice = input("Choose an option (1-5): ").strip()
    
    if choice == "1":
        name = input("Enter contact name: ").strip()
        phone = input("Enter phone number: ").strip()
        contacts[name] = phone
        print(f"Contact '{name}' added successfully!")
        
    elif choice == "2":
        if not contacts:
            print("Your contact book is empty.")
        else:
            print("\n--- Contact List ---")
            for name, phone in contacts.items():
                print(f"Name: {name} | Phone: {phone}")
                
    elif choice == "3":
        name = input("Enter the name to search: ").strip()
        if name in contacts:
            print(f"Found! Name: {name} | Phone: {contacts[name]}")
        else:
            print("Contact not found.")
            
    elif choice == "4":
        name = input("Enter the name to delete: ").strip()
        if name in contacts:
            del contacts[name]
            print(f"Contact '{name}' deleted.")
        else:
            print("Contact not found.")
            
    elif choice == "5":
        print("Goodbye!")
        break
        
    else:
        print("Invalid choice. Please pick a number from 1 to 5.")
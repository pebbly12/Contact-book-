import re

user_contact = []

def get_user_input():
    while True:
        name = input("Enter name: ").strip()
        number = input("Enter phone number: ").strip()
        email = input("Enter email: ").strip()
        address = input("Enter address: ").strip()

        if validate_contact(name,number,email,address):
            print("\nContact added successfully!")

            return {
                "name": name,
                "number": number,
                "email": email,
                "address": address }
        else:
            print("Invalid input.Please check your details and try again.\n")

def add_contact():
    global user_contact
    user_contact.append(get_user_input())

def view_contact():
    if user_contact:
        for i,contact in enumerate(user_contact,1):
            print(f"{i}. {contact['name']}")
            print(f"   Phone: {contact['number']}")
            print(f"   Email: {contact['email']}")
            print(f"   Address: {contact['address']}\n")
    else:
        print("No contact information found. Please add your contact first!\n")

def search_contact():
    search = input("Enter name to search: ").strip()
    found = False
    for contact in user_contact:
        if search in contact['name']:
            print("\n--- Search Results ---")
            view_contact()
            found = True
    if not found:
        print("The name cannot be found!\n")

def update_contact():
    global user_contact
    if not user_contact:
        print("No contact information found!,please add your contacts first\n")
        return 

    update_name = input("Enter name of contact to update: ").strip()
    found = False

    for contact in user_contact:
        if contact['name'] == update_name:
            found = True 

            new_name = input("Enter new name (or leave blank to keep the same): ").strip()
            if new_name and validate_name(new_name):
                contact['name'] = new_name
                
            new_address = input("Enter new address (or leave blank to keep the same): ").strip()
            if new_address and validate_address(new_address):
                contact['address'] = new_address
                
            new_email = input("Enter new email (or leave blank to keep the same): ").strip()
            if new_email and validate_email(new_email):
                contact['email'] = new_email

            new_number = input("Enter new phone number (or leave blank to keep the same): ").strip()
            if new_number and validate_number(new_number):
                contact['number'] = new_number
                
            print("Contact updated successfully!")
            break 

    if not found:
        print("Contact not found!")

def delete_contact():
    global user_contact
    if user_contact:
        delete = input("Enter the name of contact to delete: ").strip()
        found = False 

        for contact in user_contact:
            if contact["name"].lower() == delete.lower():
                user_contact.remove(contact)
                print("Contact deleted successfully!")
                found = True

        if not found:
            print("Contact not found!\n")
    else:
        print("No contact information to delete.\n")

def validate_name(name):
    # remove spaces from the name
    name_no_spaces = name.replace(" ","")
    # Check if all characters are alphabetic and length is between 2 and 50
    return name_no_spaces.isalpha() and 2 <= len(name) <= 50

def validate_number(number):
    cleaned_number = ''.join(filter(str.isdigit, number))
    return len(cleaned_number) == 10

def validate_email(email):
    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(email_pattern, email) is not None

def validate_address(address):
    return len(address) >= 4

def validate_contact(name,number,email,address):
    return (validate_name(name) and 
            validate_number(number) and 
            validate_email(email) and 
            validate_address(address)
    )


def BasicContactBooks():
    print("Welcome to the Basic Contact Book!")
    options = ("\n1. Add Contact\n2. Views Contacts\n3. Search Contact\n4. Update Contact\n5. Delete Contact\n6. Exit")
    print(options)
    while True:
        # Prompt the user for input 
        chose = int(input("\nPlease select an option (1-6): "))

        if chose == 1:
            print("--- Add Contact ---")
            add_contact()
            print(options)
            
        elif chose == 2:
            print("--- Contacts ---")
            view_contact()
            print(options)

        elif chose == 3:
            print("\n--- Search Contact ---")
            search_contact()
            print(options)
            
        elif chose == 4:
            print("\n--- Update Contact ---")
            update_contact()
            print(options)

        elif chose == 5:
            print("\n--- Delete Contact ---")
            delete_contact()
            print(options)

        elif chose == 6:
            print("Thanks for you co-operation!")
            break
        else:
            print("Choose again!\n")

BasicContactBooks()


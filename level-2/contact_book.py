import json

FILE_CONTACT = "python-nuggets/level-2/contact.json"

def load_contacts():
    try:
        with open(FILE_CONTACT, "r") as file:
            contacts = json.load(file)
            print("Contacts loaded successfully.")
            return contacts
    except FileNotFoundError:
        print("No saved contacts found.")
        return []
    
def save_contacts(contacts):
    with open(FILE_CONTACT, "w") as file:
        json.dump(contacts, file, indent=4)

def display_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return
    else:
        print("==========================\n")
        for contact in contacts:
            print(f"name: {contact['name']}\nphone: {contact['phone']}\ne-mail: {contact['email']}\n")
        print("==========================")

def add_contacts(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")

    contacts.append({"name": name, "phone": phone, "email": email})
    print("Contact added successfully!")
    save_contacts(contacts)

def search_contact(contacts):
    query = input("Enter name, phone, or email to search: ")
    results = [contact for contact in contacts if query.lower() in contact["name"].lower() or query in contact["phone"] or query.lower() in contact["email"].lower()]
    if results:
        display_contacts(results)
    else:
        print("No contacts found")

def update_contact(contacts):
    name = input("Enter the name of the contact to update: ")
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            print("Current details:")
            print(f"name: {contact['name']}\nphone: {contact['phone']}\nemail: {contact['email']}\n")
            contact['phone'] = input("Enter new phone number (leave blank to keep current): ") or contact["phone"]
            contact['email'] = input("Enter new email (leave blank to keep current): ") or contact["email"]

            print("Contact updated successfully!")
            save_contacts(contacts)
            return
    print("Contact not found.")

def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ")
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            contacts.remove(contact)
            print("Contact deleted successfully!")
            save_contacts(contacts)
            return
    print("Contact not found.")

def main():
    contacts = load_contacts()
    print("CONTACT BOOK")

    while True:
        print("""
1. Add a contact
2. View all contacts
3. Search for a contact
4. Update a contact
5. Delete a contact
6. Save and Exit
""")
        choice = input("Choose an option: ")
        if choice == "1":
            add_contacts(contacts)
        elif choice == "2":
            display_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            save_contacts(contacts)
            print("Save contacts data...\nThank you! —hazellenuts")
            break

if __name__ == "__main__":
    main()
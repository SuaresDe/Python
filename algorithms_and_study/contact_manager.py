import json

contact_file = "contacts.json"

def load_contacts():
    try:
        with open(contact_file, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_contact(contacts):
    with open(contact_file, "w", encoding="utf-8") as f:
        json.dump(contacts, f, indent=4, ensure_ascii=False)

def add_contact():
    name = input("Enter contact name: ")
    telephone = input("Enter the contact's telephone number: ")
    email = input("Enter the contact's email: ")
    
    contacts = load_contacts()
    contacts.append({"name": name, "telephone": telephone, "email": email})

    save_contact(contacts)
    print(f"Contact '{name}' added successfully.")

def list_contacts():
    contacts = load_contacts()
    if not contacts:
        print("No contacts found.")
        return
    
    print("\nContacts List:")
    for i, contact in enumerate(contacts, 1):
        print(f"{i}. {contact['name']} - {contact['telephone']} - {contact['email']}")

def search_contact():
    name_search = input("Enter the contact name to search: ")
    contacts = load_contacts()

    contacts_found = [c for c in contacts if name_search.lower() in c["name"].lower()]

    if not contacts_found:
        print("Contact not found.")
        return

    print("\nContacts found:")
    for contact in contacts_found:
        print(f"{contact['name']} - {contact['telephone']} - {contact['email']}")

def edit_contact():
    name_search = input("Enter the contact name to edit: ")
    contacts = load_contacts()

    for contact in contacts:
        if contact["name"].lower() == name_search.lower():
            print(f"Editing contact: {contact['name']}")

            new_name = input(f"New name ({contact['name']}): ") or contact["name"]
            new_telephone = input(f"New number ({contact['telephone']}): ") or contact["telephone"]
            new_email = input(f"New email ({contact['email']}): ") or contact["email"]

            contact.update({"name": new_name, "telephone": new_telephone, "email": new_email})

            save_contact(contacts)
            print("Contact updated successfully.")
            return

    print("Contact not found.")

def delete_contact():
    name_search = input("Enter the contact name to delete: ")
    contacts = load_contacts()

    filtered_contacts = [c for c in contacts if c["name"].lower() != name_search.lower()]

    if len(contacts) == len(filtered_contacts):
        print("Contact not found.")
        return
    
    save_contact(filtered_contacts)
    print(f"Contact '{name_search}' removed successfully.")

def menu():
    while True:
        print("\nContact Manager:")
        print("1 - Add Contact")
        print("2 - List Contacts")
        print("3 - Search Contact")
        print("4 - Edit Contact")
        print("5 - Delete Contact")
        print("0 - Exit")

        choice = input("Choose an option: ")
        
        if choice == "1":
            add_contact()
        elif choice == "2":
            list_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            edit_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "0":
            print("Exiting Contact Manager. See you later!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    menu()
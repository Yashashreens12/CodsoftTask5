import json
import os

# Function to load contacts from a file
def load_contacts():
    try:
        with open("contacts.json", "r") as file:
            contacts = json.load(file)
        return contacts
    except FileNotFoundError:
        return []

# Function to save contacts to a file
def save_contacts(contacts):
    with open("contacts.json", "w") as file:
        json.dump(contacts, file, indent=2)

# Function to display the menu
def show_menu():
    print("\n===== Contact Management System =====")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

# Function to add a new contact
def add_contact(contacts):
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    address = input("Enter address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(contact)
    save_contacts(contacts)
    print("Contact added successfully!")

# Function to view all contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        print("\n===== Contact List =====")
        for i, contact in enumerate(contacts, start=1):
            print(f"{i}. {contact['name']} - {contact['phone']}")
        print("=" * 20)

# Function to search for a contact by name or phone number
def search_contact(contacts):
    query = input("Enter name or phone number to search: ").lower()
    results = []

    for contact in contacts:
        if query in contact["name"].lower() or query in contact["phone"]:
            results.append(contact)

    if not results:
        print("No matching contacts found.")
    else:
        view_contacts(results)

# Function to update contact details
def update_contact(contacts):
    view_contacts(contacts)
    index = int(input("Enter the number of the contact to update: ")) - 1

    if 0 <= index < len(contacts):
        contact = contacts[index]
        contact["phone"] = input("Enter new phone number: ")
        contact["email"] = input("Enter new email address: ")
        contact["address"] = input("Enter new address: ")
        save_contacts(contacts)
        print("Contact updated successfully!")
    else:
        print("Invalid contact number.")

# Function to delete a contact
def delete_contact(contacts):
    view_contacts(contacts)
    index = int(input("Enter the number of the contact to delete: ")) - 1

    if 0 <= index < len(contacts):
        deleted_contact = contacts.pop(index)
        save_contacts(contacts)
        print(f"{deleted_contact['name']} deleted successfully!")
    else:
        print("Invalid contact number.")

# Main function
def main():
    contacts = load_contacts()

    while True:
        show_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            print("Exiting the Contact Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()

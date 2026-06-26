contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")

    contact = {
        "name": name,
        "phone": phone
    }

    contacts.append(contact)
    print("Contact added successfully")


def view_contacts():
    if not contacts:
        print("No contacts available")
        return

    print("\n--- Contact List ---")

    for contact in contacts:
        print(f"""
Name : {contact['name']}
Phone: {contact['phone']}
--------------------
""")


def search_contact():
    name = input("Enter name: ").lower()

    found = False

    for contact in contacts:
        if name in contact["name"].lower():
            print(contact)
            found = True

    if not found:
        print("Contact not found")


while True:
    print("\n===== Contact Management =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        print("Program closed")
        break

    else:
        print("Invalid choice")

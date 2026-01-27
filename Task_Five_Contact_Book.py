contacts = []

def main():
    while True:
        print("\n--- CONTACT BOOK ---")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Choose an option (1-6): ")

        if choice == '1':
            name = input("Enter Name: ")
            phone = input("Enter Phone Number: ")
            email = input("Enter Email: ")
            address = input("Enter Address: ")
            contacts.append({"name": name, "phone": phone, "email": email, "address": address})
            print("Contact saved!")

        elif choice == '2':
            print("\n--- CONTACT LIST ---")
            if not contacts:
                print("No contacts found.")
            for i, c in enumerate(contacts, 1):
                print(f"{i}. {c['name']} | {c['phone']}|{c['email']} |{c['address']} ")

        elif choice == '3':
            query = input("Search by name or phone: ").lower()
            found = False
            for c in contacts:
                if query in c['name'].lower() or query in c['phone']:
                    print(f"\nFound: {c['name']} | {c['phone']} | {c['email']} | {c['address']}")
                    found = True
            if not found:
                print("No contact matching that search.")

        elif choice == '4':
            name_to_update = input("Enter the name of the contact to update: ").lower()
            for c in contacts:
                if c['name'].lower() == name_to_update:
                    print("Enter new details (leave blank to keep current):")
                    c['phone'] = input(f"New Phone [{c['phone']}]: ") or c['phone']
                    c['email'] = input(f"New Email [{c['email']}]: ") or c['email']
                    c['address'] = input(f"New Address [{c['address']}]: ") or c['address']
                    print("Update successful!")
                    break
            else:
                print("Contact not found.")

        elif choice == '5':
            name_to_delete = input("Enter name to delete: ").lower()
            for c in contacts:
                if c['name'].lower() == name_to_delete:
                    contacts.remove(c)
                    print("Contact deleted.")
                    break
            else:
                print("Contact not found.")

        elif choice == '6':
            print("Closing Contact Book.")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()




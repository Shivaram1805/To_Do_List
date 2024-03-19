class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print("Contact added successfully.")

    def view_contact_list(self):
        if not self.contacts:
            print("Contact list is empty.")
        else:
            print("\nContact List:")
            for idx, contact in enumerate(self.contacts, start=1):
                print(f"{idx}. Name: {contact.name}, Phone: {contact.phone_number}")

    def search_contact(self, search_term):
        results = []
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone_number:
                results.append(contact)
        return results

    def update_contact(self, index, new_contact):
        self.contacts[index] = new_contact
        print("Contact updated successfully.")

    def delete_contact(self, index):
        del self.contacts[index]
        print("Contact deleted successfully.")

def main():
    contact_book = ContactBook()

    while True:
        print("\n===== Contact Management System =====")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact = Contact(name, phone_number, email, address)
            contact_book.add_contact(contact)
        elif choice == "2":
            contact_book.view_contact_list()
        elif choice == "3":
            search_term = input("Enter name or phone number to search: ")
            search_results = contact_book.search_contact(search_term)
            if not search_results:
                print("No matching contacts found.")
            else:
                print("\nSearch Results:")
                for idx, contact in enumerate(search_results, start=1):
                    print(f"{idx}. Name: {contact.name}, Phone: {contact.phone_number}")
        elif choice == "4":
            contact_book.view_contact_list()
            try:
                index = int(input("Enter the index of the contact to update: ")) - 1
                if 0 <= index < len(contact_book.contacts):
                    name = input("Enter new name: ")
                    phone_number = input("Enter new phone number: ")
                    email = input("Enter new email: ")
                    address = input("Enter new address: ")
                    new_contact = Contact(name, phone_number, email, address)
                    contact_book.update_contact(index, new_contact)
                else:
                    print("Invalid index.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == "5":
            contact_book.view_contact_list()
            try:
                index = int(input("Enter the index of the contact to delete: ")) - 1
                if 0 <= index < len(contact_book.contacts):
                    contact_book.delete_contact(index)
                else:
                    print("Invalid index.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == "6":
            print("Thank you for using the Contact Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

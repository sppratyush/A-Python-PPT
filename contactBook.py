"""2.Contact Book 
Develop a contact book that can save, edit, and search contacts. 
Handle errors such as duplicate entries, empty fields, and wrong phone number 
format."""
class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone):
        if not name or not phone:
            raise ValueError("Name and phone number cannot be empty.")
        if not isinstance(name, str) or not isinstance(phone, str):
            raise TypeError("Name and phone number must be strings.")
        if name in self.contacts:
            raise KeyError("Contact already exists.")
        self.contacts[name] = phone

    def edit_contact(self, name, new_phone):
        if name not in self.contacts:
            raise KeyError("Contact does not exist.")
        if not isinstance(new_phone, str):
            raise TypeError("Phone number must be a string.")
        self.contacts[name] = new_phone

    def search_contact(self, name):
        if name not in self.contacts:
            raise KeyError("Contact does not exist.")
        return self.contacts[name]
# Example usage
if __name__ == "__main__":
    contact_book = ContactBook()
    try:
        contact_book.add_contact("Alice", "123-456-7890")
        contact_book.add_contact("Bob", "987-654-3210")
        print(contact_book.search_contact("Alice"))  # Output: 123-456-7890
        contact_book.edit_contact("Alice", "111-222-3333")
        print(contact_book.search_contact("Alice"))  # Output: 111-222-3333
        print(contact_book.search_contact("Charlie"))  # This will raise an exception
    except (ValueError, TypeError, KeyError) as e:
        print("Error:", e)
        
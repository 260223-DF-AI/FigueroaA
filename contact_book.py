# contact_book.py - Contact Book Application
# Starter code for e003-exercise-data-structures

"""
Contact Book Application
------------------------
A simple contact management system using Python data structures.

Data Structure:
- Each contact is a dictionary with: name, phone, email, category, created_at
- All contacts are stored in a list

Complete the TODO sections below to finish the application.
"""

from datetime import datetime

# =============================================================================
# Initialize Contact Book
# =============================================================================
contacts = []


# =============================================================================
# TODO: Task 1 - Create the Contact Book
# =============================================================================

def add_contact(contacts, name, phone, email, category):
    """
    Add a new contact to the contact book.
    
    Args:
        contacts: The list of all contacts
        name: Contact's full name
        phone: Contact's phone number
        email: Contact's email address
        category: One of: friend, family, work, other
    
    Returns:
        The created contact dictionary
    """
    # TODO: Create a contact dictionary with all fields

    # TODO: Add created_at timestamp using datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_contact = {"name": name,
               "phone": phone,
               "email": email,
               "category": category,
               "created_at": created_at}
    contacts.append(new_contact)
    # TODO: Append to contacts list

    # TODO: Return the new contact

    return new_contact
    


# =============================================================================
# TODO: Task 2 - Display Contacts
# =============================================================================

def display_all_contacts(contacts):
    """
    Display all contacts in a formatted table.
    
    Output format:
    =============================================
                CONTACT BOOK (X contacts)
    =============================================
    #  | Name            | Phone         | Category
    ---|-----------------|---------------|----------
    1  | Alice Johnson   | 555-123-4567  | friend
    ...
    """
    # TODO: Print header with contact count
    print("=" * 60)
    print(f"\t\t\tCONTACT BOOK ({len(contacts)})\t\t")
    print("=" * 60)
    # TODO: Print table headers
    print(f"# | \tName\t\t | Phone \t\t| Email \t\t | Category")
    print("-" * 2 + "|" + "-" * 22 + "|" + "-" * 22 + "|" + "-" * 24 + "|---------")
    # TODO: Loop through contacts and print each row
    for num in range(len(contacts)):
        print(str(num) + " |\t" + contacts[num].get('name') + 
              "\t | " + contacts[num].get('phone') + " \t| " +contacts[num].get("email") + " \t | " + 
              contacts[num].get('category'))
        
    # TODO: Print footer
    print("-" * 44)
    


def display_contact_details(contact):
    """
    Display detailed information for a single contact.
    
    Output format:
    --- Contact Details ---
    Name:     [name]
    Phone:    [phone]
    Email:    [email]
    Category: [category]
    Added:    [created_at]
    ------------------------
    """
    # TODO: Print formatted contact details
    print("--- Contact Details ---")
    print(f"Name: {contact["name"]}")
    print(f"Phone: {contact["phone"]}")
    print(f"Email: {contact["email"]}")
    print(f"Category: {contact["category"]}")
    print(f"Created at: {contact["created_at"]}")
    


# =============================================================================
# TODO: Task 3 - Search Functionality
# =============================================================================

def search_by_name(contacts, query):
    """
    Find contacts whose name contains the query string.
    Case-insensitive search.
    
    Returns:
        List of matching contacts
    """
    # TODO: Filter contacts where query is in name (case-insensitive)
    # Hint: Use list comprehension and .lower()
    # Apparently -1 is a truthy value in python, can't use string's find() function here
    return [contact for contact in contacts if query.lower() in contact["name"].lower()]
    


def filter_by_category(contacts, category):
    """
    Return all contacts in a specific category.
    
    Returns:
        List of contacts matching the category
    """
    # TODO: Filter contacts by category
    return [contact for contact in contacts if contact["category"] == category]
    pass


def find_by_phone(contacts, phone):
    """
    Find a contact by exact phone number.
    
    Returns:
        The contact dictionary if found, None otherwise
    """
    # TODO: Search for contact with matching phone
    return [contact for contact in contacts if contact["phone"] == phone]
    


# =============================================================================
# TODO: Task 4 - Update and Delete
# =============================================================================

def update_contact(contacts, phone, field, new_value):
    """
    Update a specific field of a contact.
    
    Args:
        contacts: The list of all contacts
        phone: Phone number to identify the contact
        field: The field to update (name, phone, email, or category)
        new_value: The new value for the field
    
    Returns:
        True if updated, False if contact not found
    """
    target_contact = ""
    is_success = False
    # TODO: Find contact by phone
    for contact in contacts:
        if contact["phone"] == phone:
            target_contact = contact
    # TODO: Update the specified field
    if (field == "name"):
        target_contact["name"] = new_value
        is_success = True
    elif (field == "phone"):
        target_contact["phone"] = new_value
        is_success = True
    elif (field == "email"):
        target_contact["email"] = new_value
        is_success = True
    elif (field == "category"):
        target_contact["category"] = new_value
        is_success = True

    # TODO: Return success/failure
    return is_success
    pass


def delete_contact(contacts, phone):
    """
    Delete a contact by phone number.
    
    Returns:
        True if deleted, False if not found
    """
    # TODO: Find and remove contact with matching phone
    is_deleted = False
    for contact in contacts:
        if contact["phone"] == phone:
            contacts.remove(contact)
            is_deleted = True

    return is_deleted



# =============================================================================
# TODO: Task 5 - Statistics
# =============================================================================

def display_statistics(contacts):
    """
    Display statistics about the contact book.
    
    Output:
    --- Contact Book Statistics ---
    Total Contacts: X
    By Category:
      - Friends: X
      - Family: X
      - Work: X
      - Other: X
    Most Recent: [name] (added [date])
    -------------------------------
    """
    # TODO: Count total contacts
    total_contacts = len(contacts)

    # TODO: Count contacts by category

    category = {"Friend" : 0,
                "Family" : 0,
                "Work" : 0,
                "Other" : 0}
    for contact in contacts:
        # the values inside category will be what is already there + 1. if value not found in contact dict, return 0 instead of None
        category[contact.get("category")] = category.get(contact["category"], 0) + 1
    
    print("--- Contact Book Statistics ---")
    print(f"Total Contacts: {total_contacts}")
    print("By Category: ")
    print(f"\t - Friends: {category.get("friend", 0)}")
    print(f"\t - Family: {category.get("family", 0)}")
    print(f"\t - Work: {category.get("work", 0)}")
    print(f"\t - Other: {category.get("other", 0)}")

    # TODO: Find most recently added contact
    recent_contact = ""
    recent_date = "0"
    for contact in contacts:
        if contact["created_at"] > recent_date:
            recent_contact = contact
    


# =============================================================================
# STRETCH GOAL: Interactive Menu
# =============================================================================

def display_menu():
    """Display the main menu."""
    print("\n========== CONTACT BOOK ==========")
    print("1. View all contacts")
    print("2. Add new contact")
    print("3. Search contacts")
    print("4. Update contact")
    print("5. Delete contact")
    print("6. View statistics")
    print("0. Exit")
    print("==================================")


def main():
    """Main function with interactive menu."""

    # TODO: Implement menu loop
    is_running = True
    while is_running:
        display_menu()
        selection = int(input("Choose an option: "))
        if selection <= 0:
            break
        if selection == 1:
            display_all_contacts(contacts)
        if selection == 2:
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            category = input("Enter category: ")
            print(add_contact(contacts, name, phone, email, category))
        if selection == 3:
            query = input("Enter a name to search for: ")
            print(search_by_name(contacts, query))
        if selection == 4:
            phone_query = input("Enter a phone number to search for: ")
            field_query = input("Enter from the following fields to update: \n" +
            "Name\n" + "Phone\n" + "Email\n"+ "Category").lower()
            new_value = input("Enter new value: ")
            update_contact(contacts, phone_query, field_query, new_value)
        if selection == 5:
            phone_query = input("Enter phone number to search for: ")
            is_deleted = delete_contact(contacts, phone_query)
            if is_deleted: 
                print(f"Contact with phone number: {phone_query} has been deleted.")
            else: print(f"No contact found with phone number: {phone_query}")
        if selection == 6:
            display_statistics(contacts)
        
        pass

    # Use while True and break on exit choice
    


# =============================================================================
# Test Code - Add sample data and test functions
# =============================================================================

if __name__ == "__main__":
    print("Contact Book Application")
    print("=" * 40)
    add_contact(contacts, "Alice Johnson", "555-123-4567", "alice@example.com", "friend")
    add_contact(contacts, "Micheal Jordon", "773-178-4622", "mjordan@aol.com", "other")
    add_contact(contacts, "Justin Bieber", "619-5027-8848", "jber323@yahoo.com", "other")
    add_contact(contacts, "Terry Rivers", "532-893-0217", "riverscrooz@mail.com", "family")
    add_contact(contacts, "Jane Doe", "500-153-4765", "JDoe@gmail.com", "work")
    # TODO: Add at least 5 sample contacts
    # add_contact(contacts, "Alice Johnson", "555-123-4567", "alice@example.com", "friend")
 
    # TODO: Test your functions
    # display_all_contacts(contacts)
    # results = search_by_name(contacts, "alice")
    # etc.

    
    """add_contact(contacts, "Alec Figueroa", "111-111-1111", "alec@revature.net", "family")
    display_all_contacts(contacts)
    print(search_by_name(contacts, "Jane Doe"))
    update_contact(contacts, "555-123-4567", "name", "Emilia Summers")
    display_all_contacts(contacts)
    delete_contact(contacts, "111-111-1111")
    display_all_contacts(contacts)
    display_statistics(contacts)
    display_all_contacts(contacts)"""
    # STRETCH: Uncomment to run interactive menu
    main()

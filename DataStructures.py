# A simple contacts application
#
# In this example, we introduce the concept of a global variable
# A global variable has scope over all of your program and can
# be accessed anywhere in your codebase. To create a global variable
# initialise it outside the scope of any function or class, or create it
# explicitly using the 'global' keyword.

def setupContacts():
    """The key is a person's name. The value in each case is
       a 3-tuple with (email,position,extension)"""
    return \
        {'jane': ('jane@acme.com', 'manager', 1546), \
         'rod': ('rod@acme.com', 'programmer', 8724), \
         'freddy': ('freddy@acme.com', 'support', 8524)}


def listAllContacts():
    """Iterate through the dictionary to show all contacts"""
    print("The names of all contacts:")
    for names in contacts.keys():
        print(f"{names}")


def addNewContact(name, email, position, extension):
    """Add a new key/value pairing to the dictionary"""
    contacts['name'] = (email, position, extension)


def searchByName(name):
    """Search for person by name and display contact details"""
    if name not in contacts.keys():
        print(f"Sorry, {name.title()} not in contacts.")
    else:
        v = contacts[name]  # need to unpack the values (tuples) of the keys (names).
        email, position, extension = v
        print(f"The details of {name}: Email: {email}, Position {position}, Extension: {extension}")


def printAllKeys():
    """Print all keys in the dictionary """
    for keys in contacts.keys():
        print(f"{keys}")


def main():
    global contacts  # Global variable
    contacts = setupContacts()

    listAllContacts()

    addNewContact('samira', 'samira@acme.com', 'legal', 6245)
    addNewContact('john', 'john@acme.com', 'maintenance', 6134)
    listAllContacts()

    searchByName('freddy')
    searchByName('samira')
    searchByName('david')  # Not in our contacts list ...

    # Print out all keys to confirm ...
    printAllKeys()


if __name__ == "__main__":
    main()

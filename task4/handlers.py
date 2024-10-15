from err_handlers import input_error

@input_error
def add_contact(args, contacts):
    name, phone = args
    if name in contacts:
        raise KeyError(name)
    contacts[name] = phone
    return f'Contact "{name}" added.'

@input_error
def change_contact(args, contacts):
    name, phone = args
    if not(name in contacts):
        raise KeyError(name)
    contacts[name] = phone
    return f'Contact "{name}" modified.'

@input_error
def get_phone(args, contacts):
    name = args[0]
    return f'{name}: {contacts[name]}'

def get_all_contacts(contacts):
    contact_strings = []
    for key, value in contacts.items():
        contact_strings.append(f'{key}: {value}')
    return '\n'.join(contact_strings)
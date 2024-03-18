def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    name, phone = args
    if name not in contacts:
        return "Contact not found."
    contacts[name] = phone
    return "Contact changed."

def phone_username(args, contacts):
    if args not in contacts:
        return "Contact not found."
    return contacts[args]

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change_username_phone":
            print(change_contact(args, contacts))
        elif command == "phone_username":
            print(phone_username(args, contacts))
        elif command == "all":
            print(contacts)
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()

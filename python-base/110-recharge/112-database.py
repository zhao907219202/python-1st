import sys, shelve


def store_person(db):
    """
    Query user for data and store it in the shelf object
    :param db:
    :return:
    """
    pid = input("Enter unique ID number: ")
    person = dict({})
    person['name'] = input("Enter name: ")
    person['age'] = input("Enter age: ")
    person['phone'] = input("Enter phone number: ")
    db[pid] = person


def lookup_person(db):
    """
    Query user for ID and desired field, and fetch the corresponding date from
    the shelf object
    :param db:
    :return:
    """
    pid = input("Enter ID number: ")
    field = input("What would you like to know? (name,age,phone) ")
    filed = field.strip().lower();
    print(filed.capitalize() + " : " + db[pid][field])


def print_help():
    print("The available commands are: ")
    print("store  : Stores information about a person")
    print("lookup : Looks up a person from ID number")
    print("quit   : Save changes and exit")
    print("?      : Prints this message")


def enter_command():
    cmd = input("Enter command (? for help): ")
    cmd = cmd.strip().lower()
    return cmd


def main():
    database = shelve.open("./file/database")
    try:
        while True:
            cmd = enter_command()
            if cmd == "store":
                store_person(database)
            elif cmd == "lookup":
                lookup_person(database)
            elif cmd == "?":
                print_help()
            elif cmd == "quit":
                return
    finally:
        database.close()


if __name__ == "__main__":
    main()

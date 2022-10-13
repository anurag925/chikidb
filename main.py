import logging
from pathlib import Path

from configs.banner import banner
from configs.logger import init_logger
from driver.database import Database


def main():
    try:
        setup_app()
        db = Database()
        db.connect()
        while True:
            user_input = input(">>> ").split(maxsplit=2)
            command = user_input[0].lower()
            if command == 'exit': 
                break
            elif command == 'show':
                show(db)
            elif command == 'set':
                set_data(db, user_input)
            elif command == 'get':
                get_data(db, user_input)
            elif command == 'search':
                search_data(db, user_input)
            elif command == 'help':
                help()
            elif command == 'commit':
                commit(db)
            else:
                print("please provide a proper command")
                print("enter 'help' to get all commands")
    except:
        print("some syntax error occured or invalid input")

def show(db):
    db.show()

def set_data(db, user_input):
    key = sub_command(user_input)
    if key is None:
        print("please provide a key to set data")
        return
    value = opt_command(user_input)
    if value is None:
        print("please provide a value to set data")
        return
    db.set_data(key, value)

def get_data(db, user_input):
    key = sub_command(user_input)
    if key is None:
        print("please provide a key to get data")
        return
    columns = opt_command(user_input)
    if columns:
        if columns[0] != '[' or columns[-1] != ']':
            print("columns to select must be an array enclosed withine '[]'")
            return
        columns = eval(columns)
    print(db.get_data(key, columns))

def search_data(db, user_input):
    element_to_search = sub_command(user_input)
    if element_to_search is None:
        print("please provide a value to search data")
        return
    value = opt_command(user_input)
    if value is not None:
        print("third value not allowed")
        return
    print(db.search(element_to_search))

def commit(db):
    db.commit()

def help():
    print('''
    Manual for the db
        get <key> (get the value of a key)
        get <key> ['column1', 'column2] (get the perticular column of iterable value)
        set <key> <value> (json, hash, array, touple, string, integer allowed)
        search <value> (search a perticular value in db)
        show (to show all the entries in the database)
        commit (commit changes for persistency)
    ''')
    

def sub_command(user_input):
    try:
        return user_input[1]
    except IndexError:
        return None

def opt_command(user_input):
    try:
        return user_input[2]
    except IndexError:
        return None
    
def setup_app():
    init_logger()
    print(banner())
    print("Welcome to chikidb inmemory verion")
    print("Write help to get all the commands and functionalities")

if __name__=="__main__":
    main()

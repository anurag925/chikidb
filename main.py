
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

if __name__=="__main__":
    main()

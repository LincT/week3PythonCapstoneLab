import sqlite3
import traceback

'''
Chainsaw Juggling Record Holder,	Country,	Number of catches
Ian Stewart,	Canada,	94
Aaron Gregg,	Canada,	88
Chad Taylor,	USA,	78
'''


def main():
    try:
        db = sqlite3.connect('my_first_db.db')  # Creates or opens database file
        table_string = "records (name text, country text, catches int)"
        table_name = table_string.split()[0]
        menu = {
            "create": 1,
            "read": 2,
            "update catches": 3,
            "update country": 4,
            "destroy": 5,
            "quit": 9
        }

        cur = db.cursor()  # Need a cursor object to perform operations

        # Create a table
        cur.execute('CREATE TABLE IF NOT EXISTS records (name text, country text, catches int)')

        # get input from user
        for kvp in menu:
            print(kvp.title() + ":".ljust(16-len(kvp), " ") + str(menu.get(kvp)))

        choice = 0
        while choice != menu.get("quit"):
            choice = int(input("please choose an option"))
            if choice == menu.get("create"):
                name = input("name to add: ")
                country = input("country of origin: ")
                catches = input("catches made: ")
                with db:
                    cur.execute('insert into records values (?, ?, ?)', (name.title(), country.upper(), catches))

            elif choice == menu.get("read"):
                if len(cur.execute('select * from records').fetchall()) >= 1:
                    for row in cur.execute('select * from records'):
                        print(row)
                else:
                    print("no records")
            elif choice == menu.get("update catches"):
                name = input("whose record do you wish to update?")
                catches = int(input("how many catches should be listed? "))
                with db:
                    if len(cur.execute('select name from records where name  = ?', (name.title(),)).fetchall())>0:
                        cur.execute('update records set catches = ? where name = ?', (catches, name.title()))
                print("WIP")
            elif choice == menu.get("update catches"):
                name = input("whose record do you wish to update?")
                country = input("what country should be listed? ")
                with db:
                    if len(cur.execute('select name from records where name  = ?',(name.title(),)).fetchall()) > 0:
                        cur.execute('update records set country = ? where name = ?', (country.upper(), name.title()))

            elif choice == menu.get("destroy"):
                name = input("who do you wish to delete? ")
                cur.execute('delete from records where name = ?', (name.title(),))

                print(name + "removed")
        print("Ending program")
    except ValueError as e:
        pass
    except Exception as e:
        print('error encountered:', e)
        traceback.print_exc()  # Displays a stack trace, useful for debugging
        # db.rollback()


if __name__ == '__main__':
    main()

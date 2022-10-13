Its a simple in memory database with persistency

its features include
1. Add a record

2. Delete a record or records by a key-value pair

3. Find all the records which contain a particular value

4. Should be able to select particular fields while finding a record(by default it should return all the fields)


Manual for the db
get <key> (get the value of a key)
get <key> ['column1', 'column2] (get the perticular column of iterable value)
set <key> <value> (json, hash, array, touple, string, integer allowed)
search <value> (search a perticular value in db)
show (to show all the entries in the database)
commit (commit changes for persistency)


Always remember "In Case of Fire must do commit"
without commit the changes will not be stored

To get Started
1) install pipenv (pip/pip3 install pipenv) 
2) pipenv shell
3) python main.py

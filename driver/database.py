import json
from pathlib import Path


class Database:

  file_path="/tmp/chikiDB.json"
  _instance = None
  db = None

  def __new__(cls):
    if cls._instance is None:
      cls._instance = super(Database, cls).__new__(cls)
    return cls._instance

  def connect(self):
    if Database.db is None:
      if not Path(Database.file_path).is_file():
        self.write_in_file({})
      Database.db = self.read_from_file()

  def show(self):
    print(Database.db)

  def set_data(self, key, value):
    try:
      data = eval(value)
      if type(data) in [int, dict, str, list, tuple]:
        Database.db[key] = data
      else:
        print("invalid data type or syntax")
    except:
      Database.db[key] = value

  def get_data(self, key, column):
    data = Database.db.get(key)
    if data:
      if column:
        if type(data) not in [dict, list, tuple]:
          print("cannot select value is not iterable")
          return data
        res = {}
        for i in column:
          try:
            res[i] = data[i]
          except:
            res[i] = None
        data = res
      return data
    return None

  def search(self, value):
    data = []
    try:
      value = eval(value)
    except:
      value = value
    for i, v in Database.db.items():
      if type(v) in [list, tuple]:
        for j in v:
          if j == value:
            data.append(i)
      elif type(v) == dict:
        for j in v.values():
          if j == value:
            data.append(i)
      elif v == value:
        data.append(i)
    return data

  def commit(self):
    self.write_in_file(Database.db)

  def read_from_file(self):
    file = open(Database.file_path, 'r')
    data = json.loads(file.read())
    file.close()
    return data

  def write_in_file(self, data):
    file = open(Database.file_path, 'w')
    file.write(json.dumps(data))
    file.close()
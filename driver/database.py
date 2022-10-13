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

  def read_from_file(self):
    file = open(Database.file_path, 'r')
    data = json.loads(file.read())
    file.close()
    return data

  def write_in_file(self, data):
    file = open(Database.file_path, 'w')
    file.write(json.dumps(data))
    file.close()
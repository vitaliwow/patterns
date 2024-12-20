"""Top-level modules should not depend on lower-level modules.
 Both should depend on abstractions.

 Good reference
 """

from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

class MySQLDatabase(Database):
    def connect(self):
        print("Connecting to MySQL")

class PostgreSQLDatabase(Database):
    def connect(self):
        print("Connecting to PostgreSQL")

class Application:
    def __init__(self, db: Database):
        self.db = db

    def run(self):
        self.db.connect()

db = MySQLDatabase()
app = Application(db)
app.run()

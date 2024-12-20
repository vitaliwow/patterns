"""Top-level modules should not depend on lower-level modules.
 Both should depend on abstractions.
 """

class MySQLDatabase:
    """Bad examole"""
    def connect(self):
        print("Connecting to MySQL")

class Application:
    def __init__(self):
        # App has a strong relation to MySQL
        self.db = MySQLDatabase()

    def run(self):
        self.db.connect()

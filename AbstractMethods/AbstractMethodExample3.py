from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def save(self, data):
        pass

class PostgresSQL(Database):
    def connect(self):
        print("Connected to PostgresSQL")

    def save(self, data):
        print(f"Saving {data} to postgresSQL database")

class MongoDB(Database):
    def connect(self):
        print("Connected to MongoDB")

    def save(self, data):
        print(f"Saving {data} to MongoDB")
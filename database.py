import psycopg2
from psycopg2 import Error
import sqlite3


class database:
    def __init__(self) -> None:
        """база данных"""
        try:
            # Вход в базу данных
            self.database_name = 'clinic'
            self.user_name = 'postgres'
            self.host = '31.129.109.154'
            self.password = '1*t&kvJlBCrc'
            self.connection = psycopg2.connect(
                    user=self.user_name,
                    password=self.password,
                    host=self.host,
                    database=self.database_name
            )
            self.createTable()
        except (Exception, Error) as error:
            print("Error while connecting to PostgreSQL", error)
            exit()

    def createTable(self) -> None:
        """Создание таблицы"""
        self.cursor = self.connection.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS recording (
                sequence_number SERIAL PRIMARY KEY,
                login TEXT,
                surname TEXT,
                middlename TEXT,
                fullname TEXT,
                date DATE
            )
        """)
        self.connection.commit()

        self.cursor = self.connection.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                sequence_number SERIAL PRIMARY KEY,
                login TEXT,
                password TEXT
            )
        """)
        self.connection.commit()    

    def selectAllLogin(self, nick: str) -> list:
        """Чтение всех логинов из базы данных"""
        self.cursor = self.connection.cursor()
        self.cursor.execute("""
            SELECT login FROM users WHERE login = %s
        """, (nick,))
        return self.cursor.fetchall()

    def writeNewLogin(self, nick: str, password: str) -> None:
        """Запись нового пользователя в базу данных"""
        self.cursor = self.connection.cursor()
        self.cursor.execute("""
            INSERT INTO users (login, password) VALUES (%s, %s)
        """, (nick, password,))
        self.connection.commit()
    
    def selectLoginPassword(self, login: str, password: str) -> bool:
        """Проверка на вход."""
        self.cursor = self.connection.cursor()
        self.cursor.execute("""
            SELECT login, password FROM users WHERE login = %s AND password = %s
        """, (login, password,))
        return self.cursor.fetchall()

class LocalDatabase:
    def __init__(self):
        self.connection = sqlite3.connect("local.sqlite")
        self.cursor = self.connection.cursor()
    
    def create_table(self):
        # Создаем таблицу, если она не существует
        database().selectAllLogin()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS joins (login TEXT, password TEXT)''')
        self.connection.commit()


if __name__ == "__main__":
    pass

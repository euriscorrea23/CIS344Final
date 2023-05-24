import mysql.connector
from mysql.connector import Error


class Database():
    def __init__(self,
                 host="127.0.0.1",
                 port="3306",
                 database="banks_portal",
                 user='root',
                 password='Ec062300'):

        self.host       = host
        self.port       = port
        self.database   = database
        self.user       = user
        self.password   = password
        self.connection = None
        self.cursor     = None
        self.connect()

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host         = self.host,
                port         = self.port,
                database     = self.database,
                user         = self.user,
                password     = self.password)
            
            if self.connection.is_connected():
                self.cursor = self.connection.cursor()
        except Error as e:
            print("Error while connecting to MySQL", e)

    def getAllAccounts(self):
        if self.connection.is_connected():
            query = "SELECT * FROM accounts"
            self.cursor.execute(query)
            records = self.cursor.fetchall()
            return records

    def getAllTransactions(self):
        if self.connection.is_connected():
            query = "SELECT * FROM Transactions"
            self.cursor.execute(query)
            records = self.cursor.fetchall()
            return records

    def deposit(self, accountID, amount):
        if self.connection.is_connected():
            self.cursor.callproc('deposit', [accountID, amount])
            self.connection.commit()

    def withdraw(self, accountID, amount):
        if self.connection.is_connected():
            self.cursor.callproc('withdraw', [accountID, amount])
            self.connection.commit()

    def addAccount(self, ownerName, owner_ssn, balance, status):
        if self.connection.is_connected():
            query = "INSERT INTO accounts (ownerName, owner_ssn, balance, account_status) VALUES (%s, %s, %s, %s)"
            self.cursor.execute(query, (ownerName, owner_ssn, balance, status))
            self.connection.commit()

    def accountTransactions(self, accountID):
        if self.connection.is_connected():
            self.cursor.callproc('accountTransactions', [accountID])
            results = self.cursor.stored_results().fetchall()
            return results

    def deleteAccount(self, accountID):
        if self.connection.is_connected():
            query = "DELETE FROM Transactions WHERE accountId = %s"
            self.cursor.execute(query, [accountID])
            query = "DELETE FROM accounts WHERE accountId = %s"
            self.cursor.execute(query, [accountID])
            self.connection.commit()

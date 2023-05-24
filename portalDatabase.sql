CREATE DATABASE banks_portal;
USE banks_portal;

CREATE TABLE accounts(
	accountId INT NOT NULL AUTO_INCREMENT,
    ownerName VARCHAR(45) NOT NULL,
    owner_ssn INT NOT NULL,
    balance DECIMAL(10,2) DEFAULT 0.00,
    account_status VARCHAR(45),
    PRIMARY KEY (accountId)
);

CREATE TABLE IF NOT EXISTS Transactions (
    transactionId INT NOT NULL AUTO_INCREMENT,
    accountId INT NOT NULL,
    transactionType VARCHAR(45) NOT NULL,
    transactionAmount DECIMAL(10,2) NOT NULL,
    PRIMARY KEY (transactionId)
); 

INSERT INTO accounts (ownerName, owner_ssn, balance, account_status) VALUES
("Maria Jozef", 123456789, 10000.00, "active"),
("Linda Jones", 987654321, 2600.00, "inactive"),
("John McGrail", 222222222, 100.50, "active"),
("Patty Luna", 111111111, 509.75, "inactive");

INSERT INTO Transactions (accountId, transactionType, transactionAmount) VALUES
(1, "deposit", 650.98),
(3, "withdraw", 899.87),
(3, "deposit", 350.00);

DELIMITER //
CREATE PROCEDURE accountTransactions(IN accID INT)
BEGIN
    SELECT * FROM Transactions WHERE accountId = accID;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE deposit(IN accID INT, IN amount DECIMAL(10,2))
BEGIN
    UPDATE accounts SET balance = balance + amount WHERE accountId = accID;
    INSERT INTO Transactions (accountId, transactionType, transactionAmount) VALUES (accID, 'deposit', amount);
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE withdraw(IN accID INT, IN amount DECIMAL(10,2))
BEGIN
    UPDATE accounts SET balance = balance - amount WHERE accountId = accID;
    INSERT INTO Transactions (accountId, transactionType, transactionAmount) VALUES (accID, 'withdraw', amount);
END //
DELIMITER ;

from datetime import datetime
import hashlib
import random
import string
import time
import mysql.connector
from tkinter import messagebox
from decimal import Decimal

def getCurrentDate():
    current_datetime = datetime.now()
    current_month = current_datetime.month
    current_date = current_datetime.day
    current_year = current_datetime.year
    return f"{current_year}-{current_month}-{current_date}"
    
def getCurrentTime():
    current_time = datetime.now().time()
    return f"{current_time.strftime('%H:%M:%S')}"
    
def generateHash(number):
    return hashlib.sha256(str(number).encode()).hexdigest()

def genrateAccountNumber():
    random_number = random.randint(10**19, (10**20)-1)
    return random_number

def generateIFSCCode():

    letters_and_digits = string.ascii_uppercase + string.digits + string.digits + string.digits
    ifsc = 'BOI' 
    
    for _ in range(8):
        ifsc += random.choice(letters_and_digits)
        
    return ifsc



# ALL DATABASE OPERATIONS        
def createConnection(db_name):
    
    connection= mysql.connector.connect(
            
            host="localhost",
            user= "root",
            password= "root",
            database= db_name
        )
    
    
    cursor= connection.cursor()
    
    return connection,cursor

def createAccountInDB(name, acctype, balance ,pin, accNo= genrateAccountNumber(), ifsc= generateIFSCCode()):
    accNo= genrateAccountNumber()
    ifsc= generateIFSCCode()
    
    connection,cursor= createConnection("bank")
    query= f"insert into accounts values ({accNo},'{ifsc}','{name}','{acctype}',{balance},'{generateHash(pin)}' )"

    updatePassbook(accNo,"NULL",balance,balance)    
    cursor.execute(query)

    connection.commit()


def getAllAccountsInDB():
    connection,cursor= createConnection("bank")
    
    query= "select * from accounts"
        
    cursor.execute(query)
    rows= cursor.fetchall()

    connection.close()
    cursor.close()
    return rows


def checkForValidAccount(accNo):
    connection,cursor= createConnection("bank")
    
    query= f"select pin,balance from accounts where accNo= {accNo}"
    
    cursor.execute(query)
    data= cursor.fetchone()

    connection.close()
    cursor.close() 
    
    if data:
        return data
    
    else:
        messagebox.showerror("Error", "INVALID ACCOUNT NUMBER")
        return False

def updateBalance(money,accNo):
    connection,cursor= createConnection("bank")
    
    query= f"UPDATE accounts SET balance={money} WHERE accNo={accNo}"
    cursor.execute(query)

    connection.commit()
    connection.close()
    cursor.close()    

       
def deleteAccountInDB(accNo):
    connection,cursor= createConnection("bank")
    query= f"DELETE FROM accounts WHERE accNo={accNo}"
    cursor.execute(query)

    connection.commit()
    connection.close()
    cursor.close()

def modifyAccount(accNo,acctype,name):
    connection,cursor= createConnection("bank")
    query= f"UPDATE accounts SET acctype='{acctype}',name='{name}' WHERE accNo={accNo}"
    
    cursor.execute(query)
    connection.commit()
        
    cursor.close()
    connection.close()


def getAccount(accNo):
    connection,cursor= createConnection("bank")
    
    query= f"select * from accounts where accNo={accNo}"
        
    cursor.execute(query)
    data= cursor.fetchone()
    
    cursor.close()
    connection.close()

    return data

def updatePassbook(accNo,withdraw,deposite,balance,date= getCurrentDate(),time= getCurrentTime()):
    connection,cursor= createConnection("bank")
    query= f"insert into passbook values ({accNo},'{date}','{time}',{withdraw},{deposite},{balance})"
    
    cursor.execute(query)
    connection.commit()
    
    cursor.close()
    connection.close()


def getPassbook(accNo):
    
    connection,cursor= createConnection("bank")
    query= f"select * from passbook where accNo= {accNo} order by time,date"
    
    cursor.execute(query)
    data= cursor.fetchall() 
    
    cursor.close()
    connection.close()

    return data
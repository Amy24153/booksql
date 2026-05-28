#DOCSTRING - AMY HUANG - LIBRARY DATABASE APPLICATION
#IMPORTS
import sqlite3

#CONTANTS AND VARIABLES
DATABASE = 'books.db'

#FUNCTIONS
def print_all_books():
    '''print all the books nicely'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = 'SELECT * FROM book;'
    cursor.execute(sql)
    results = cursor.fetchall()

#PRINTING THE BOOKS IN A NICE FORMAT
    print("Book ID  | Title                                         | Author                      | Issue Date | Return Date | Status    | Borrower")
    print("-" * 145)
    for row in results:
         print(f"{row[0]:<8} | {row[1]:<45} | {row[2]:<27} | {row[3]:<10} | {row[4]:<11} | {row[5]:<9} | {row[6]}")
#PRINTING PERSON TABLE
    print("\nUser ID | First Name          | Last Name            |City        ")
    print("-" * 50)
    sql = 'SELECT * FROM person;'
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        print(f"{row[0]:<6} | {row[1]:<20} | {row[2]:<20} | {row[3]:<12}")
    db.close()
#MAIN CODE
def add_person(): 
    '''Add a new person/borrower record into the person table'''
#CONNECT TO THE DATABASE
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()

    #GET USER INFORMATION
    user_id = int(input("Enter user ID: ")) #INTEGER INPUT FOR USER ID TO MATCH THE DATABSE
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    city = input("Enter city: ")


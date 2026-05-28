#DOCSTRING - AMY HUANG - LIBRARY DATABASE APPLICATION
#IMPORTS
import sqlite3

#CONTANTS AND VARIABLES
DATABASE = 'books.db'

#FUNCTIONS
def print_all_books(): #CREATE A FUNCTION TO PRINT ALL BOOKS IN THE DATABASE
    '''print all the books nicely'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor() #ACTS AS A BRIDGE BETWEEN YOUR PYTHON CODE AND THE DATABASE
    sql = 'SELECT * FROM book;'
    cursor.execute(sql) #SEND AND RUN SQL COMMANDS AGAIN A DATABASE 
    results = cursor.fetchall() #FETCH ALL THE RESULTS OF THE QUERY AND STORE THEM IN A VARIABLE CALLED RESULTS - THIS WILL BE A LIST OF TUPLES, WHERE EACH TUPLE REPRESENTS A ROW IN THE BOOK TABLE

#PRINTING THE BOOKS IN A NICE FORMAT
    print("Book ID  | Title                                         | Author                      | Issue Date | Return Date | Status    | Borrower")
    print("-" * 145)
    for row in results:
         print(f"{row[0]:<8} | {row[1]:<45} | {row[2]:<27} | {row[3]:<10} | {row[4]:<11} | {row[5]:<9} | {row[6]}")
#PRINTING PERSON TABLE
    print("\nUser ID | First Name          | Last Name            |City        ")
    print("-" * 50) #PRINT A SEPARATOR LINE
    sql = 'SELECT * FROM person;'
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        print(f"{row[0]:<6} | {row[1]:<20} | {row[2]:<20} | {row[3]:<12}")
    db.close() #CLOSE THE DATABASE CONNECTION TO FREE UP RESOURCES AND PREVENT POTENTIAL ISSUES WITH TOO MANY OPEN CONNECTIONS

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

    #INSERT THE NEW PERSON INTO THE DATABASE USING A PARAMETERIZED QUERY TO PREVENT SQL INJECTION - A PARAMETERIZED QUERY IS A WAY TO WRITE DATABASE QUERIES THAT USES 'PLACEHOLDERS' INSTEAD OF ACTUAL DATA
    #'?' IS A PLACEHOLDER THAT WILL BE REPLACED WITH THE ACTUAL DATA WHEN THE QUERY IS EXECUTED
    sql = 'INSERT INTO person VALUES (?, ?, ?, ?);'
    cursor.execute(sql, (user_id, first_name, last_name, city))

    db.commit() #COMMIT THE CHANGES TO THE DATABASE TO MAKE SURE THE NEW PERSON IS SAVED
    print("Person added successfully.")
    db.close() #CLOSE THE DATABASE CONNECTION

def add_book():
    '''Add a new book record into the book table with default status of available'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()

    #GET BOOK INFORMATION
    book_id = int(input("Enter book ID: ")) #INTEGER INPUT FOR BOOK ID TO MATCH THE DATABASE
    title = input("Enter book title: ")
    author = input("Enter author name: ")

    #INSERT THE NEW BOOK INTO THE DATABASE - ISSUE DATE, RETURN DATE, STATUS, ARE SET TO DEFAULT VALUES (NULL OR 'available')
    #THE SQL QUERY USES PLACEHOLDERS FOR THE BOOK INFORMATION, AND THE STATUS IS SET TO 'available' BY DEFAULT
    sql = 'INSERT INTO book (book_id, title, author, issue_date, status) VALUES (?, ?, ?, ?, ?);'
    cursor.execute(sql, (book_id, title, author, 'available'))
    
    db.commit()
    print("Book added successfully.")
    db.close()

def issue_book():
    '''Issue an existing book to a registered user by updating its record'''

    # Connect to the database
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()

    # Collect the book and borrower details from the user
    book_id     = int(input("Book ID: "))
    user_id     = int(input("User ID: "))
    issue_date  = input("Issue Date (DD/MM/YYYY): ")
    return_date = input("Return Date (DD/MM/YYYY): ")

    #UPDATE THE BOOK RECORD TO REFLECT THE ISSUE - SET THE STATUS
    sql = "UPDATE book SET user_id=?, issue_date=?, return_date=?, status='issued' WHERE book_id=?;"
    cursor.execute(sql, (user_id, issue_date, return_date, book_id))

    db.commit()  # Save changes to the database
    print("Book issued successfully.")
    db.close()

def return_book():
    '''Return a book by clearing its borrower info and marking it as returned'''
    #CONNECT TO THE DATABASE
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()

    #GET THE BOOK ID TO BE RETURNED
    book_id = int(input("Enter book ID to return: "))
    #Clear the borrower link and dates, then update status to 'returned'
    # NULL means no value — the book no longer has an active borrower or dates
    sql = "UPDATE book SET user_id=NULL, issue_date=NULL, return_date=NULL, status='returned' WHERE book_id=?;"
    cursor.execute(sql, (book_id,))
    #Note: (book_id,) is a tuple with one item — the trailing comma is required
    # without it Python treats it as just a variable, not a tuple
    db.commit()  # Save changes to the database
    print("Book returned successfully.")
    db.close()  # Close the database connection
    
#!/usr/bin/env python3
# Exercise 4

################################################################################

#Using the lecture notes as a guide, write functions that will show the structure 
#of a database table chosen by you, the user 
#(i.e. one fuction might rely on the output from the other).

################################################################################


#===================================
#changes made from the original functions:
# 1. import getpass and get the input from the user at runtime
# 2. call the function to display tables and get the table choice
# 3. modify the try except into a second function
#    which takes password and table name
# 4. exit the second function if no table is selected
# 5. remove the hard coded table name blasthits
# 6. call the second function, passing the table name returned by the first
# 7. remove the duplicate SHOW TABLES from the second function
# 8. change the database to my username (remove _exercises)
# 9. adjust formatting of imports to separate standard imports from 3rd party
#    this was directed by the linter
#===================================

import os
from getpass import getpass

import MySQLdb


def get_table_choice(host, user, password, database):
# These are the Python comment lines in our function
    """
    Queries the database for all available tables and prompts the user to select one.
    Returns the string name of the chosen table, or None if exit/error.
    """
    connection = None
    try:
        connection = MySQLdb.connect(
            host=host,
            user=user,
            passwd=password,
            db=database
        )
        cursor = connection.cursor()
        # Fetch all tables in the database
        cursor.execute("SHOW TABLES")
        tables = [row[0] for row in cursor.fetchall()]
        # Error trap...        
        if not tables:
            print("No tables found in this database.")
            return None
        # Display the tables as a numbered menu
        print("\nAvailable Tables:")
        print("-" * 30)
        for index, table_name in enumerate(tables, 1):
            print(f"[{index}] {table_name}")
        print("-" * 30)
        # Get the user to choose one!
        while True:
            try:
                choice = input(f"Pick a table number (1-{len(tables)}) or 'q' to quit: ").strip()
                if choice.lower() == 'q':
                    return None
                
                choice_num = int(choice)
                if 1 <= choice_num <= len(tables):
                    return tables[choice_num - 1]
                else:
                    print(f"Invalid number. Please choose between 1 and {len(tables)}.")
            except ValueError:
                print("Please enter a valid number or 'q'.")
    except MySQLdb.Error as e:
        print(f"Database error while fetching tables: {e}")
        return None
    finally:
        if connection and connection.open:
            cursor.close()
            connection.close()

password = getpass("Enter your MySQL password: ")

table_name = get_table_choice(
    "localhost",
    "s1306053",
    password,
    "s1306053"
)

if table_name is None:
    raise SystemExit



def get_table_structure(password=password, table_name=table_name):
    try:
        connection = MySQLdb.connect(
            host="127.0.0.1",      
            user=os.environ["USER"],
            passwd=password,
            db=os.environ["USER"]
        )
    # Check our connection works
        cursor = connection.cursor()
        cursor.execute("SELECT VERSION()")
        db_version = cursor.fetchone()
        print(f"Database version: {db_version[0]}")
        # Let's check a specific table - take the table name from the earlier function call
        cursor.execute(f"DESCRIBE {table_name}")
        # Get the query outputs
        columns = cursor.fetchall()
        # Set up a display
        print(f"\nStructure for table: '{table_name}'")
        print("~" * 60)
        print(f"{'Field Name':<20} | {'Type':<15} | {'Null Allowed?':<12} | {'Key'}")
        print("~" * 60)
        # Populate the display
        for col in columns:
            print(f"{col[0]:<20} | {col[1]:<15} | {col[2]:<13} | {col[3]}")
            print("-" * 60)
    except MySQLdb.Error as e:
        print(f"Error: {e}")
    finally:
        if 'connection' in locals():
            cursor.close()
            connection.close()
    

get_table_structure(password, table_name)



















# import sqlite3

# # Connect to the database file
# conn = sqlite3.connect('main.db')

# # Create a cursor object to execute SQL commands
# cursor = conn.cursor()

# # Execute the query to get a list of all tables in the database
# cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

# # Fetch all the table names from the query result
# tables = cursor.fetchall()

# # Print the table names
# for table in tables:
#     print(table[0])

# # Close the cursor and the connection
# cursor.close()
# conn.close()

# --------------------------------------------------------------------------------------------------------------------------------------------

import sqlite3

# Connect to the database file
conn = sqlite3.connect('main.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Execute the query to get a list of all tables in the database
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

# Fetch all the table names from the query result
tables = cursor.fetchall()

# Iterate over the table names
for table in tables:
    table_name = table[0]
    print("Table:", table_name)

    # Execute a query to fetch all entries from the current table
    cursor.execute(f"SELECT * FROM {table_name};")

    # Fetch all the entries from the query result
    entries = cursor.fetchall()

    # Get the column names of the table
    cursor.execute(f"PRAGMA table_info({table_name});")
    columns = cursor.fetchall()
    column_names = [column[1] for column in columns]

    # Print the column names
    print("Attributes:", column_names)

    # Print the entries
    for entry in entries:
        print(entry)

    print()  # Add a newline for separation

# Close the cursor and the connection
cursor.close()
conn.close()

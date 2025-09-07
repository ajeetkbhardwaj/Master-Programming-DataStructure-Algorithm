"""
Structured Query Language(SQL) is a standard language for managing and manipulating relational databases.
SQLite is a self-contained, serverless and zero-configuration database engine that is widely used for embedded databaase systems.
The SQL and SQLite,we learn about creating databases, tables and performing various SQL operations.

"""
#%% dependencies
import sqlite3

#%% connect to an SQLite database
connection = sqlite3.connect("example.db")
connection

#%%
cursor = connection.cursor()

#%%
cursor.execute(
    """
    Create Table If Not Exists employees(
    id Integer Primary Key,
    name Text Not Null,
    age Integer,
    department text
    )
    """
)

#%% commit the changes
connection.commit()

#%%
cursor.execute(
    """
    Select * from employees
    """
)

#%%
# Insert the data in sqlite table
cursor.execute('''
Insert Into employees(name,age,department)
               values('Krish',32,'Data Scientist')

''')

cursor.execute('''
INSERT INTO employees (name, age, department)
VALUES ('Bob', 25, 'Engineering')
''')

cursor.execute('''
INSERT INTO employees (name, age, department)
VALUES ('Charlie', 35, 'Finance')
''')

## commi the changes
connection.commit()

#%% 
# Query the data from the table
cursor.execute('Select * from employees')
rows=cursor.fetchall()

## print the queried data

for row in rows:
    print(row)
    
#%% 
## Delete the data from the table
cursor.execute('''
Delete from employees
               where name ='Bob'
''')

connection.commit()

#%% 
## Query the data from the table
cursor.execute('Select * from employees')
rows=cursor.fetchall()

## print the queried data

for row in rows:
    print(row)
    
#%%
## Working Wwith Sales Data
# Connect to an SQLite database
connection = sqlite3.connect('sales_data.db')
cursor = connection.cursor()

# Create a table for sales data
cursor.execute('''
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY,
    date TEXT NOT NULL,
    product TEXT NOT NULL,
    sales INTEGER,
    region TEXT
)
''')

# Insert data into the sales table
sales_data = [
    ('2023-01-01', 'Product1', 100, 'North'),
    ('2023-01-02', 'Product2', 200, 'South'),
    ('2023-01-03', 'Product1', 150, 'East'),
    ('2023-01-04', 'Product3', 250, 'West'),
    ('2023-01-05', 'Product2', 300, 'North')
]

cursor.executemany('''
Insert into sales(date,product,sales,region)
                   values(?,?,?,?)
''',sales_data)

connection.commit()

#%% 

# Query data from the sales table
cursor.execute('SELECT * FROM sales')
rows = cursor.fetchall()

# Print the queried data
for row in rows:
    print(row)
    
#%% 

## close the connection
connection.close()

# Query data from the sales table
cursor.execute('SELECT * FROM sales')
rows = cursor.fetchall()

# Print the queried data
for row in rows:
    print(row)
# importing sqlite3 module in init_db.py file.
import sqlite3

# opens a connection to the database file named ideas.db.  
connect = sqlite3.connect('ideas.db') 
# creates a cursor object that sets up a pipeline to execute SQL commands. 
cursor = connect.cursor()

# Creates the ideas table in the database if it does not already exist. 
cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS ideas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL, 
        description TEXT NOT NULL CHECK (length(description) BETWEEN 10 AND 50000),
        tags TEXT NOT NULL CHECK (tags IN ('Hackathon', 'Startup', 'Innovation', 'All')),
        author TEXT NOT NULL,
        difficulty TEXT NOT NULL CHECK (difficulty IN ('Senior', 'Junior', 'Intern', 'All')),
        likes INTEGER NOT NULL DEFAULT 0,
        created_time TEXT DEFAULT CURRENT_TIMESTAMP 
    )
""")



connect.commit()
connect.close()
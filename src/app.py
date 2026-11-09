# importing flask module in app.py file. 
from flask import Flask 
import sqlite3

# Creates the Flask application object named app.  
app = Flask(__name__)

# Maps the root URL to the hello() function.  
@app.route("/") 
# Returns the string "Hello, World" when the the root URL is accessed.
def home(): 
    return "Welecome to IDEATOON!"

def get_connection():
    # creates connection to the database file ideas.db. 
    connection = sqlite3.connect('ideas.db')
    # sets the row factory to sqlite3.Row. Allows to access columns by their names instead of python tuples (idexes).
    connection.row_factory = sqlite3.Row 
    # closes connection after executing a query to prevent leaks.
    return connection

@app.route("/ideas")
def list_ideas():
    # establishes a connection to the database using the get_connection() function.
    connection = get_connection()
    # maybe use SELECT * FROM ideas b/c all the columns could be used
    rows = connection.execute("SELECT * FROM ideas").fetchall()
    # closes the connection to the database after executing the fetchall of the SELECT columns query.
    connection.close()
    # checks if there are no rows returned from the database query.  
    if not rows:
        return "No ideas found."
    # returns the rows feteched from the database as a response.
    return ", ".join([f"{row['id']} - {row['title']} - {row['description']} - {row['tags']} - {row['author']} - {row['difficulty']} - {row['likes']} - {row['created_time']}" for row in rows])

# Ensures the application runs when app.py is executed. 
if __name__ == "__main__":
    # app.run()
    # runs the app in debug mode, detecting errors. 
    app.run(debug=True) 
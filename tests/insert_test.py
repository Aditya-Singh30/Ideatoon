import sqlite3

connect = sqlite3.connect('ideas.db')
cursor = connect.cursor()

cursor.execute(
    "INSERT INTO ideas (title, description, tags, author, difficulty) VALUES (?, ?, ?, ?, ?)",
    ("My Idea", "This is my cool ideas of a project for a Hackathon.", "Hackathon", "Aditya Singh", "Senior")
)

connect.commit()
connect.close()
# importing flask module in app.py file. 
from flask import Flask

# Creates the Flask application object named app.  
app = Flask(__name__)

# Maps the root URL to the hello() function.  
@app.route("/")
#returns the string "Hello, World" when the the root URL is accessed.
def hello():
    return "Hello, World!"

# Ensures the application runs when app.py is executed. 
if __name__ == "__main__":
    #app.run()
    #runs the app in debug mode, detecting errors. 
    app.run(debug=True) 
from flask import Flask , render_template
"""
It create an instance of the Flask class,
which will be your WSGI (Web Server Gateway Interface) application.
The first argument is the name of the application's module or package.
This is needed so that Flask knows where to look for resources such as templates and static files.
"""

## WSGI Application
app = Flask(__name__)

@app.route("/")# This is a decorator that tells Flask what URL should trigger the function that follows it.
def Welcome():
  return "<html><H1>Welcome to this best Flask Course.This Should be an amazing course. </H1></html>" # This is the response that will be sent to the client when they access the root URL ("/").

@app.route("/index")
def index():
  return render_template("index.html") # This is the response that will be sent to the client when they access the "/index" URL. It renders the "index.html" template.

@app.route("/about")
def about():
  return render_template("about.html") # This is the response that will be sent to the client when they access the "/about" URL. It renders the "about.html" template.

@app.route("/contact")
def contact():
  return render_template("contact.html") # This is the response that will be sent to the client when they access the "/contact" URL. It renders the "contact.html" template.


if __name__ == '__main__':
  app.run(debug=True) # This line checks if the script is being run directly (as the main program) and, if so, it starts the Flask development server. The debug=True argument enables debug mode, which provides helpful error messages and automatically reloads the server when code changes are detected.
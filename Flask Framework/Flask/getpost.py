from flask import Flask , render_template , request
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

@app.route("/index",methods=['GET'])
def index():
  return render_template("index.html") # This is the response that will be sent to the client when they access the "/index" URL. It renders the "index.html" template.

@app.route("/about")
def about():
  return render_template("about.html") # This is the response that will be sent to the client when they access the "/about" URL. It renders the "about.html" template.

@app.route("/contact")
def contact():
  return render_template("contact.html") # This is the response that will be sent to the client when they access the "/contact" URL. It renders the "contact.html" template.

@app.route('/form',methods=['GET','POST'])
def form():
  if request.method == 'POST': # This checks if the HTTP method of the request is POST, which indicates that the form has been submitted.
    name = request.form['name'] # This retrieves the value of the form field named 'name' from the submitted form data.
    email = request.form['email'] # This retrieves the value of the form field named 'email' from the submitted form data.
    return f"<h1>Name: {name}, Email: {email}</h1>" # This returns a string that includes the values of the 'name' and 'email' fields, which will be displayed to the user after they submit the form.
  return render_template('form.html') # This is the response that will be sent to the client when they access the "/form" URL. It renders the "form.html" template.

if __name__ == '__main__':
  app.run(debug=True) # This line checks if the script is being run directly (as the main program) and, if so, it starts the Flask development server. The debug=True argument enables debug mode, which provides helpful error messages and automatically reloads the server when code changes are detected.
## Building Url Dyanamically
## Variable Rules
## Jinja 2 Template Engine 
'''In Flask, you can build URLs dynamically using the `url_for` function provided by the Jinja2 templating engine. This function allows you to generate URLs for your routes based on the endpoint name and any arguments required by the route.'''


# Jinja 2 Template Engine 
"""
{{ }} : Experssions to print output in html
{%.....%} : Conditions , for loops 
{#...#} : This is commets
"""

from flask import Flask , render_template , request


## WSGI Application
app = Flask(__name__)

@app.route("/")
def Welcome():
  return "<html><H1>Welcome to this best Flask Course.This Should be an amazing course. </H1></html>" 

@app.route("/index",methods=['GET'])
def index():
  return render_template("index.html") 

@app.route("/about")
def about():
  return render_template("about.html") 

@app.route("/contact")
def contact():
  return render_template("contact.html") 

@app.route('/form',methods=['GET','POST'])
def form():
  if request.method == 'POST': 
    name = request.form['name'] 
    email = request.form['email'] 
    return f"<h1>Name: {name}, Email: {email}</h1>" 
  return render_template('form.html') 

#Variable Rules
@app.route('/success/<int:score>')
def success(score):
  res=""
  if score>=50:
    res="PASSED"
  else:
    res="FAILED"
  return render_template('result.html',results=res)


#Variable Rules
@app.route('/successres/<int:score>')
def successres(score):
  res=""
  if score>=50:
    res="PASSED"
  else:
    res="FAILED"

  exp = {'Score':score , 'res':res}

  return render_template('result1.html',results=exp)


# if condition
@app.route('/successif/<int:score>')
def successif(score):
  res=""
  if score>=50:
    res="PASSED"
  else:
    res="FAILED"
  return render_template('result.html',results=res)



if __name__ == '__main__':
  app.run(debug=True) 
from flask import Flask,render_template
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/form', methods=['GET', 'POST'])  # decorator
def form():
    if request.method == 'POST':
        name = request.form['name']
        return f'Hello {name}!'
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)

'''
creates an innstance of the Flask class,
which will be our WSGI application.
'''
### WSGI: Web Server Gateway Interface
app = Flask(__name__)

@app.route('/')### decorator
def welcome():
    return "<html><h1>Hello, World!--FLASH--flask prog successfull-what a wonderful day</h1></html>"


@app.route('/index',methods=['GET'])### decorator
def index():
    return render_template('index.html')

@app.route('/about')### decorator
def about():
    return render_template('about.html')

@app.route('/form', methods=['GET', 'POST'])  # decorator
def form():
    if request.method == 'POST':
        name = request.form['name']
        return f'Hello {name}!'
    return render_template('form.html')

@app.route('/submit', methods=['GET', 'POST'])  # decorator
def submit():
    if request.method == 'POST':
        name = request.form['name']
        return f'Hello {name}!'
    return render_template('form.html')

   
if __name__ == '__main__':
    app.run(debug=True)
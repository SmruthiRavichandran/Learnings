from flask import Flask,render_template
'''
creates an innstance of the Flask class,
which will be our WSGI application.
'''
### WSGI: Web Server Gateway Interface
app = Flask(__name__)

@app.route('/')### decorator
def welcome():
    return "<html><h1>Hello, World!--FLASH--flask prog successfull-what a wonderful day</h1></html>"


@app.route('/index')### decorator
def index():
    return render_template('index.html')

@app.route('/about')### decorator
def about():
    return render_template('.html')

if __name__ == '__main__':
    app.run(debug=True)
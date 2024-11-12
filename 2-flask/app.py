from flask import Flask
'''
creates an innstance of the Flask class,
which will be our WSGI application.
'''
### WSGI: Web Server Gateway Interface
app = Flask(__name__)

@app.route('/')### decorator
def index():
    return "<h1>Hello, World!--FLASH--flask prog successfull-what a wonderful day</h1>"
@app.route('/home')### decorator
def home():
    return "<h1>welcome to the home page</h1>"

if __name__ == '__main__':
    app.run(debug=True)
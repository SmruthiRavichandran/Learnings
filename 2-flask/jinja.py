from flask import Flask, render_template, request

app = Flask(__name__)

# Home route
@app.route('/')  # decorator
def welcome():
    return "<h1>Hello, World!--FLASH--flask prog successful - what a wonderful day</h1>"

# Index route
@app.route('/index', methods=['GET', 'POST'])  # decorator
def index():
    return render_template('index.html')

# About route
@app.route('/about')  # decorator
def about():
    return render_template('about.html')

# Form route
@app.route('/form', methods=['GET', 'POST'])  # decorator
def form():
    if request.method == 'POST':
        name = request.form['name']
        return f'Hello {name}!'
    return render_template('form.html')

# Submit route (redirects to form page for POST requests)
@app.route('/submit', methods=['GET', 'POST'])  # decorator
def submit():
    if request.method == 'POST':
        name = request.form['name']
        return f'Hello {name}!'
    return render_template('form.html')

# Success route with variable rule
@app.route('/success/<score>')  # decorator
def success(score):
    #return "The person has passed and the score is: " + str(score)
    score=float(score)
    res=""
    if score>=50:
        res="PASS"
    else:
        res="FAIL"
    return render_template('results.html',result=res)

# Success route with variable rule

@app.route('/successresults/<score>')  # decorator
def successresults(score):
    #return "The person has passed and the score is: " + str(score)
    score=float(score)
    res=""
    if score>=50:
        res="PASS"
    else:
        res="FAIL"
        
    exp={'score':score,'res':res}   
    return render_template('resultsexp.html',result=exp)


# Success route with if conditionn

@app.route('/successif/<score>')  # decorator
def successif(score):
    score=int(score)
    #return "The person has passed and the score is: " + str(score)
    return render_template('resultsif.html',results=score)
    
    
if __name__ == '__main__':
    app.run(debug=True)

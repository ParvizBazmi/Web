from flask import Flask, render_template, request, url_for, redirect
import csv
app = Flask(__name__)
print(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/home')
def homeB():
    return render_template('index.html')


@app.route("/works")
def works():
    return render_template('works.html')

@app.route("/thankyou.html")
def thankyou():
    return render_template('thankyou.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

def write_to_file(data):
    with open('database.csv.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email},{subject},{message}')



@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_file(data)
        return redirect('/thankyou.html')
    else:
        return 'Uh oh! try again!'

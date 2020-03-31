from flask import Flask, render_template, request
import csv

app = Flask(__name__)


@app.route('/')
def my_home():
    return render_template('/index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_csv(data):
    with open('database.csv', mode='a') as database2:
        first_name = data['first_name']
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([first_name, email, subject, message])
        

def write_to_file(data):
    with open('database.txt', 'a') as database:
        first_name = data["first_name"]
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        database.write(f'\n{first_name}, {email}, {subject}, {message}')
        

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = dict(request.form)
        write_to_csv(data)
        return render_template('thank.html', name=data['first_name'])
    else:
        return 'something went wron. Try again!'
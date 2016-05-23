# encoding=utf-8
from flask import *
from wtforms import *

app = Flask(__name__)

@app.route('/')
def index():
    email_list = ['1@1.com', '2@2.com']
    email = request.form.get('email')
    password=request.form.get('password')
    if email in email_list:
        return render_template('test.html')
    else:
        return redirect('/login/')



@app.route('/login/')
def login():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

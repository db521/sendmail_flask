# coding=utf-8
from flask import *

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': U'函数里面的名字made'}  # fake user
    return render_template('index.html',user=user,title=u'函数里面的标题')



app.run(debug=True)

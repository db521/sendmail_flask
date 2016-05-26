# coding=utf-8
from flask import *

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': U'函数里面的名字made'}  # fake user
    posts = [
        {'author': {'nickname': u'你妹'},
         'body': u'说你妹的啥呢'},
        {
            'author': {'nickname': u'你妹妹'},
            'body': u'找你妹干啥'}
            ]
    return render_template('index.html', user=user, title=u'函数里面的标题', posts=posts)


app.run(debug=True)

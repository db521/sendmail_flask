# coding=utf-8

import flask.ext
from wtforms import StringField,SubmitField
import flask.ext


class NameForm():
    name=StringField(u'邮箱地址')
    secret=StringField(u'密码')
    submit=SubmitField(u'登录')


def loginin():
    #2个点，第一个使用邮箱账号登录
    #第二个是在邮箱地址列表里面

    pass


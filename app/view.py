
import sys

from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, helpers

DATABASE = '/tmp/flaskr.db'
ENV = 'development'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

print("__name__ is")
print(__name__)
print(type(__name__))
print(helpers.get_root_path(__name__))
print(sys.modules.get(__name__))


app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def show_entries():
    return render_template('index.html')


## todo add parameters here
@app.route('/play')
def play():
    print(request.args)
    x_pos = request.args.get('x_pos')

    y_pos = request.args.get('y_pos')

    print(request.url)

    print(x_pos , y_pos)
    return "helloworld"


if __name__ == '__main__':
    app.run()

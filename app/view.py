
import sys
import  json
from flask import Flask, request, render_template, helpers
from connect_four import fillBoard, player2, init, play, player1
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


class connect_4():

    def __init__(self):
        self.board = init(6, 7)

    def player2(self):
        return play(self.board, player2)

    def fillBoard(self, x, y, player):
        fillBoard(self.board, x, y, player)

    def reset(self):
        self.board = init(6, 7)


connectFour = connect_4()

@app.route('/')
def show_entries():
    connectFour.reset()
    return render_template('index.html')


@app.route('/play', methods=["POST", "GET"])
def play__():

    print(request.form)
    ## looks strane here
    x_pos = int(request.form["y"])
    y_pos = int(request.form["x"])

    print("x={}|y={}".format(x_pos, y_pos))

    connectFour.fillBoard(x_pos, y_pos, player1)
    r, c = connectFour.player2()
    d = {"row":c, "col":r}
    print(d)
    return json.dumps(d)


if __name__ == '__main__':
    app.run()

from flask import Flask, render_template, request
import AI

app = Flask(__name__)

white = []
black = []

@app.route('/')
def chessBoard():
  global white, black
  white = []
  black = []
  return render_template('main.html')

@app.route('/play')
def play():
  global white, black
  user_pos = int(request.args.get('id',''))
  if user_pos not in white and user_pos not in black:
    white.append(user_pos)
    AI_pos = AI.play(white, black)
    black.append(AI_pos)
    return str(AI_pos)
  else:
    return '-1'

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)

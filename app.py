import os 
from flask import Flask, request
from flask_cors import CORS
import chess
import chess.engine

application = Flask(__name__)
CORS(application)

@application.route('/')
def hello_world():
  return 'Hello, World!'

# POST /nextmove
# chessboard state as payload
@application.route('/nextmove', methods=['POST'])
def getNextMove():
  # # init engine
  engine = chess.engine.SimpleEngine.popen_uci("/usr/local/bin/stockfish")

  # get the payload
  req_data = request.data
  print(req_data.decode('utf-8'))

  board = chess.Board(req_data.decode('utf-8'))
  result = engine.play(board, chess.engine.Limit(time=0.100))
  engine.quit()

  return result.move.uci()

if __name__ == '__main__':
  application.run(host='0.0.0.0', debug=True, port=80)
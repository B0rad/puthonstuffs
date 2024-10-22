import pprint
import yaml
chessBoard = {'a8': ' ', 'b8': ' ', 'c8': ' ', 'd8': ' ', 'e8': ' ', 'f8': ' ', 'g8': ' ', 'h8': ' ',
              'a7': ' ', 'b7': ' ', 'c7': ' ', 'd7': ' ', 'e7': ' ', 'f7': ' ', 'g7': ' ', 'h7': ' ',
              'a6': ' ', 'b6': ' ', 'c6': ' ', 'd6': ' ', 'e6': ' ', 'f6': ' ', 'g6': ' ', 'h6': ' ',
			  'a5': ' ', 'b5': ' ', 'c5': ' ', 'd5': ' ', 'e5': ' ', 'f5': ' ', 'g5': ' ', 'h5': ' ',
			  'a4': ' ', 'b4': ' ', 'c4': ' ', 'd4': ' ', 'e4': ' ', 'f4': ' ', 'g4': ' ', 'h4': ' ',
			  'a3': ' ', 'b3': ' ', 'c3': ' ', 'd3': ' ', 'e3': ' ', 'f3': ' ', 'g3': ' ', 'h3': ' ',
			  'a2': ' ', 'b2': ' ', 'c2': ' ', 'd2': ' ', 'e2': ' ', 'f2': ' ', 'g2': ' ', 'h2': ' ',
			  'a1': ' ', 'b1': ' ', 'c1': ' ', 'd1': ' ', 'e1': ' ', 'f1': ' ', 'g1': ' ', 'h1': ' '}


chessPieces= {player1: {'wPawn': 8, 'wBishop': 2, 'wKnight': 2, 'wRook': 2, 'wQueen': 1, 'wKing': 1 },
			  player2: {'bPawn': 8, 'bBishop': 2, 'bKnight': 2, 'bRook': 2, 'bQueen': 1, 'bKing': 1}}

# def printChessBoard(chessBoard):
#     print(chessBoard


def playerPieces(pieceType, amount):
    numberOfPieces = 0
    for k, v in pieceType.items():
        numberOfPieces = numberOfPieces + v.get(amount,0)
    return numberOfPieces

# print("Players have this many pieces left: ")
# print('Player 1: ', chessPieces.get('player1').get('Pawn'))
# print("Player 1 has this many Pawns: ",chessPieces['player1']['Pawn'])
# pprint.pprint(chessPieces, width=1)

# for player1,v in chessPieces.items():
#     print(player1)
#     for attribute,value in chessPieces.items():
#         print('{} : {}'.format(attribute, value))
print(chessBoard['a8']+chessBoard['b8']+chessBoard['c8']+chessBoard['d8']+chessBoard['e8']+chessBoard['f8']+chessBoard['g8']+chessBoard['h8'])
# print(yaml.dump(chessPieces))
# print(yaml.dump(chessBoard))

turn = "player1"
for i in range(36):

    print('THis is test of my function:' + turn + ' enter something')
    move = input()
    chessBoard[move]= turn
    if turn == "player1":
        turn = "player2"
    else:
        turn = "X"


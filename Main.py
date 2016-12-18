from Board import Board
from Player import Player

the_board = Board()
print the_board.board

x_player = Player("x")
o_player = Player("o")
current_player = x_player

while (the_board.check_winner() == None):
    print "It is player " + current_player.id + "'s turn"
    print the_board.board
    x_coord = input('Please enter your x coordinate: ')
    y_coord = input('Please enter your y coordinate: ')

    if the_board.board[x_coord][y_coord].marker == None:
        the_board.board[x_coord][y_coord].set_marker(current_player.id)

    if the_board.check_winner():
        break
    else:
        if (current_player is x_player):
            current_player = o_player
        else:
            current_player = x_player

print current_player.id, 'has won the game.'
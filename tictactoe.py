""" A fancy tic-tac-toe game for CSSE1001/7030 A1. """
from constants import *

Board = list[list[str]]
Pieces = list[int]
Move = tuple[int, int, int]

# functions here
def num_hours() -> float:
    '''Returns float of number of hours worked on code.'''
    return(float(17.2))

def generate_initial_pieces(num_pieces: int) -> Pieces:
    '''
    Parameters:
        num_pieces(int): number of pieces players have
    Return:
        Pieces: list of the number of pieces
    '''
    Pieces = list(range(1, num_pieces + 1))
    return(Pieces)

def initial_state() -> Board:
    '''Returns an empty board(Board).'''
    board = [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY]]
    return(board)

def place_piece(board: Board, player: str, pieces_available: Pieces, 
                move: Move) -> None:
    '''
    Parameters:
        board(Board): places new piece on current board
        player(str): NAUGHT or CROSS player to place piece 'O' or 'X'
        pieces_available(Pieces): removes size(int) from pieces list
        move(Move): contains piece row, column and size(int)
    '''
    board[move[0]][move[1]] = player + str(move[2])
    pieces_available.remove(move[2])
    return

def print_game(board: Board, naught_pieces: Pieces, 
               cross_pieces: Pieces) -> None:
    '''
    Parameters:
        board(Board): prints current board and pieces
        naught_pieces(Pieces): prints list of NAUGHT pieces available
        cross_pieces(Pieces): prints list of CROSS pieces available
    '''
    # to get rid of [] from the list into a proper string
    print("O has:", end = " ")
    print(*naught_pieces, sep = ", ")
    print("X has:", end = " ")
    print(*cross_pieces, sep = ", ")
    Line = "  ---------"
    print("\n   1  2  3")
    print(Line)
    print("1|" + board[0][0] + "|" + board[0][1] + "|" + board[0][2] + "|")
    print(Line)
    print("2|" + board[1][0] + "|" + board[1][1] + "|" + board[1][2] + "|")
    print(Line)
    print("3|" + board[2][0] + "|" + board[2][1] + "|" + board[2][2] + "|")
    print(Line)
    return

def process_move(move: str) -> Move | None:
    '''
    Parameters:
        move(str): move string user input
    Return:
        Move|None: returns new_move(Move) if move in right format
                    otherwise None
    '''
    if len(move) - move.count(' ') != 3:
        print(INVALID_FORMAT_MESSAGE)
        return None
    elif move[0] not in '1, 2, 3':
        print(INVALID_ROW_MESSAGE)
        return None
    elif move[2] not in '1, 2, 3':
        print(INVALID_COLUMN_MESSAGE)
        return None
    elif move[4] not in '1, 2, 3, 4, 5, 6, 7, 8, 9':
        print(INVALID_SIZE_MESSAGE)
        return None
    else:
        a = int(move[0]) - 1
        b = int(move[2]) - 1
        c = int(move[4])
        new_move = (a, b, c)
        return(new_move)

def get_player_move() -> Move:
   '''
   Return:
        Move: Prompts user input until move is entered in Move format
        Prints help message if user input is 'h/H'
   '''
   while True:
      player_move = input("Enter your move: ")
      if player_move.lower() == 'h':
         print(HELP_MESSAGE)
         continue
      move = process_move(player_move)
      if move == None:
         continue
      else:
         return move
      break

def check_move(board: Board, pieces_available: Pieces, move: Move) -> bool:
    '''
    Parameters:
        board(Board): current board and pieces on it
        pieces_available(Pieces): list of NAUGHT or CROSS pieces
        move(Move): user input move 
    Return:
        bool: True if size(int) is available and bigger than size on board, 
        False otherwise
    '''
    check_board = board[move[0]][move[1]]
    if move[2] in pieces_available:
        if check_board == "  ":
            return True
        if move[2] > int(float(check_board[1])):
            return True
    else:
        return False

def check_win(board: Board) -> str | None:
     '''
     Parameters:
        board(Board): checks the pieces inside the current board
     Return:
        str | None: string 'O' or 'X' if either wins, or None
        if no one won yet
     '''
     #for horizontal wins: joins the row into one string seperated by ' ' 
     #and counts the number of element 'O/X'. If there are 3 of 'O' or 3 of 
     #'X', return 'O' or 'X' respectively.'''
     for row in board: 
        if ' '.join(row).count('O') == 3:
             return 'O'
     for row in board:
         if ' '.join(row).count('X') == 3: 
             return 'X'
     # for vertical wins: 'column' contains every column in the board. 
     # Uses the same logic as horizontal wins.
     column = [[board[0][0], board[1][0], board[2][0]], 
               [board[0][1], board[1][1], board[2][1]], 
               [board[0][2], board[1][2], board[2][2]]]
     for col in column: 
         if ' '.join(col).count('O') == 3:
             return 'O'
     for col in column: 
         if ' '.join(col).count('X') == 3: 
             return 'X'
     # for diagonal wins: 'diagonal' contains the two diagonal lines in 
     # the board. Uses the same logic as horizontal wins.
     diagonal = [[board[0][0], board[1][1], board[2][2],], 
                 [board[0][2], board[1][1], board[2][0]]]
     for dia in diagonal:
         if ' '.join(dia).count('O') == 3:
             return 'O'
         if ' '.join(dia).count('X') == 3:
             return 'X'
     else:
         return None

def check_stalemate(board: Board, naught_pieces: Pieces, 
                    cross_pieces: Pieces) -> bool:
    '''
    Parameters:
        board(Board): current board and pieces
        naught_pieces(Pieces): list of available NAUGHT pieces
        cross_pieces(Pieces): list of available CROSS pieces
    Return:
        bool: False if game can continue going, True if at stalemate
    '''
    flat_board = []
    # to flatten the board list into one long list for the 'for' function
    for row in board: 
        flat_board.extend(row)
        ''.join(flat_board)
    str_board = str(flat_board)
    int_board = ""
    # to remove XO[]', and spaces so as to compare only the numbers on the 
    # board against the pieces
    for x in str_board:
        if x in 'XO[]\'\,\ ':
            int_board = int_board
        else: 
            int_board = int_board + x
    # to ensure all board spaces are filled: 0 == "", <9 is != 9
    if int_board == "":
        return False
    else:
        if len(int_board) != 9:
            return False
    # to find the bigger number between the board and the pieces
        elif len(int_board) == 9:
            for number in naught_pieces: 
                for y in int_board:
                    if number > int(float(y)):
                        return False
            for number in cross_pieces:
                for y in int_board:
                    if number > int(float(y)):
                        return False
            else:
                return True               

def main() -> None: 
    '''Starts the game and keeps going until Play again? != y/Y'''
    # prints empty board and new pieces for the game
    board = initial_state()
    naught_pieces = generate_initial_pieces(PIECES_PER_PLAYER)
    cross_pieces = generate_initial_pieces(PIECES_PER_PLAYER)
    print_game(board, naught_pieces, cross_pieces)
    # check if any player has won the game during while loop
    while check_win(board) is None:
        # check if stalemate has been reached in the game
        if check_stalemate(board, naught_pieces, cross_pieces) is False:
            # turn = 2 is to ensure that while it is still even (NAUGHT's 
            # turn), it will not play functions from odd (CROSS'S turn)
            turn = 2
            while turn % 2 == 0:
                # for NAUGHT turn
                print("\nO turn to move\n")
                move = get_player_move()
                if check_move(board, naught_pieces, move) is True:
                    place_piece(board, NAUGHT, naught_pieces, move)
                    print_game(board, naught_pieces, cross_pieces)
                    turn = turn + 1
                else:
                    print(INVALID_MOVE_MESSAGE)
                    continue
            while turn % 2 != 0:
                # before the turn starts, ensure that NAUGHT hasn't won or 
                # game is at a stalemate
                if check_win(board) is not None:
                    break
                elif check_stalemate(board, naught_pieces, 
                                     cross_pieces) is not False:
                    break
                # for CROSS turn
                print("\nX turn to move\n")
                move = get_player_move()
                if check_move(board, cross_pieces, move) is True:
                    place_piece(board, CROSS, cross_pieces, move)
                    print_game(board, naught_pieces, cross_pieces)
                    turn = turn + 1
                else:
                    print(INVALID_MOVE_MESSAGE)
                    continue   
        else:
            print("Stalemate!")
            play_input = input("Play again? ")
            if play_input.lower() == 'y':
            # reset board and pieces, check_win(board) back to none if 
            # input == 'y/Y' and ends that game
                main()
                return
            else:
                # end of game: function done
                return
    print(check_win(board) + " wins!")
    # play again function
    play_input = input("Play again? ")
    if play_input.lower() == 'y':
        # reset board and pieces, check_win(board) back to none 
        # if input == 'y/Y'
        main()
    else:
        # end of game: function done
        return

if __name__ == '__main__':
    main()

# Author: Lyndon Keeling
# Date: 09SEP2021
# Description: A game with a 4x4 board, where players move pieces. Any piece that lands orthogonal
# to another piece of opposing color will be flipped to that color. A player wins when their
# color are the only ones left playing on the board.

class OrthokonBoard:
    """
    A game with a 4x4 board, where players move pieces. Any piece that lands orthogonal to
    another piece of opposing color will be flipped to that color. A player wins when
    their color are the only ones left playing on the board.
    """

    def __init__(self):
        """ Initializes objects for program"""
        self._current = "UNFINISHED"
        self._board = [["R", "R", "R", "R"],  # row 0
                       ["E", "E", "E", "E"],  # row 1
                       ["E", "E", "E", "E"],  # row 2
                       ["Y", "Y", "Y", "Y"]]  # row 3

    def get_current_state(self):
        """Returns current state of the game."""
        return self._current

    def state_check(self):
        """Determines the state of the game after every turn"""

        winconditiony = 0
        for i in range(0, 4):  # test case for R, if winconditionY == 0, Yellow wins
            for ch in range(0, 4):
                if self._board[i][ch] == "R":  # looks for R and if there are any it adds to total
                    winconditiony += 1
        if winconditiony == 0:
            self._current = "YELLOW_WON"

        winconditionr = 0
        for i in range(0, 4):  # test case for Y, if winconditionR == 0, Red wins
            for ch in range(0, 4):
                if self._board[i][ch] == "Y":  # looks for Y and if there are any it adds to total
                    winconditionr += 1
        if winconditionr == 0:
            self._current = "RED_WON"

    def get_current_board_layout(self):  # For working on the program.
        """Returns current board layout"""
        print(self._board[3])
        print(self._board[2])
        print(self._board[1])
        print(self._board[0])

    def make_move(self, startrow, startcol, endrow, endcol):
        """Makes the move on the OrthokonBoard"""

        # Initial code determines if move is valid.
        if self._board[startrow][startcol] == "E":  # move cannot begin if no piece there.
            return False
        elif self._board[endrow][endcol] == "R":  # move cannot occupy space already occ.
            return False
        elif self._board[endrow][endcol] == "Y":  # move cannot occupy space already occ.
            return False
        elif self._current == "RED_WON":  # ends program if Red won
            return False
        elif self._current == "YELLOW_WON":  # ends program if Yellow won
            return False
        elif endrow == 4:  # out of range move
            return False
        elif endcol == 4:  # out of range move
            return False

        elif abs(startcol) - abs(endcol) != 0:  # orthogonal up and down check
            if abs(startrow) - abs(endrow) != 0:  # orthogonal left and right check
                slope = int((abs(startcol) - abs(endcol)) / (abs(startrow) - abs(endrow)))  # diagonal check
                if slope != 1:
                    return False  # Implies invalid movement, not orthogonal or diagonal

        callclass = OrthokonBoard
        if endcol < 3:  # case cuz 3 is out of range.
            if self._board[startrow][startcol] == "R":  # R case

                for i in range(-1, 2):  # Up and down check
                    if self._board[endrow + i][endcol] == "Y":
                        self._board[endrow + i][endcol] = "R"
                        self._board[startrow][startcol] = "E"
                        self._board[endrow][endcol] = "R"
                        callclass.state_check(self)
                        return True

                for i in range(-1, 2):  # Left to right check
                    if self._board[endrow][endcol + i] == "Y":
                        self._board[endrow][endcol + i] = "R"
                        self._board[startrow][startcol] = "E"
                        self._board[endrow][endcol] = "R"
                        callclass.state_check(self)
                        return True
                if self._board[startrow][startcol] == "R":  # Implies move was invalid.
                    return False

            elif self._board[startrow][startcol] == "Y":  # Y case
                for i in range(-1, 2):  # Up and down check
                    if self._board[endrow + i][endcol] == "R":
                        self._board[endrow + i][endcol] = "Y"
                        self._board[startrow][startcol] = "E"
                        self._board[endrow][endcol] = "Y"
                        callclass.state_check(self)
                        return True

                for i in range(-1, 2):  # Left to right check
                    if self._board[endrow][endcol + i] == "R":
                        self._board[endrow][endcol + i] = "Y"
                        self._board[startrow][startcol] = "E"
                        self._board[endrow][endcol] = "Y"
                        callclass.state_check(self)
                        return True
                if self._board[startrow][startcol] == "Y":  # Implies move was invalid.
                    return False

        elif endcol == 3:  # special case for when endcol == 3, for out of range case
            if self._board[startrow][startcol] == "R":  # R case

                for i in range(-1, 2):  # Up and down check
                    if self._board[endrow + i][endcol] == "Y":
                        self._board[endrow + i][endcol] = "R"
                        self._board[startrow][startcol] = "E"
                        self._board[endrow][endcol] = "R"
                        callclass.state_check(self)
                        return True

                for i in range(-1, 1):  # Left to right check
                    if self._board[endrow][endcol + i] == "Y":
                        self._board[endrow][endcol + i] = "R"
                        self._board[startrow][startcol] = "E"
                        self._board[endrow][endcol] = "R"
                        callclass.state_check(self)
                        return True
                if self._board[startrow][startcol] == "R":  # Implies move was invalid.
                    return False

            elif self._board[startrow][startcol] == "Y":  # Y case
                for i in range(-1, 2):  # Up and down check
                    if self._board[endrow + i][endcol] == "R":
                        self._board[endrow + i][endcol] = "Y"
                        self._board[startrow][startcol] = "E"
                        self._board[endrow][endcol] = "Y"
                        callclass.state_check(self)
                        return True

                for i in range(-1, 1):  # Left to right check
                    if self._board[endrow][endcol + i] == "R":
                        self._board[endrow][endcol + i] = "Y"
                        self._board[startrow][startcol] = "E"
                        self._board[endrow][endcol] = "Y"
                        callclass.state_check(self)
                        return True
                if self._board[startrow][startcol] == "Y":  # Implies move was invalid.
                    return False


#board = OrthokonBoard()
#Red win condition
#board.make_move(0,0,2,0)
#board.make_move(0,1,2,1)
#board.make_move(0,2,2,2)
#board.make_move(0,3,2,3)

#board.make_move(0,1,2,3)
#board.make_move(2,3,2,0)
#board.make_move(0,0,2,2)
# board.make_move(3,1,0,1)
# board.make_move(0,1,2,3)
# board.make_move(0,1,2,1)
# board.make_move(0,2,2,2)
# board.make_move(0,3,2,3)

#board.get_current_board_layout()
#print(board.get_current_state())

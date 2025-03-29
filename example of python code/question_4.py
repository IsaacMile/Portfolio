class ColourPuzzle:
    def __init__(self, puzzle):
        '''initialised a colour puzzle using board puzzle

        Args:
            self (ColourPuzzle): colour puzzle being created
            puzzle (2d list of size 4x4 containing int): starting board

        Raises:
            ValueError: puzzle is not a valid puzzle
        '''
        # check that puzzle is a 4x4 list containing ints
        if not (isinstance(puzzle, list)):
            raise ValueError("puzzle needs to be a list")
        if len(puzzle) != 4:
            raise ValueError("puzzle must have 4 rows")
        if not (isinstance(puzzle[0], list) and
                isinstance(puzzle[1], list) and
                isinstance(puzzle[2], list) and
                isinstance(puzzle[3], list)):
            raise ValueError("puzzle must be a 2d list")
        if (len(puzzle[0]) != 4 or
           len(puzzle[1]) != 4 or
           len(puzzle[2]) != 4 or
           len(puzzle[3]) != 4):
            raise ValueError("puzzle must have 4 columns")
        # check there is one and only one 0
        # and that the other numbers are all 1,2 or 3
        number_empty = 0
        valid_tiles = True
        for row in puzzle:
            for column in row:
                if column == 0:
                    number_empty += 1
                elif not (column == 1 or column == 2 or column == 3):
                    valid_tiles = False
        if number_empty != 1:
            raise ValueError("puzzle must have 1 empty space")
        if valid_tiles is False:
            raise ValueError("puzzle must contain 1, 2 or 3 in spaces with a "
                             "block")
        self._board = puzzle.copy()

    def matchPattern(self, pattern):
        '''tests in the centre 2x2 matches the pattern given, pattern is not
           tested. returns true if matching, false if not

        Args:
            self (ColourPuzzle): the puzzle to be tested
            pattern (2x2, 2d list of int): the puzzle to be searched for

        Returns:
            pattern_found (bool): returns True if pattern matches central 2x2,
                false if it does not
        '''
        if (self._board[1][1] == pattern[0][0] and
           self._board[1][2] == pattern[0][1] and
           self._board[2][1] == pattern[1][0] and
           self._board[2][2] == pattern[1][1]):
            # if the corresponding indexes on the lists match
            return True
        else:
            return False

    def moveLowerTile(self):
        '''moves the tile below the empty tile up by 1 if possible,
           returns true if move was made

        Args:
            self (ColourPuzzle): puzzle to be moved

        Returns:
            move_successful (bool): returns True if move was possible and
                made, false if it was not
        '''
        # find the empty tile in _board
        for row in range(len(self._board)):
            for column in range(len(self._board[row])):
                if self._board[row][column] == 0:
                    empty_tile = [row, column]
        # if empty tile is at bottom, move is not possible, return false
        if empty_tile[0] == 3:
            return False
        # swap tiles using empty_tile as point of reference
        tile_to_replace = self._board[empty_tile[0]+1][empty_tile[1]]
        self._board[empty_tile[0]][empty_tile[1]] = tile_to_replace
        self._board[empty_tile[0]+1][empty_tile[1]] = 0
        return True

    def moveUpperTile(self):
        '''moves the tile above the empty tile down by 1 if possible,
           returns true if move was made

        Args:
            self (ColourPuzzle): puzzle to be moved

        Returns:
            move_successful (bool): returns True if move was possible and
                made, false if it was not
        '''
        # find the empty tile in _board
        for row in range(len(self._board)):
            for column in range(len(self._board[row])):
                if self._board[row][column] == 0:
                    empty_tile = [row, column]
        # if empty tile is at top, move is not possible, return false
        if empty_tile[0] == 0:
            return False
        # swap tiles using empty_tile as point of reference
        tile_to_replace = self._board[empty_tile[0]-1][empty_tile[1]]
        self._board[empty_tile[0]][empty_tile[1]] = tile_to_replace
        self._board[empty_tile[0]-1][empty_tile[1]] = 0
        return True

    def moveLeftTile(self):
        '''moves the tile left of the empty tile right by 1 if possible,
           returns true if move was made

        Args:
            self (ColourPuzzle): puzzle to be moved

        Returns:
            move_successful (bool): returns True if move was possible and
                made, false if it was not
        '''
        # find the empty tile in _board
        for row in range(len(self._board)):
            for column in range(len(self._board[row])):
                if self._board[row][column] == 0:
                    empty_tile = [row, column]
        # if empty tile is on left, move is not possible, return false
        if empty_tile[1] == 0:
            return False
        # swap tiles using empty_tile as point of reference
        tile_to_replace = self._board[empty_tile[0]][empty_tile[1]-1]
        self._board[empty_tile[0]][empty_tile[1]] = tile_to_replace
        self._board[empty_tile[0]][empty_tile[1]-1] = 0
        return True

    def moveRightTile(self):
        '''moves the tile right of the empty tile left by 1 if possible,
           returns true if move was made

        Args:
            self (ColourPuzzle): puzzle to be moved

        Returns:
            move_successful (bool): returns True if move was possible and
                made, false if it was not
        '''
        # find the empty tile in _board
        for row in range(len(self._board)):
            for column in range(len(self._board[row])):
                if self._board[row][column] == 0:
                    empty_tile = [row, column]
        # if empty tile is on right, move is not possible, return false
        if empty_tile[1] == 3:
            return False
        # swap tiles using empty_tile as point of reference
        tile_to_replace = self._board[empty_tile[0]][empty_tile[1]+1]
        self._board[empty_tile[0]][empty_tile[1]] = tile_to_replace
        self._board[empty_tile[0]][empty_tile[1]+1] = 0
        return True

    def solvable(self, pattern, n):
        '''takes in a pattern and number of moves required to find the pattern
           the function will then call itself with every possible move,
           n number of times until a correct solution is found or n reaches 0

        Args:
            self (ColourPuzzle): the puzzle to be solved
            pattern (2x2 list of int): pattern being searched for in centre
            n (int): number of moves remaining to solve puzzle

        Returns:
            pattern_possible (bool): True if the puzzle is solvable,
                false if not
        '''
        # base cases: if solution was found or number of trials reaches 0
        # return true or false respectively
        if self.matchPattern(pattern) is True:
            return True
        if n == 0:
            return False

        # if base case is not met,
        # move in every possible directrion and call self
        pattern_possible = False
        if self.moveLeftTile() is True:
            pattern_possible = (pattern_possible or
                                self.solvable(pattern, n-1))
            self.moveRightTile()
        if self.moveRightTile() is True:
            pattern_possible = (pattern_possible or
                                self.solvable(pattern, n-1))
            self.moveLeftTile()
        if self.moveLowerTile() is True:
            pattern_possible = (pattern_possible or
                                self.solvable(pattern, n-1))
            self.moveUpperTile()
        if self.moveUpperTile() is True:
            pattern_possible = (pattern_possible or
                                self.solvable(pattern, n-1))
            self.moveLowerTile()
        return pattern_possible

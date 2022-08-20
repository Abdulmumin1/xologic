class Logic():
    """
    Logic for tic-tac-toe board
    """

    def __init__(self, board_size=4):
        self.board_size = board_size
        self.win_size = 2
        self.default = ['' for i in range(self.board_size**2)]
        self.board = self.default[:]

    def check(self, board=None, board_size=None) -> list:
        """
        returns the winner 
        and a list of the indexes where the win was found!

        example (x, [0,1,2,3])
        """
        if not board:
            board = self.board
        else:
            if not board_size: return "board_size required for a custom board"
        horizontal = self.horizontal(board)
        # print(<'horizontal checked')
        vertical = self.vertical(board)
        # print('vertical checked')
        diagonal_1 = self.diagonal_1(board)
        # print('d1 checked')
        diagonal_2 = self.diagonal_2(board)
        # print('d2 checked')
        if horizontal:
            return horizontal
        elif vertical:
            return vertical
        elif diagonal_1:
            return diagonal_1
        elif diagonal_2:
            return diagonal_2
        else:
            return

    def horizontal(self, board):
        at = 0
        number_indexes = [i for i in range(self.board_size)]
        # linux = map(lambda x:board[at+x], line)
        for i in range(self.board_size):
            pos = list(map(lambda x: board[at+x], number_indexes))
            # print(pos)
            if self.hole(pos, board[at]):
                return board[at], [j+at for j in number_indexes]
            at += self.board_size
        return False

    def vertical(self, board):
        at = 0
        for i in range(self.board_size):
            number_indexes = [
                i+at for i in range(0, self.board_size**2, self.board_size)]
            line = map(lambda x: board[x], number_indexes)
            if self.hole(line, board[at]):
                return board[at], number_indexes
            at += 1

        return False

    def diagonal_1(self, board):

        number_indexes = [i for i in range(
            0, self.board_size**2, self.board_size+1)]
        pos = map(lambda x: board[x], number_indexes)
        # print(number_indexes)
        if self.hole(pos, board[0]):
            return board[0], number_indexes
        return False

    def diagonal_2(self, board):
        number_indexes = [i for i in range(
            self.board_size-1, self.board_size**2, self.board_size-1)][:self.board_size]
        # print(number_indexes)
        pos = map(lambda x: board[x], number_indexes)
        if self.hole(pos, board[self.board_size-1]):
            return board[self.board_size-1], number_indexes

        return False

    def hole(self, list_, val):
        # return self.black_hole(list_, val)
        all_values = True
        for i in list_:
            if i == val and val != '' and i != '':
                all_values = True
            else:
                all_values = False
                return all_values

        return all_values

    def black_hole(self, list_, val):
        count = 0
        for i in list_:
            if i == val and val != '' and i != '':
                count += 1
            else:
                return False
            if count == self.win_size:
                return True

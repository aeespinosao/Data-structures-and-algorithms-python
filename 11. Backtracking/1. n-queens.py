class NQueens:
    
    def __init__(self, n) -> None:
        self.n = n
        #self.board = [[0]*n]*n why does not work?
        self.board = [[0 for i in range(n)] for j in range(n)]

    def print_queens(self):
        for row in self.board:
            for column in row:
                if column == 1:
                    print(' Q ', end='')
                else:
                    print(' _ ', end='')
            print()
            
    def is_place_safe(self, row_index, col_index):
        for column in self.board[row_index]:
            if column == 1:
                return False
            
        j = col_index
        for i in range(row_index, -1, -1):
            if i < 0:
                break
            if self.board[i][j] == 1:
                return False
            j = j-1
        
        j = col_index
        for i in range(row_index, self.n):
            if i < 0:
                break
            if self.board[i][j] == 1:
                return False
            j = j-1
            
        return True
    
    def solve(self, col_index=0):
        if col_index == self.n:
            return True
        
        for row_index in range(self.n):
            if self.is_place_safe(row_index, col_index):
                self.board[row_index][col_index] = 1
                if self.solve(col_index+1):
                    return True
                self.board[row_index][col_index] = 0
            
        return False
    
    def solve_n_queens(self):
        if self.solve():
            self.print_queens()
        else:
            print('no solutions')
    
queens = NQueens(4)
queens.solve_n_queens()
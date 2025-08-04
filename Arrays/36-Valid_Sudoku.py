"""
Question: Valid Sudoku
Leetcode -36: https://leetcode.com/problems/valid-sudoku/

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

Example:
Input:
Input: board = 
[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]

Output: true

"""
from typing import List,Counter

class Solution:
    def visualizeBoard(self, board):
        for i in range(9):
            print([board[i][j] for j in range(9)])

    def checkDuplicate(self, numbers: List[int]) -> bool:
        freq = Counter(numbers)
        freq["."] = 0 # Ignoring empty cells
        for i in list(freq.values()):
            if i > 1:
                return False
        return True
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        #Checking rows 
        for row in board:
            if self.checkDuplicate(row):
                continue
            else:
                return False
        
        #Checking columns
        for i in range(9):
            column = [board[j][i] for j in range(9)]
            if self.checkDuplicate(column):
                continue
            else:
                return False
        
        #Checking boxes
        #We have known coordinates for the starting point of each "box"
        # 0,0 0,3 0,6 3,0 3,3 3,6 6,0 6,3 6,6
        # We will check elements in the box with these starting points as reference

        boxStartCoordinates = [[0,0], [0,3], [0,6], [3,0], [3,3], [3,6], [6,0], [6,3], [6,6]]
        for start in boxStartCoordinates:
            boxNumbers = []
            for i in range(start[0], start[0] + 3):                            
                [boxNumbers.append(board[i][start[1] + j]) for j in range(3)]
            
            if self.checkDuplicate(boxNumbers):
                continue
            else:
                return False


        return True
    

#Driver Code
obj = Solution()
board = [["1","2",".",".","3",".",".",".","."], ["4",".",".","5",".",".",".",".","."], [".","9","8",".",".",".",".",".","3"],["5",".",".",".","6",".",".",".","4"], [".",".",".","8",".","3",".",".","5"], ["7",".",".",".","2",".",".",".","6"],[".",".",".",".",".",".","2",".","."], [".",".",".","4","1","9",".",".","8"], [".",".",".",".","8",".",".","7","9"]]
board2 = [["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
board3 = [[".",".",".","1",".","8",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],["4",".",".",".",".","7",".",".","."],[".",".",".","7",".",".","8","4","1"],[".",".",".",".","7",".",".",".","."],[".",".",".",".",".",".","6",".","."],[".",".",".","6",".",".",".",".","."],["6",".",".",".",".",".",".",".","."]]
#op = obj.isValidSudoku(board)
#op2 = obj.isValidSudoku(board2)
op3 = obj.isValidSudoku(board3)
#obj.visualizeBoard(board3)
print("========OUTPUT=========")
#print(op)
#print(op2)
print(op3)
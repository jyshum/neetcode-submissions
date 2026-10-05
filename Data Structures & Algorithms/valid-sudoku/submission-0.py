class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:    
        # any occurance of a number that is > 9 returns FALSE
        # loop through each row to find if there are duplicates
        # loop through each column to find if there are duplicates
        # loop through every 3 by 3 to find if there are duplicates 

        for c in range(9): # checking each element in each row
            seen = set()
            for r in range(9):
                if board[c][r] in seen:
                    return False
                if board[c][r] != ".":
                    seen.add(board[c][r])
        
        for r in range(9): # checking each element in each column
            seen = set()
            for c in range(9):
                if board[c][r] in seen:
                    return False
                if board[c][r] != ".":
                    seen.add(board[c][r])

        for bc in range(0, 9, 3):
            for br in range(0, 9, 3):
                seen = set()
                for c in range(bc, bc+3):
                    for r in range(br, br+3):
                        if board[c][r] in seen:
                            return False
                        if board[c][r] != ".":
                            seen.add(board[c][r])

        return True

        

        
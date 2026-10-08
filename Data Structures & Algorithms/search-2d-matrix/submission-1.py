class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        top = rows * cols
        bottom = 0

        while top > bottom:
            middle = (top + bottom) // 2
            row = middle // cols
            col = middle % cols
            value = matrix[row][col]

            if target == value:
                return True
            elif target < value:
                top = middle
            else:
                bottom = middle + 1

        return False
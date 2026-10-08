class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        array1d = [item for row in matrix for item in row]
        top = len(array1d)
        bottom = 0

        while top > bottom:
            middle = (top+bottom)//2
            if target == array1d[middle]:
                return True
            elif target < array1d[middle]:
                top = middle
            elif target > array1d[middle]:
                bottom = middle + 1

        return False

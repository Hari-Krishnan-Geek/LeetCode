class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m = len(matrix) - 1
        n = len(matrix[0]) - 1

        result = False
        i = m
        j = 0
        while i >= 0 and j<= n:
            if target < matrix[i][j]:
                i -= 1
            elif target > matrix[i][j]:
                j += 1
            else:
                result = True
                break
        return result


        
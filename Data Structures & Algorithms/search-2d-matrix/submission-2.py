class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 1:
            left = 0
            right = len(matrix[0]) - 1

            while left <= right:
                mid = (left + right) // 2

                if target < matrix[0][mid]:
                    right = mid - 1
                elif target > matrix[0][mid]:
                    left = mid + 1
                else:
                    return True
            return False

        top = 0
        bottom = len(matrix) - 1
        row = None

        while top is not bottom:
            mid = math.ceil((top + bottom) / 2)

            if target < matrix[mid][0]:
                bottom = mid - 1
            elif target > matrix[mid][0]:
                top = mid
            else:
                return True
            
            if top == bottom:
                row = top

        if row is None:
            return False

        left = 0
        right = len(matrix[row]) - 1

        while left <= right:
            mid = (left + right) // 2

            if target < matrix[row][mid]:
                right = mid - 1
            elif target > matrix[row][mid]:
                left = mid + 1
            else:
                return True

        return False
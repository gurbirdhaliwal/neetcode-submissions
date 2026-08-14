class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        outer_left, outer_right = 0, len(matrix) - 1
        while outer_left <= outer_right:
            outer_middle = (outer_left + outer_right) // 2
            
            if matrix[outer_middle][0] > target:
                outer_right = outer_middle - 1
            elif matrix[outer_middle][-1] < target:
                outer_left = outer_middle + 1
            else:
                inner_left, inner_right = 0, len(matrix[outer_middle]) - 1
                while inner_left <= inner_right:
                    inner_middle = (inner_left + inner_right) // 2
                    if matrix[outer_middle][inner_middle] < target:
                        inner_left = inner_middle + 1
                    elif matrix[outer_middle][inner_middle] > target:
                        inner_right = inner_middle - 1
                    else:
                        return True
                return False
        return False
                
        
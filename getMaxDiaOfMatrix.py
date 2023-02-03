def getDiagonalSum(matrix,row,col,rows,cols):
    curSum = 0
    while(row<rows and col<cols):
        curSum += matrix[row][col]
        row += 1
        col += 1
    return curSum

def getMaximumDiagonal(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    maxSum = 0
    for i in range(1,rows):
        curSum = getDiagonalSum(matrix,i,0,rows,columns)
        maxSum = max(maxSum,curSum)
    
    for j in range(0,columns):
        curSum = getDiagonalSum(matrix,0,j,rows,columns)
        maxSum = max(maxSum,curSum)
    
    return maxSum
    
matrix = [[1,2,3,10],[4,5,6,10],[7,8,9,10]]
print(getMaximumDiagonal(matrix))    

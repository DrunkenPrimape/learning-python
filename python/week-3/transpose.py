def transpose(matrix):
    # Store the values of rows and columns of the current matrix 
    rows = range(len(matrix))
    columns = range(len(matrix[0]))

    # Create a empty transpose matrix with the flipped size
    transpose = [[0 for column in rows] for row in columns]

    # For each element in the matrix, assign it to the right location in the transpose
    for row in rows:
        for column in columns:
            transpose[column][row] = matrix[row][column]

    return transpose          


transpose([[1,4,9]])
transpose([[1,3,5],[2,4,6]])
transpose([[1,1,1],[2,2,2],[3,3,3]])
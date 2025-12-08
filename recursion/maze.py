# Ex 4 
# Write a recursive function that determines whether there is a path from the top-left corner (0, 0) to the bottom-right corner (n-1, n-1) in a maze represented by a 2D grid. 
# Maze Rules: 
# •	The maze is a 2D list of booleans (True means you can walk there, False means wall). 
# •	You can move up, down, left, or right — no diagonal moves. 
# •	You may not revisit the same cell twice. 
# •	The start point is always (0, 0). 
# •	The end point is always (n-1, n-1). 



def path_exists(maze):
    size = len(maze)                     
    visited = set()                      

    def explore(row, col):
        if row < 0 or row >= size or col < 0 or col >= size:
            return False
        
        if maze[row][col] is False:
            return False
        
        if (row, col) in visited:
            return False

        if (row, col) == (size - 1, size - 1):
            return True

        visited.add((row, col))
        return (
            explore(row + 1, col) or  
            explore(row - 1, col) or  
            explore(row, col + 1) or  
            explore(row, col - 1)     
        )
    return explore(0, 0)



maze = [
    [True, True, False],
    [False, True, False],
    [False, True, True]
]

print(path_exists(maze))   

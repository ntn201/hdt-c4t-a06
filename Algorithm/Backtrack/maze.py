maze = [[0,0,1,0,0,0],
        [0,1,1,0,1,1],
        [0,0,0,0,0,0],
        [0,0,1,0,1,0],
        [0,0,1,0,1,1],
        [0,0,1,0,0,0]]
    
def get_moves(maze,row,col):
    moves = [[-1,-1],[-1,-1],[-1,-1],[-1,-1]]
                # U       D       L       R
    if row > 0 and maze[row-1][col] == 0:
        moves[0] = [row-1,col]
    if row < len(maze)-1 and maze[row+1][col] == 0:
        moves[1] = [row+1,col]
    if col > 0 and maze[row][col-1] == 0:
        moves[2] = [row,col-1]
    if col < len(maze[0])-1 and maze[row][col+1] == 0:
        moves[3] = [row,col+1]
    return moves

def go(maze,start,end,path=[],paths=[]):
    if start == end:
        paths.append(path)
    else:
        moves = get_moves(maze,start[0],start[1])
        for cell in moves:
            if cell != [-1,-1]:
                maze[start[0]][start[1]] = 1
                go(maze,cell,end,path+[cell],paths)
                maze[start[0]][start[1]] = 0

    return paths
        
print(go(maze,[0,0],[5,5]))
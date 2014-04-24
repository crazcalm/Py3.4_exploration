import time
from turtle import *

class Maze:
    def __init__(self, mazeFileName):
        rowsInMaze = 0
        columnInMaze = 0
        self.mazelist = []
        mazeFile = open(mazeFileName, "r")
        rowsInMaze = 0

        for line in mazeFile:
            rowList = []
            col = 0
            for ch in line[:-1]:
                rowList.append(ch)
                if ch == "S":
                    self.startRow = rowsInMaze
                    self.startCol = col

                col = col + 1
            rowsInMaze = rowsInMaze + 1
            self.mazelist.append(rowList)
            columnInMaze = len(rowList)

        self.rowsInMaze = rowsInMaze
        self.columnInMaze = columnInMaze
        self.xTranslate = -columnInMaze/2
        self.yTranslate = rowsInMaze/2
        self.t = Turtle(shape="turtle")
        setup(width=600, height=600)
        setworldcoordinates(-(columnInMaze-1)/2 -5,
                            -(rowsInMaze-1)/2-5,
                            (columnInMaze-1)/2+5,
                            (rowsInMaze -1)/2+5)

    def drawMaze(self):
        for y in range(self.rowsInMaze):
            for x in range(self.columnInMaze):
                if self.mazelist[y][x] == OBSTACLE:
                    self.drawCenterBox(x+self.xTranslate,
                                       -y)



def searchFrom(maze, startRow, startColumn):
    maze.updatePosition(startRow, startColumn)

    # Check for base case
    # 1. We have run into an obstacle, return false
    if maze[startRow][startColumn] == OBSTACLE:
        return False

    # 2. We have found a square that has already been explored
    if maze[startRow][startColumn] == TRIED:
        return False

    # 3. Success, an outside edge not occupied by an obstacle
    if maze.isExit(startRow, startColumn):
        maze.updatePosition(startRow, startColumn, PART_OF_PATH)
        return True
    maze.updatePosition(startRow, startColumn, TRIED)

    # Otherwise, use logical short circuiting to try each
    # direction in turn (if needed)
    found = searchFrom(maze, startRow-1, startColumn) or \
            searchFrom(maze, startRow+1, startColumn) or \
            searchFrom(maze, startRow, startColumn-1) or \
            searchFrom(maze, startRow, startColumn+1)

    if found:
        maze.updatePosition(startRow, startColumn, PART_OF_PATH)
    else:
        maze.updatePosition(startRow, startColumn, DEAD_END)



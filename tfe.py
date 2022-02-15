import numpy as np
from random import randint

class twenty_forty_eight:
    def __init__(self, ID):
        self.ID = ID
        self.turnNum = 0
        self.score = 0

        self.board = np.array([[0 for i in range(4)] for x in range(4)], int)
        self.board_init()
        
        self.colours = twenty_forty_eight.colours_init()
        
    def __repr__(self):
        print_str = f'Game = {self.ID}\nTurns = {self.turnNum}\n'
        for x in self.board:
            for y in x:
                print_str += '[{:^6}]'.format(y) if y != 0 else '[      ]'
            print_str += '\n'
        return print_str

    def colours_init():
        colour_dict = {
            0 : "#FFFFFF",
            2 : "#FFF4E5",
            4 : "#FFEED9",
            8 : "#FFE9CC",
            16 : "#FEE3C0",
            32 : "#FDDEB3",
            64 : "#F3DFC0",
            128 : "#E8E0CC",
            256 : "#DDE0D9",
            512 : "#D0E1E6",
            1024 : "#C1E2F2",
            2048 : "#B1E3FF"
            }
        return colour_dict
    
    def board_init(self):
        for x in range(2):
            self.rand_insert()
    
    def move_check(self, rowNum, colNum, rowCheck):
        # If the space is empty, a move is needed but search is not fin
        if self.board[rowCheck][colNum] == 0:
            return (0, False)
        # If the space is not the same no merge is needed and the search is fin
        elif self.board[rowCheck][colNum] != self.board[rowNum][colNum]:
            return (1, True)
        # If the space is the same a merge is needed and the search is fin
        elif self.board[rowCheck][colNum] == self.board[rowNum][colNum]:
            return (2, True)
    
    # Rotates the board array to a certain orientation 
    def arr_transpose(self, direction):
        # Up = 0, Left = 3, Down = 2, Right = 1
        self.board = np.rot90(self.board, direction)
    
    def move(self, i): # Moves elements up
        self.arr_transpose(abs(i))
        rowNum = 1
        colNum = 0
        num_of_moves = 0
        for row in self.board[1:]:   # Moves down rows starting at 2nd row
            colNum = 0
            for item in row:    # Moves right on the full row
                if item != 0:
                    for rowCheck in reversed(range(rowNum)):
                        result = self.move_check(rowNum, colNum, rowCheck)
                        req_row = abs(rowCheck)
                        if result[1] == True:
                            break
                    if result[0] == 2:  # Merge
                        self.item_mod(item*2, rowNum, colNum, req_row)
                        num_of_moves += 1
                    elif result[1] == False: # Move into empty top row
                        self.item_mod(item, rowNum, colNum, req_row)
                        num_of_moves += 1
                    elif req_row+1 != rowNum: # Move distance
                        self.item_mod(item, rowNum, colNum, req_row+1)
                        num_of_moves += 1
                    # Everything else is unmoved 
                colNum += 1
            rowNum += 1
        self.arr_transpose(i)
        return num_of_moves
    
    # Changes element in array
    def item_mod(self, item, rowNum, colNum, desired_row):
        tempItem = abs(item)
        self.board[rowNum][colNum] = 0
        self.board[desired_row][colNum] = abs(tempItem)
    
    # Returns a dictionary of the arr's empty space locations
    def empty_spaces(self): 
        avail_space_dict = {}
        rowNum = 0      # Starting locations of the search
        colNum = 0
        i = 1
        for row in self.board:
            colNum = 0
            for item in row:
                if item == 0:
                    avail_space_dict[i] = (rowNum, colNum)
                    i+=1
                colNum += 1
            rowNum += 1
        return avail_space_dict

    def rand_insert(self):
        # insert starting integer into random empty element
        avail_space_dict = twenty_forty_eight.empty_spaces(self)
        
        # when bool() is used on empty dictionary in python it returns False
        if bool(avail_space_dict) == True:                  
            randNum = randint(1, len(avail_space_dict))
            randCoords = avail_space_dict[randNum]
            self.board[randCoords[0]][randCoords[1]] = 2    # num inserted
    
    def avail_moves_check(self):
        for row in self.board:
            for col in row:
                if col == 0:
                    return True
        for row in range(4):
            for col in range(3):
                check_num = self.board[row][col]
                if self.board[row][col+1] == check_num:
                    return True
        for row in range(3):
            for col in range(4):
                check_num = self.board[row][col]
                if self.board[row+1][col] == check_num:
                    return True
        return False
    
    def turn(self, direction):
        num_of_moves = self.move(direction)
        if num_of_moves > 0:
            self.rand_insert()
            self.turnNum += 1
        if self.avail_moves_check() == False:
            print("Game Over")
       
                

        
            
            

import numpy as np
from pynput import keyboard
from random import randint
from time import sleep

class twenty_forty_eight:
    def __init__(self, ID):
        self.ID = ID
        self.turnNum = 0
        self.board = np.array([[0 for i in range(4)] for x in range(4)], int)
        self.score = 0
        
    def __repr__(self):
        print_str = f'Game = {self.ID}\nTurns = {self.turnNum}\n'
        for x in self.board:
            for y in x:
                print_str += '[{:^6}]'.format(y) if y != 0 else '[      ]'
            print_str += '\n'
        return print_str

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
    
    def move(self): # Moves elements up
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

    def rand_insert(self): # insert starting integer into random empty element
        avail_space_dict = twenty_forty_eight.empty_spaces(self)
        
        # when bool() is used on empty dictionary in python it returns False
        if bool(avail_space_dict) == True:                  
            randNum = randint(1, len(avail_space_dict))
            randCoords = avail_space_dict[randNum]
            self.board[randCoords[0]][randCoords[1]] = 2    # num inserted
    
    def turn(self, num_of_moves):
        if num_of_moves > 0:
            self.rand_insert()
        elif num_of_moves == 0:
            print('BAD MOVE, NO NEW NUM ADDED')
            return
        self.turnNum += 1
        print(self)
        
        if len(self.empty_spaces()) == 0:
            possible_moves = 0
            # Fast way of making a copy of a 2D array without references
            arr_copy = np.array([row[:] for row in self.board])
            # Tests all moves for a valid move
            for x in range(4):
                self.arr_transpose(x)
                possible_moves += self.move()
                if possible_moves > 0:
                    self.board = np.array([row[:] for row in arr_copy])
                    break
            if possible_moves == 0:
                print('No possible moves remaining')
                gameOver = ('G','A','M','E','O','V','E','R')
                for x in gameOver:
                    print(x)
                    sleep(0.2)
                exit(None)
def main():
    game_board = twenty_forty_eight(1)
    
    # Adds two numbers into the array in randomised spaces
    for x in range(2):
        game_board.rand_insert()
    print(game_board)

    def on_press(key):
        if key == keyboard.Key.up:
            i = 0
        elif key == keyboard.Key.left:
            i = -3
        elif key == keyboard.Key.down:
            i = -2
        elif key == keyboard.Key.right:
            i = -1
        elif key == keyboard.Key.esc:
            return False
        else:
            return
        game_board.arr_transpose(abs(i))
        moves_taken = game_board.move()
        game_board.arr_transpose(i)
        game_board.turn(moves_taken)
        
    with keyboard.Listener(on_press = on_press) as listener:
        listener.join()



if __name__ == '__main__':
    main()
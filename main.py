from pynput import keyboard
from random import randint
from time import sleep


def main():
    board_arr = [[None,None,None,None],[None,None,None,None],[None,None,None,None],[None,None,None,None]]
    
    for x in range(2):          # Adds two numbers into the array in randomised spaces to start off the game
        rand_insert(board_arr)
    
    print_arr(board_arr)

    def on_press(key):

        if key == keyboard.Key.right:
            empty_spaces = moveRight(board_arr)
            turn(board_arr, empty_spaces)
        elif key == keyboard.Key.left:
            empty_spaces = moveLeft(board_arr)
            turn(board_arr, empty_spaces)
        elif key == keyboard.Key.up:
            empty_spaces = moveUp(board_arr)
            turn(board_arr, empty_spaces)
        elif key == keyboard.Key.down:
            empty_spaces = moveDown(board_arr)
            turn(board_arr, empty_spaces)
        elif key == keyboard.Key.esc:
            return False
        else:
            pass


    with keyboard.Listener(on_press = on_press) as listener:
        listener.join()

def print_arr(board_arr):
    item_string = '[{:^8}]' # Board space formatting
    print_string = '\n\n'
    for row in board_arr:   # Builds the board to be printed
        for item in row:
            if item == None:
                print_string += item_string.format('')
            else:
                print_string += item_string.format(str(item))
        print_string += '\n\n'
    print(print_string)

def rand_insert(board_arr): # Used to insert a starting integer into a random empty element
    avail_space_dict = {}
    rowNum = 0
    colNum = 0
    i = 1
    for row in board_arr:
        colNum = 0
        for item in row:
            if item == None:
                avail_space_dict[i] = (rowNum, colNum)
                i+=1
            colNum += 1
        rowNum += 1
    if bool(avail_space_dict) == True:                  # when bool() is used on an empty dictionary in python it returns False
        randNum = randint(1, len(avail_space_dict))     # this is an easy way to tell if there are any spaces left in the array
        #print(avail_space_dict)
        #print(randNum)
        randCoords = avail_space_dict[randNum]

        board_arr[randCoords[0]][randCoords[1]] = 2
    #print(len(avail_space_dict))
    return len(avail_space_dict)


def elementChanger(board_arr, item, rowNum, colNum, desiredRow, desiredCol):
    tempItem = abs(item)
    board_arr[rowNum][colNum]= None
    board_arr[desiredRow][desiredCol] = abs(tempItem)

def rowChecker(board_arr, rowCheck, rowNum, colNum, attitude, num_checked): # attitude = +/-1 depending on the direction
    desiredRow = abs(rowCheck)                                              # UP and LEFT are +1 as they need to check the space in that direction in relation to themselves,
    if board_arr[rowCheck][colNum] == None:                                 # i.e the space above or to the left due to the way the software navigates searching the array.
        return False, False, True, desiredRow                               # DOWN and RIGHT are -1 for the same reasons as their search needs to be inverted
    elif board_arr[rowCheck][colNum] == board_arr[rowNum][colNum]:
        return True, True, True, desiredRow
    elif board_arr[rowCheck][colNum] != board_arr[rowNum][colNum]:
        if num_checked == 0:
            return True, False, False, desiredRow
        return True, False, True, desiredRow+attitude
    else:
        return False, False, False, desiredRow
    
def colChecker(board_arr, colCheck, rowNum, colNum, attitude, num_checked):              
    desiredCol = abs(colCheck)                                              
    if board_arr[rowNum][colCheck] == None:                                 # If the space is empty, a move is needed but search is not fin
        return False, False, True, desiredCol
    elif board_arr[rowNum][colCheck] == board_arr[rowNum][colNum]:          # If the space is the same a merge is needed and the search is fin
        return True, True, True, desiredCol
    elif board_arr[rowNum][colCheck] != board_arr[rowNum][colNum]:          # If the space is not the same no merge is needed and the search is fin
        if num_checked == 0:
            return True, False, False, desiredCol
        return True, False, True, desiredCol+attitude
    else:
        return False, False, False, desiredCol
    

def moveUp(board_arr):
    rowNum = 1
    colNum = 0
    num_of_moves = 0
    for row in board_arr[1:]:   # Moves down the rows starting at the second row
        colNum = 0
        for item in row:    # Moves right on the full row
            if item != None:
                num_checked = 0
                for rowCheck in reversed(range(rowNum)):
                    finished, mergeReq, changeReq, desiredRow = rowChecker(board_arr, rowCheck, rowNum, colNum, 1, num_checked)
                    if finished == True:
                        break
                    num_checked += 1

                itemMultiplier = 2 if mergeReq == True else 1
                if changeReq == True:
                    elementChanger(board_arr, (item*itemMultiplier), rowNum, colNum, desiredRow, colNum)
                    num_of_moves += 1
            colNum += 1
        rowNum += 1

    return num_of_moves
            
def moveDown(board_arr):
    rowNum = 2
    colNum = 3
    num_of_moves = 0
    for row in reversed(board_arr[:3]): # Moves up the rows starting from the third row
        colNum = 3
        for item in reversed(row):  # Moves left on the full row
            if item != None:
                num_checked = 0
                for rowCheck in range(rowNum+1, len(board_arr)):
                    finished, mergeReq, changeReq, desiredRow = rowChecker(board_arr, rowCheck, rowNum, colNum, -1, num_checked)
                    if finished == True:
                        break
                    num_checked += 1
                
                itemMultiplier = 2 if mergeReq == True else 1
                if changeReq == True:
                    elementChanger(board_arr, (item*itemMultiplier), rowNum, colNum, desiredRow, colNum)
                    num_of_moves += 1
            colNum -= 1
        rowNum -= 1
    return num_of_moves

def moveLeft(board_arr):
    rowNum = 0
    colNum = 1
    num_of_moves = 0
    for row in board_arr:   # Moves down all the rows
        colNum = 1
        for item in row[1:]: # Moves right on the row starting at the second element
            if item != None:
                num_checked = 0
                for colCheck in reversed(range(colNum)):
                    finished, mergeReq, changeReq, desiredCol = colChecker(board_arr, colCheck, rowNum, colNum, 1, num_checked)
                    if finished == True:
                        break
                    num_checked += 1
                
                itemMultiplier = 2 if mergeReq == True else 1
                if changeReq == True:
                    elementChanger(board_arr, (item*itemMultiplier), rowNum, colNum, rowNum, desiredCol)
                    num_of_moves += 1
            colNum += 1
        rowNum += 1
    return num_of_moves

def moveRight(board_arr):
    rowNum = 0
    colNum = 2
    num_of_moves = 0
    for row in board_arr:   # Moves down all the rows
        colNum = 2
        for item in reversed(row[:3]):  # Moves left on the row starting on the third element
            if item != None:
                num_checked = 0
                for colCheck in range(colNum+1, len(board_arr)):
                    finished, mergeReq, changeReq, desiredCol = colChecker(board_arr, colCheck, rowNum, colNum, -1, num_checked)
                    if finished == True:
                        break
                    num_checked += 1
                
                itemMultiplier = 2 if mergeReq == True else 1
                if changeReq == True:
                    elementChanger(board_arr, (item*itemMultiplier), rowNum, colNum, rowNum, desiredCol)
                    num_of_moves += 1
            colNum -= 1
        rowNum += 1
    return num_of_moves

    
def turn(board_arr, num_of_moves):
    if num_of_moves > 0:                            # Stops the game adding in another new number if nothing changes, stops cheating
        freeSpaces = rand_insert(board_arr)
    else:
        print('BAD MOVE, NO NEW NUM ADDED')
        freeSpaces = 0
        
    print_arr(board_arr)

    if freeSpaces == 0:     # Checks to see if there's any moves left, only if there's no free spaces in the array
        num_of_possible_moves = 0
        arr_copy = [row[:] for row in board_arr]    # Fast way of making a copy of a 2D array without references
        moveDict = {
            '1' : moveUp,
            '2' : moveDown,
            '3' : moveRight,
            '4' : moveLeft
        }
        for x in moveDict:  # Goes through all possible moves to test for validity
            num_of_possible_moves += moveDict[x](arr_copy)
            if num_of_possible_moves > 0:
                break
        if num_of_possible_moves == 0:
            print('No possible moves remaining')
            gameOver = ('G','A','M','E','O','V','E','R')
            for x in gameOver:
                print(x)
                sleep(0.2)
            exit(None)
            return True
    return False    


if __name__ == '__main__':
    main()




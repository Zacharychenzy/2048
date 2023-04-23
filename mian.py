import os
import random

#//////////STYLE CLASSES//////////
#create classes to differentiate different types of style
#create variables inside the class to call the terminal commands easier (ex. \033[0m' -- RESET_FG)
#call the styles by using: (class name).(variable name inside the class)

#font style
#change the font style
class style():
    #some font styles
    BOLD        = '\033[1m'
    DIM         = '\033[2m'
    NORMAL      = '\033[22m'
    #reset foreground and background styles
    RESET_FG    = '\033[0m'
    RESET_BG    = '\033[49m'
    
#foreground color
#change the font color
class fg_style():
    BLACK       = '\033[30m'
    RED         = '\033[31m'
    GREEN       = '\033[32m'
    YELLOW      = '\033[33m'
    BLUE        = '\033[34m'
    MAGENTA     = '\033[35m'
    CYAN        = '\033[36m'
    WHITE       = '\033[37m'
    UNDERLINE   = '\033[4m'

#background color
#change the background color
class bg_style():
    BLACK       = '\033[40m'
    RED         = '\033[41m'
    GREEN       = '\033[42m'
    YELLOW      = '\033[43m'
    BLUE        = '\033[44m'
    MAGENTA     = '\033[45m'
    CYAN        = '\033[46m'
    WHITE       = '\033[47m'

#//////////ALL DIFFERENT KINDS OF FUNCTIONS//////////
#print functions: print or erease things
#feedback functions: to print out some feedback to user such as rules
#status functions: check the game status for example if player win or loose
#motion functions: move the matrix by shifting, rotating, merging etc.

#---print functions---

#print list function
#/////check and print different styles according to different numbers inside the matrix/////
def print_mat(mat):
    for x in range(4):
        for y in range(4):
            #by using end = "" at the end of print, it will continue next print at the end
            #check which number it is
            if mat[x][y] == 0:
                #give a style to the number
                print (style.BOLD + fg_style().BLACK + str(mat[x][y]), end = "")
                #loop number of times base on the length of the number, longer it is lesser space at the end
                for i in range(4 - len(str(mat[x][y]))):
                    #print the spaces after each number
                    print(style.RESET_BG + style.RESET_FG + " ", end = "")
            
            if mat[x][y] == 2:
                print (style.BOLD + fg_style().YELLOW + str(mat[x][y]), end = "")
                for i in range(4 - len(str(mat[x][y]))):
                    print(style.RESET_BG + style.RESET_FG + " ", end = "")
            
            if mat[x][y] == 4:
                print (style.BOLD + fg_style().BLUE + str(mat[x][y]), end = "")
                for i in range(4 - len(str(mat[x][y]))):
                    print(style.RESET_BG + style.RESET_FG + " ", end = "")
            
            if mat[x][y] == 8:
                print (style.BOLD + fg_style().GREEN + str(mat[x][y]), end = "")
                for i in range(4 - len(str(mat[x][y]))):
                    print(style.RESET_BG + style.RESET_FG + " ", end = "")
            
            if mat[x][y] == 16:
                print (style.BOLD + fg_style().CYAN + str(mat[x][y]), end = "")
                for i in range(4 - len(str(mat[x][y]))):
                    print(style.RESET_BG + style.RESET_FG + " ", end = "")
            
            if mat[x][y] == 32:
                print (style.BOLD + fg_style().MAGENTA + str(mat[x][y]), end = "")
                for i in range(4 - len(str(mat[x][y]))):
                    print(style.RESET_BG + style.RESET_FG + " ", end = "")
            
            if mat[x][y] == 64:
                print (style.BOLD + fg_style().RED + str(mat[x][y]), end = "")
                for i in range(4 - len(str(mat[x][y]))):
                    print(style.RESET_BG + style.RESET_FG + " ", end = "")
            
            if mat[x][y] == 128:
                print (style.BOLD + bg_style().YELLOW + fg_style().WHITE + str(mat[x][y]), end = "")
                for i in range(4 - len(str(mat[x][y]))):
                    print(style.RESET_BG + style.RESET_FG + " ", end = "")
            
            if mat[x][y] == 256:
                print (style.BOLD + bg_style().BLUE + fg_style().WHITE + str(mat[x][y]), end = "")
                for i in range(4 - len(str(mat[x][y]))):
                    print(style.RESET_BG + style.RESET_FG + " ", end = "")
            
            if mat[x][y] == 512:
                print (style.BOLD + bg_style().GREEN + fg_style().WHITE + str(mat[x][y]), end = "")
                for i in range(4 - len(str(mat[x][y]))):
                    print(style.RESET_BG + style.RESET_FG + " ", end = "")
            
            if mat[x][y] == 1024:
                print (style.BOLD + bg_style().CYAN + fg_style().WHITE + str(mat[x][y]), end = "")
                for i in range(4 - len(str(mat[x][y]))):
                    print(style.RESET_BG + style.RESET_FG + " ", end = "")
            
            if mat[x][y] == 2048:
                print (style.BOLD + bg_style().RED + fg_style().WHITE + str(mat[x][y]), end = "")
                for i in range(4 - len(str(mat[x][y]))):
                    print(style.RESET_BG + style.RESET_FG + " ", end = "")
        print("")

#clear function
#/////clear the printing in the console using os library with keyword "clear"/////
def clearConsole():
    os.system("clear")

#---feedback functions---

#rule function
#/////introduce player the basics of the game/////
def startGame():
    #some simple game rule
    print(style.BOLD + "Welcome to 2048!")
    print(style.BOLD + "Use 'W' 'A' 'S' 'D' commands to move the tiles.")
    print(style.BOLD + "Press 'Enter' after each command")
    print(style.BOLD + "Tiles with the same number merge into one when they touch.")
    print(style.BOLD + "Add them up to reach 2048!")
    #controles you use in the game
    print(style.BOLD + "Commands are as follows : ")
    print(style.BOLD + fg_style().RED + "'W'" + style.RESET_FG + style.BOLD + " : Move Up")
    print(style.BOLD + fg_style().RED + "'S'" + style.RESET_FG + style.BOLD + " : Move Down")
    print(style.BOLD + fg_style().RED + "'A'" + style.RESET_FG + style.BOLD + " : Move Left")
    print(style.BOLD + fg_style().RED + "'D'" + style.RESET_FG + style.BOLD + " : Move Right")
    #let player start the game
    start = input(style.BOLD + "Press enter to start.")

#win function
#/////if the player won it will print the following/////
def win():
    print(style.BOLD + "CONGRATULATION!")
    print(style.BOLD + "YOU WON!")

#loose function
#/////if the player lost it will print the following/////
def lost():
    print(style.BOLD + "You Lost")
    print(style.BOLD + "Nice Try...")

#---status functions---

#win game function
#/////check if the player won the game by checking if the player reached "2048"/////
def winGame(mat):
    win = False
    for x in range(4):
        for y in range(4):
            #check each index if it equals to "2048"
            if mat[x][y] == 512:
                win = True
    return win

#loose game function
#/////check if the player lost the game by checking if theres any changes to the matrix after each move/////
def lostGame(mat):
    lost = False
    #checking if the playing can move by using all the motion functions
    if up(mat) == mat and down(mat) == mat and left(mat) == mat and right(mat) == mat:
        lost = True
    return lost

#full mat function
#/////check if the matirx is full so that there wont be anymore new "2"s adding in/////
def full(mat):
    full = True
    for x in range(4):
        for y in range(4):
            #check if there is any spaces
            if mat[x][y] == 0:
                full = False
    return full

#score function
#/////count the score of the player/////
def count():
    global score
    score += 2

#---motions funcitons---

#add two function
#/////add a new "2" in the matrix randomly if there is space/////
def addTwo(mat):
    temp_mat = mat
    #check if there is space by using full mat function
    while not full(mat):
        #pick random spot for both role and colume, (0, 3) is 0, 1, 2, 3
        role = random.randint(0, 3)
        colume = random.randint(0, 3)
        #check if the spot if available
        while(mat[role][colume] != 0):
            #if not repick the spot
            role = random.randint(0, 3)
            colume = random.randint(0, 3)
        #assign the "2" to its position
        temp_mat[role][colume] = 2
        break
    return temp_mat

#rotate function
#/////rotate the matirx colckwise with the number of times based on which direction the player is shifting/////
def spin(mat, nums):
    new_mat = mat
    for i in range(nums):
        #rotate the matrix
        #"[::-1]" makes a copy of the original list in reverse order, can also use list.reversed()
        #"*" makes each sublist in the original list a separate argument to zip(), in general it unzip the list so that it can be used zip() function
        #"zip()" takes one item from each argument and makes a list, this will rotate the matirx
        temp_mat = list(zip(*new_mat[::-1]))
        '''
        original mat
        [0 1 4 0]
        [7 8 3 9]
        [8 4 0 7]
        [2 1 0 5]
        
        [::-1] mat
        [2 1 0 5]
        [8 4 0 7]
        [7 8 3 9]
        [0 1 4 0]
        
        zip() mat
        [2 8 7 0]
        [1 4 8 1]
        [0 0 3 4]
        [5 7 9 0]
        '''
        #renew the matrix for the next rotation
        new_mat = temp_mat
    return temp_mat

#shift function
#/////shift every number in the matrix upward to the top until theres no more spaces in between/////
def shift(mat):
    #create an empty matrix to store the shifted number
    temp_mat = []
    for i in range(4):
        temp_mat.append([0] * 4)
    
    for x in range(4):
        #blank index for the next shift
        blank = 0
        for y in range(4):
            #check colume by colume ([y][x]) if there is a number
            if mat[y][x] != 0:
                #if so then move the number
                temp_mat[blank][x] = mat[y][x]
                #update the next blank spot
                blank += 1
    return temp_mat

#merge function
#/////merge two numbers if they are the same when shifting/////
def combine(mat):
    temp_mat = mat
    for x in range(4):
        #repeat only 3 times here because you wont be checking the last index due to theres no more index after it
        for y in range(3):
            #check if the number and the one follwing are the same
            #they also cant be 0
            if mat[y][x] == mat[y+1][x] and mat[y][x] != 0:
                #merge the number and clear the second one and clear the following one
                temp_mat[y][x] = mat[y][x] * 2
                temp_mat[y+1][x] = 0
                mat = temp_mat
                count()
    return temp_mat

#move function
#/////this function will shift the matrix and then merge the numbers, after merging it will shift again to make sure theres no sapce in between, last it will generate a 2 randomly/////
#this a super function that just calls all other function and run them one by one, it is also for us to manage the code#
def move(mat):
    temp_mat = mat
    temp_mat = shift(mat)
    temp_mat = combine(temp_mat)
    temp_mat = shift(temp_mat)
    temp_mat = addTwo(temp_mat)
    return temp_mat

#derection functions
#/////base on which direction the player want to go, spin the matrix until its facing upward, call the move function to shift, merge, and add a new "2", spin the matrix back to original position/////
#up function
def up(mat):
    mat = move(mat)
    mat = spin(mat, 4)
    return mat

#down function
def down(mat):
    mat = spin(mat, 2)
    mat = move(mat)
    mat = spin(mat, 2)
    return mat

#left function
def left(mat):
    mat = spin(mat, 1)
    mat = move(mat)
    mat = spin(mat, 3)
    return mat

#right function
def right(mat):
    mat = spin(mat, 3)
    mat = move(mat)
    mat = spin(mat, 1)
    return mat

#detect function
#/////determine which direction does the player want to push toward/////
def direction():
    if(x.lower() == "w"):
        return up(mat)
    elif(x.lower() == "s"):
        return down(mat)
    elif(x.lower() == "a"):
        return left(mat)
    elif(x.lower() == "d"):
        return right(mat)

#//////////MAIN//////////
#call out the rules
startGame()

#clear the rules
clearConsole()

#create a empty matirx
mat = []
for i in range(4):
    mat.append([0] * 4)

#create a score count
score = 0

#put a "2" in the matrix
mat = addTwo(mat)

#if not won then loop forever
while not winGame(mat):
    #check if lost 
    if lostGame(mat):
        #if so then print how the player lost and call out the loosing screen
        print_mat(mat)
        lost()
        break
    
    #print the matrix and the score at the beginning of each loop so player knows what to do next
    print_mat(mat)
    print(style.RESET_FG + style.BOLD + "Your Score is: " + str(score))
    
    #make sure player enter a valid command
    while True:
        x = input(style.RESET_FG + style.BOLD + "Press the command : ")
        #not random letter
        if (x.lower() not in "wasd"):
            print("Use only 'W' 'A' 'S' 'D' to move the tiles.")
        #not just "Enter"
        elif (x == ""):
            print("Please Enter Something")
        #not more than one letter
        elif (len(x) > 1):
            print("Please Enter one character")
        else:
            break
    
    #clear whats printed at the end of the loop
    clearConsole()
    
    #update the matrix for next loop
    mat = direction()

#check if the break is cause by win or loose
if winGame(mat):
    #if so then print how the player win and call out the winning screen
    print_mat(mat)
    win()

import random


shipDict = {
    1 : [2,1],
    2 : [3,1],
    3 : [4,1],
}

def cls():
    for _ in range(32): print()

def SetShip(map,row,col,length,width):
    if col+length > len(map) or row+width > len(map):
        return False
    for i in range(width):
        if map[row+i][col]=='X':
            return False
    for i in range(length):
        if map[row][col+i]=='X':
            return False
    for i in range(width):
        for j in range(length):
            map[row+i][col+j] = 'X'
    return True

def NewEmptyMap(size):
    map = []
    for i in range(size):
        new_Row = []
        for j in range(size):
            new_Row += [' ']
        map.append(new_Row)
    return map

def NewEnemyMap(size):
    enemy_map = NewEmptyMap(size)

    for key in shipDict.keys():
        while True:
            rand_row = random.randint(0,size-1)
            rand_col = random.randint(0,size-1)
            rand_dir = random.randint(0,1) #0-Horizontal , 1-Vertical
            if(rand_dir==0):
                if SetShip(enemy_map,rand_row,rand_col,shipDict[key][0],shipDict[key][1]):
                    break
            elif(rand_dir==1):
                if SetShip(enemy_map,rand_row,rand_col,shipDict[key][1],shipDict[key][0]):
                    break
    return enemy_map

def PrintMap(map):
    print(" ",end="")
    for col in range(len(map[0])):
        print("  "+str(col) , end = " ")
    print()
    for row in range(len(map)):
        print(row, end="")
        for col in range(len(map[row])):
            print("| " + map[row][col], end=' ')
        print("|")

def GetIntInput(prompt):
    while True:
        number = input(prompt)
        if number == 'e!':
            print('\n')
            print('{:^114}'.format(f'---> Exit Game ! <---'))
            print('\n')
            return 'e!'
        try:
            number = int(number)
            # print('mnatep')
            return number
        except ValueError:
            print("Please Insert Integer !")

def SetPlayerShip(size):

    playerMap = NewEmptyMap(size)

    cls()
    PrintMap(playerMap)
    for key in shipDict.keys():
        print(f"Setup your Battleship (ship length : {str(shipDict[key][0])})")
        while True:
            row = GetIntInput("Insert Row Number : ")
            if row == 'e!': return 'e!'
            col = GetIntInput("Insert Col Number : ")
            if col == 'e!': return 'e!'

            while True:
                dir = GetIntInput("Insert Dir Number [ 0-Right , 1-Down ] : ")
                if dir == 'e!': return 'e!'
                if dir != 0 and dir != 1:
                    print('Invalid Input ! Please Type 0 or 1')
                elif dir == 0 or dir == 1: break
            
            if dir == 0:
                if SetShip(playerMap, row, col, shipDict[key][0], shipDict[key][1]):
                    break
            elif dir == 1:
                if SetShip(playerMap, row, col, shipDict[key][1], shipDict[key][0]):
                    break
            
            print("Cell is not available !")
        cls()
        PrintMap(playerMap)

    input("Your Setup is Complete. Press ENTER to Continue ...")
    return playerMap

def PlayerShoot(shownMap,CheckMap,bulletNum, name):

    for i in range(bulletNum):
        while True:
            cls()
            PrintMap(shownMap)
            print(f"{name}'s Turn to Attack ! (" + str(bulletNum-i) +")")
            row = GetIntInput("Target Row : ")
            if row == 'e!': return 'e!'
            col = GetIntInput("Target Col : ")
            if col == 'e!': return 'e!'
            
            if row< len(shownMap) and col<len(shownMap):
                if shownMap[row][col] == ' ':
                    if CheckMap[row][col] == 'X':
                        shownMap[row][col] = 'O'
                        if not CheckEnemyAlive(shownMap, CheckMap):
                            return True
                    else :
                        shownMap[row][col] = '-'
                    break
                else :
                    input('Target Already Shot. Press ENTER to Continue ...')
            else :
                input('Row or Column is Out of Bounds. Press ENTER to Continue ...')
        cls()
        PrintMap(shownMap)
    return False

def EnemyShoot(playerMap,bulletNum):
    opt = input("Enemy's Turn to Attack ! Press ENTER to Continue ...")
    if opt == 'e!': return 'e!'
    
    for i in range(bulletNum):
        while True:
            cls()
            PrintMap(playerMap)
            row = random.randint(0,len(playerMap)-1)
            col = random.randint(0,len(playerMap)-1)
            if playerMap[row][col] != '-' and playerMap[row][col] != 'O':
                if playerMap[row][col] == 'X':
                    playerMap[row][col] = 'O'
                    if not CheckPlayerAlive(playerMap):
                        return True
                else:
                    playerMap[row][col] = '-'

                input(f"Enemy is attacking ({str(row)},{str(col)}) ! Press ENTER to Continue ...")
                cls()
                break
    return False

def CheckPlayerAlive(playerMap) :
    for row in range(len(playerMap)):
        for col in range(len(playerMap)):
            if(playerMap[row][col] == 'X'):
                return True
    return False


def CheckEnemyAlive(shownMap,enemyMap):
    for row in range(len(enemyMap)):
        for col in range(len(enemyMap)):
            if enemyMap[row][col]=='X' and shownMap[row][col]==' ':
                return True
    return False

def rules_battleship():
    rulesb = '''
Battleship:
In this game of Battleship, you will try to guess the location of ships your enemy had placed on a board. 
You will be given 6 chances to guess the location in every turn. 
If you can guess all the locations of your enemy’s ship before they can, you will win the game.

Instructions:
1. To start the game, the system will ask the player what size of board they want to play in. 
   It can be a number from 4 - 10. The number imputed will be the number of rows and columns in the board. 
   If the player inputs an invalid number or any invalid input, the system will ask for another input. 
2. Next, setting up the board is necessary. 
   The player will hide 3 ships within his/her board, each ship will have a different length (2, 3, 4) and the width of 1. 
   The player will first input the row, column and direction (right/ down) for the ship with the length of 2. 
   The same will be done for the ships of length 3 and 4.
3. After setting up its board, the game will commence. 
   The player will guess the enemy’s ships’ location by inputting the row and column in the board shown. 
   The board will automatically update the board if the player succeeds in encountering the enemy’s ship 
   by replacing them with an ‘O’.  
   If the player can guess all the coordinates of the enemy’s ships one by one before the enemy does, 
   the player will win the game.
4. Happy playing!'''
    return rulesb

def BattleShip(name):
    cls()
    print('''
    ▒█░░▒█ █▀▀ ▒█░░░ ▒█▀▀█ █▀▀█ ▒█▀▄▀█ █▀▀ 　 ▀▀█▀▀ █▀▀█ 　 ▒█▀▀█ █▀▀█ ▀▀█▀▀ ▀▀█▀▀ ▒█░░░ █▀▀ ▒█▀▀▀█ ▒█░▒█ ░▀░ ▒█▀▀█ 
    ▒█▒█▒█ █▀▀ ▒█░░░ ▒█░░░ █░░█ ▒█▒█▒█ █▀▀ 　 ░▒█░░ █░░█ 　 ▒█▀▀▄ █▄▄█ ░▒█░░ ░▒█░░ ▒█░░░ █▀▀ ░▀▀▀▄▄ ▒█▀▀█ ▀█▀ ▒█▄▄█ 
    ▒█▄▀▄█ ▀▀▀ ▒█▄▄█ ▒█▄▄█ ▀▀▀▀ ▒█░░▒█ ▀▀▀ 　 ░▒█░░ ▀▀▀▀ 　 ▒█▄▄█ ▀░░▀ ░▒█░░ ░▒█░░ ▒█▄▄█ ▀▀▀ ▒█▄▄▄█ ▒█░▒█ ▀▀▀ ▒█░░░
    ''')
    print('{:^114s}'.format(f'-------------> Hello {name}, Best of Luck ! <-------------'))
    print('{:^114s}'.format(f"press ENTER to continue or 'r' to read the rules"))
    mopt = input()
    cls()

    while True:
        if mopt == 'r': 
            print(rules_battleship())
            print('{:^114s}'.format(f"press ENTER to continue or 'r' to read the rules"))
        else: break
        mopt = input()
        cls()
        
    while True:
        size = GetIntInput("Insert Board Size (4-10) : ")
        if size == 'e!': return 'e!'
        elif 4 <= size <= 10: break
        else:
            print('Please Select Within (4-10) !')

    enemyMap = NewEnemyMap(size)
    shownEnemyMap = NewEmptyMap(size)
    playerMap = SetPlayerShip(size)
    if playerMap == 'e!': return 'e!'

    while True:
        # print("Enemy Map : ")
        # PrintMap(shownEnemyMap)
        # print("Your Map : ")
        # PrintMap(playerMap)

        ps = PlayerShoot(shownEnemyMap,enemyMap,6,name)
        if ps == 'e!': return 'e!'
        if ps:
            print("Enemy Map : ")
            PrintMap(shownEnemyMap)
            print("\n\nPlayer Win !")
            return

        elif EnemyShoot(playerMap, 6):
            print("Your Map : ")
            PrintMap(playerMap)
            print("\n\nEnemy Win !")
            return

# BattleShip()

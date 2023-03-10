from hangman import *
from battleship import *

def spaces(): 
    for _ in range(32): print()

def main():
    username =  input('Enter Your Username ... \n---> ').title()
    spaces()
    
    while True:
        print(f'Welcome {username}, Please Select a Game ...')
        gamemode = input('1 : Hangman \n2 : Battle Ship \n---> ')
        while True:
            if gamemode != '1' and gamemode != '2':
                spaces()
                print("Please Enter 1 or 2 !")
                gamemode = input('Select a Game ... \n1 : Hangman \n2 : Battle Ship \n---> ')
            else: break

        gamemode = int(gamemode)
        if gamemode == 1:
            Hangman(username)
        elif gamemode == 2:
            BattleShip(username)
        
        while True:
            opt = input('Play Again ? (y/n)\n---> ')
            spaces()
            if opt == 'n':
                spaces()
                print('''
    ▀▀█▀▀ ▒█░▒█ █▀▀█ ▒█▄░▒█ ▒█░▄▀ ▒█▀▀▀█ 　 ▒█▀▀▀ █▀▀█ ▒█▀▀█ 　 ▒█▀▀█ ▒█░░░ █▀▀█ ▒█░░▒█ ░▀░ ▒█▄░▒█ ▒█▀▀█ 　 █ 
    ░▒█░░ ▒█▀▀█ █▄▄█ ▒█▒█▒█ ▒█▀▄░ ░▀▀▀▄▄ 　 ▒█▀▀▀ █░░█ ▒█▄▄▀ 　 ▒█▄▄█ ▒█░░░ █▄▄█ ▒█▄▄▄█ ▀█▀ ▒█▒█▒█ ▒█░▄▄ 　 ▀ 
    ░▒█░░ ▒█░▒█ ▀░░▀ ▒█░░▀█ ▒█░▒█ ▒█▄▄▄█ 　 ▒█░░░ ▀▀▀▀ ▒█░▒█ 　 ▒█░░░ ▒█▄▄█ ▀░░▀ ░░▒█░░ ▀▀▀ ▒█░░▀█ ▒█▄▄█ 　 ▄''')
                print('\n\n')
                return

            elif opt == 'y': 
                break
            
            else:
                print("Please Enter 'y' or 'n' !")

main()


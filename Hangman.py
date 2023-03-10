import random

dict = {
    "Fruits" : ["Apple","Banana","Orange", "Pear", "Grapefruit", "Mandarin", "Lime", "Lemon", "Apricot", "Kiwi", "Peach", "Plum", "Nectarine", "Mango", "Strawberry", "Raspberry", "Blueberry", "Passionfruit", "Watermelon", "Melons", "Tomato", "Avocado", "Lychee", "Dragon fruit", "Pineapple", "Durian", "Guava", "Grape", "Pomegranates", "Cherry", "Coconut", "Pomelo", "Yuzu", "Starfruit", "Longan", "Papaya", "Fig", "Jackfruit", "Soursop", "Persimmon", "Mulberry", "Tamarind", "Cranberry", "Mangosteen","Star fruit","Passion Fruit","Black Plum"],
    "Flowers" : ["Rose","Tulip", "Bluebell", "Daffodil", "Poppy", "Sunflower", "Dandelion", "Hyacinth", "Daisy", "Snowdrop", "Crocus", "Orchid", "Cherry Blossom", "Iris", "Peony", "Chrysanthemum", "Geranium", "Lily", "Lotus", "Water Lily", "Periwinkle", "Narcissus", "Marigold", "Lavender", "Calendula", "Acacia", "Magnolia", "Jasmine", "Oleander", "Anthurium", "Anemone", "Alstroemeria", "Amaryllis", "Anemone", "Bouvardia", "Heather", "Larkspur", "Hydrangea", "Gladiolus"],
    "Animals" : ["Cat","Dog","Bird", "Llama", "Lynx", "Mole", "Monkey", "Mouse", "Narwhal", "Orangutan", "Horse", "Otter", "Ox", "Pig", "Polar Bear", "Porcupine", "Puma", "Rabbit", "Raccoon", "Rat", "Rhinoceros", "Sheep", "Tiger", "Walrus", "Weasel", "Wolf", "Zebra", "Fish", "Crab", "Tiger", "Eagle", "Ostrich", "Vulture", "Kangaroo", "Snake", "Bear", "Hippopotamus", "Antelope", "Lion", "Gorilla", "Giraffe", "Elephant", "Jaguar", "Cow", "Turtle", "Duck", "Swan", "Goose", "Pig"],
    "Countries" : ["Indonesia", "South Korea", "Australia", "Ukraine", "Russia", "Netherlands", "Britain", "France", "Italy", "Germany", "Spain", "Poland", "Belgium", "Switzerland", "Sweden", "Austria", "Turkey", "Romania", "Belarus", "Norway", "India", "China", "Canada", "Hong Kong", "Denmark", "Ireland", "Finland", "Cambodia", "Laos", "Malaysia", "Singapore", "Myanmar", "Vietnam", "Argentina", "Japan", "Brazil", "Poland", "Pakistan", "India","Brunei Darussalam","East Timor","El Savador"," New Zealand", "North Korea", "The Bahamas"," United Kingdom", "Vatican City","Dominican Republic","Costa Rica", "Czech Republic", "Saudi Arabia", "South Africa", "Sri Lanka"],
    "Capital City":["Beijing", "Budapest", "Berlin", "Canberra", "Phnom Penh", "Bogota", "Denver", "Cairo", "London", "Paris", "Seoul", "Dublin", "Kingston", "Rome", "Nairobi", "Kuala Lumpur", "Mexico City", "Monaco", "Oslo", "Panama City", "Stockholm", "Taipei", "Bangkok", "Abu Dhabi", "Hanoi", "Singapore", "Edinburgh", "Victoria", "Madrid", "Lisbon", "Manila", "San Marino", "Pyongyang", "New Delhi", "Havana", "Santiago", "Prague", "Helsinki", "Guatemala City"],
    "Vegetables":["Asparagus", "Avocado", "Beet", "Bok Choy", "Broccoli", "Brussels Sprouts", "Cabbage", "Carrots", "Celery", "Corn", "Cucumbers", "Garlic", "Lettuce", "Beans", "Mushrooms", "Onions", "Green Onions", "Peas", "Pumpkin", "Peppers", "Potatoes", "Pumpkin", "Radish","Spinach","Tomatoes", "Zucchini", "Onion"]
}

def GetCharInput(prompt):
    while True:
        char = input(prompt)
        if char == 'e!':
            print('\n')
            print('{:^101s}'.format(f'---> Exit Game ! <---'))
            print('\n')
            return 'e!'

        if char.isalpha():
            if(len(char)>1):
                print("1 Letter Only !")
            else :
                return char
        else: print('Please Insert Letter Only !')
        print('')

def IntInput(prompt):
    while True:
        number = input(prompt)
        if number == 'e!': return 'e!'
        try:
            number = int (number)
            return number
        except ValueError:
            print("Please Insert Integer !")

def CheckGuess(guessedWord,char):
    for i in guessedWord:
        if (i == char):
            input('Please use another Letter ! Press ENTER to Continue ...')
            return False

    guessedWord.append(char)
    return True

def CheckWord(word,char):
    index = []
    for i in range(len(word)):
        if(word[i].lower() == char.lower()):
            index.append(i)

    return index

def CheckAnswer(word,answer):
    for i in range(len(word)):
        if word[i].lower() != answer[i].lower():
            return False
    return True

def PrintAnswer(answer):
    for i in answer:
        print(i,end=' ')
    print()

def rules_hangman():
    rulesh = '''
Hangman:
In this game of Hangman, you will try to guess a word within a category of your choice. 
You will be given 6 chances to guess the word before you die. 
If you are able to guess the word before your 6 chances are up, you will win the game.

Instructions:
1. To start the game, the system will ask the players what category of word they want to guess. 
   There are 6 categories to choose from which are Fruits, Flowers, Animals, Countries, Capital City and Vegetables. 
   Players are to input the number 1 until 6. If you put in an invalid number or any invalid input, 
   the system will ask for another input.
2. After receiving the input for category, the system will then generate a random word of the designated 
   category. Players are to try guessing each letter of the word correctly. 
   They will be given 6 chances and with every time the player guesses wrongly, 1 chance will be deducted accordingly. 
3. Players are to input their letter of choice to the system. The system will show whether 
   or not the letter is right by displaying an updated board. 
4. Players will win the game if they guessed the word correctly before the 6 chances are up.
5. Happy playing!'''
    return rulesh

def ChooseCategory():
    keys = [key for key in dict.keys()]
    
    print('{:^101s}'.format(f"press ENTER to continue or 'r' to read the rules"))
    sompt = input()
    space()

    while True:
        if sompt == 'r':
            print(rules_hangman())
            print('{:^114s}'.format(f"press ENTER to continue or 'r' to read the rules"))
        else: break
        sompt = input()
        space()

    print("Select Category : ")
    for i in range(len(keys)):
        print(str(i+1) + ". " + keys[i])
    while True:
        choice = IntInput("Your Choice : ")
        if choice == 'e!': 
            print('\n')
            print('{:^101s}'.format(f'---> Exit Game ! <---'))
            print('\n')
            return 'e!'

        choice = choice - 1
        if choice >=0 and choice<len(keys):
            return keys[choice]
        else :
            print("Out of Index")

def space():
    for _ in range(32): print()

def image(lives):
		if (lives == 6):
				print ("_________")
				print ("|	 |")
				print ("|")
				print ("|")
				print ("|")
				print ("|")
				print ("|________")
		elif (lives == 5):
				print ("_________")
				print ("|	 |")
				print ("|	 O")
				print ("|")
				print ("|")
				print ("|")
				print ("|________")
		elif (lives == 4):
				print ("_________")
				print ("|	 |")
				print ("|	 O")
				print ("|	 |")
				print ("|	 |")
				print ("|")
				print ("|________")
		elif (lives == 3):
				print ("_________")
				print ("|	 |")
				print ("|	 O")
				print ("|	\|")
				print ("|	 |")
				print ("|")
				print ("|________")
		elif (lives == 2):
				print ("_________")
				print ("|	 |")
				print ("|	 O")
				print ("|	\|/")
				print ("|	 |")
				print ("|")
				print ("|________")
		elif (lives == 1):
				print ("_________")
				print ("|	 |")
				print ("|	 O")
				print ("|	\|/")
				print ("|	 |")
				print ("|	/ ")
				print ("|________")
		elif (lives == 0):
				print ("_________")
				print ("|	 |")
				print ("|	 O")
				print ("|	\|/")
				print ("|	 |")
				print ("|	/ \ ")
				print ("|________")

# def looping(play_again,name):
#     play_again = input("Do You want to play again? y = yes, n = no \n")
#     while play_again.lower() not in ['y','n']:
#         play_again = input("Do You want to play again? y = yes, n = no \n")
#     if play_again == "y":
#         Hangman(name)
#     elif play_again == "n":
#         print(f'Thank you {name} for playing ! We expect to see you again!')
#         exit()

def Hangman(name):
    space()
    print('''
    ▒█░░▒█ █▀▀ ▒█░░░ ▒█▀▀█ █▀▀█ ▒█▀▄▀█ █▀▀ 　 ▀▀█▀▀ █▀▀█ 　 ▒█░▒█ █▀▀█ ▒█▄░▒█ ▒█▀▀█ ▒█▀▄▀█ █▀▀█ ▒█▄░▒█ 
    ▒█▒█▒█ █▀▀ ▒█░░░ ▒█░░░ █░░█ ▒█▒█▒█ █▀▀ 　 ░▒█░░ █░░█ 　 ▒█▀▀█ █▄▄█ ▒█▒█▒█ ▒█░▄▄ ▒█▒█▒█ █▄▄█ ▒█▒█▒█ 
    ▒█▄▀▄█ ▀▀▀ ▒█▄▄█ ▒█▄▄█ ▀▀▀▀ ▒█░░▒█ ▀▀▀ 　 ░▒█░░ ▀▀▀▀ 　 ▒█░▒█ ▀░░▀ ▒█░░▀█ ▒█▄▄█ ▒█░░▒█ ▀░░▀ ▒█░░▀█
    ''')
    print('{:^101s}'.format(f'-------------> Hello {name}, Best of Luck ! <-------------'))
    
    key = ChooseCategory()
    if key == 'e!': return 'e!'

    word = random.choice(dict[key])
    answer = []
    guessedWord = []
    lives = 6
    
    for i in range(len(word)):
        if word[i]==' ':
            answer.append(' ')
        else:
            answer.append('_')

    while not CheckAnswer(word,answer):
        space()
        image(lives)
        print("Category : " + key + " || " +  "Lives : " + str(lives))
        PrintAnswer(answer)
        char = GetCharInput("Insert Letter : ")
        if char == 'e!': return 'e!'

        if(CheckGuess(guessedWord,char)):
            index = CheckWord(word,char)
            if len(index)>0:
                for i in index:
                    if(i==0):
                        answer[i]= char.upper()
                    else :
                        answer[i] = char.lower()
            else :
                lives -= 1
                input("Wrong Guess ! Press ENTER to Continue ...")
                # image(lives)

                if lives<=0 :
                    print('\n\n')
                    print("You Lose !")
                    return
        # print("-------------------------------------")
    print('\n\n')
    print(f"The Word is '{word}', you win !")

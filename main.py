import random

while True:
    user_choice = input("Enter a choice(rock, paper, scissors): or quit")
    if user_choice == "quit".title:
        break
    choices = ['rock', 'paper', 'scissors']
    bot_choice = random.choice(choices)
    print(f'You chose {user_choice} and the bot chose {bot_choice}')
    
    if user_choice == bot_choice:
        print(f'You both selected {user_choice} you just tied to a bot, loser! :p')
    elif user_choice == 'rock'.title:
        if bot_choice == 'scissors'.title:
            print(f'Rock beats scissors! You Win! L bot lol')
        else:
            print('Paper beats rock! You lost! Unbelievable You lost to a bot, loser!')
    elif user_choice == 'scissors'.title:
        if bot_choice == 'paper'.title:
            print(f'scissors beats paper! You Win! L bot lol')
        else:
            print('paper looses to scissors! You lost! Hilarious You lost to a bot, loser!')
    elif user_choice == 'paper'.title:
        if bot_choice == 'rock'.title:
            print(f'paper beats Rock! You Win! L bot lol')
        else:
            print('paper beats rock! You lost! You lost to a bot, loser!')
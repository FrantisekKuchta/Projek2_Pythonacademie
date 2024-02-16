'''
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: František Kuchta
email: kuchta.f@seznam.cz
discord:FrantisekK #fanyny94

'''
import random
import time


def generated_number():
    '''
    The function will generate a number in the range from 1000 to 9999.
    No number that will be generated will contain duplicate digits (example = 5566)

    Ascent:
    The generated number is in the format str.
    
    '''
    duplicit = True
    while duplicit:
        number_list = []
        secret_number = str(random.randint(1000,9999))
    
        for number in secret_number:
            number_list.append(number)
            if len(set(number_list)) == len(secret_number):
                duplicit = False
                return secret_number
        else:
            continue
     


def get_bulls_cows(number, user_tip):
    '''
    Function:
       Evaluation of the entered number of the user and the guessed one. 
       The result is the number of Bulls - the number matches the location. 
       Number of Cows - the number is included in the fortune-telling number.
    Example:
       user ti = 1289
       sercret number = 1398
       bulls = 1
       cows = 2
    Ascent:
    bulls_cows = [1,2] in int.
    '''          
    bulls_cows = [0,0]
    for index in range(len(number)):
        if user_tip[index] == number[index]:
            bulls_cows[0] += 1        
        elif user_tip[index] in number:
            bulls_cows[1] += 1 
    return bulls_cows

def write_bull_bulls(value_bull):
    '''
    Function:
       Write Bulls = 0 or =< 2 
       Write Bull = 1 
    '''
    if value_bull == 1:
        bull = print(f'Bull: {value_bull}')
    else:
        bull = print(f'Bulls: {value_bull}')
    return bull

def write_cow_cows(value_cow):
    '''
    Function:
       Write Cows = 0 or =< 2 
       Write Cow = 1 
    '''
    if value_cow == 1:
        cow = print(f'Cow: {value_cow}')
    else:
        cow = print(f'Cows: {value_cow}')
    return cow

def game_replay():
    '''
    Function:
       You can restart the game or quit it.
    Example:
       Do you want to replay the game?:  Yes or No =>
       imput = Yes
       game_replay = True
       ----------------
       imput = No
       game_replay = False
    Ascent:
       game_reply = True or False
    '''
    game = input('Do you want to replay the game?:  Yes or No =>')
    if game.lower() == 'yes':
        return True
    else:
        return False
    

def game_bulls_and_cows():
    '''
    Bulls and Cows cell game launched. Where functions are used:
    get_bulls_cows,game_replay,generated_number,write_cow_cows,write_bull_bulls

    '''
    secret_number = generated_number()
    odelovac = '-' * 47
    game_go = True
    try_games = 0
    memory_attempt = []
    start_time = time.time() 
    
    print(f"""Hi there!\n{odelovac}
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.\n{odelovac}
Enter a number: \n{odelovac} """)
    while game_go:
        user_tip = input('>>> ')
        try_games += 1

    
        if user_tip[0] == str(0):
            print('Must not start 0 😞') 
            continue
        elif user_tip in memory_attempt:
            print('Repeating number  😲')
            continue         
        elif not user_tip.isnumeric():
            print('''It cannot contain letters or other characters.''')
            continue
        elif not  len(user_tip) == 4:
            print('''Incorrectly entered number of digits''')
            continue
        elif user_tip == secret_number:
            print('Victory !!!!! Congratulations 👍')
            print('Number of attempts: ', try_games)
            stop_time = time.time()
            time_game = stop_time - start_time
            print(f'Game time is {int(time_game)} s.')
            game_go = game_replay()
            if game_go == True:
                game_bulls_and_cows()
        else:   

            hodnoty = get_bulls_cows(secret_number,user_tip)
            write_bull_bulls(hodnoty[0])
            write_cow_cows(hodnoty[1])
            print(odelovac)
            memory_attempt.append(user_tip)
            continue

if __name__ == '__main__':
    game_bulls_and_cows()
        

    

    

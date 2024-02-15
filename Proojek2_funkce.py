import random
import time


def generated_number():
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
     


def get_bulls_cows(cislo, uzivatel_tip):          
    bulls_cows = [0,0]
    for index in range(len(cislo)):
        if uzivatel_tip[index] == cislo[index]:
            bulls_cows[0] += 1        
        elif uzivatel_tip[index] in cislo:
            bulls_cows[1] += 1 
    return bulls_cows

def write_bull_bulls(value_bull):
    if value_bull == 1:
        bull = print(f'Bull: {value_bull}')
    else:
        bull = print(f'Bulls: {value_bull}')
    return bull

def write_cow_cows(value_cow):
    if value_cow == 1:
        cow = print(f'Cow: {value_cow}')
    else:
        cow = print(f'Cows: {value_cow}')
    return cow


def game_bulls_and_cows():

    secret_number = generated_number()
    print(f' Secret number : {secret_number}')
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
            print('Victory !!!!! Congratulations =)')
            print('Number of attempts: ', try_games)
            game_go = False
            stop_time = time.time()
            time_game = stop_time - start_time
            print(f'Game time is {int(time_game)} s.')
        else:   

            hodnoty = get_bulls_cows(secret_number,user_tip)
            write_bull_bulls(hodnoty[0])
            write_cow_cows(hodnoty[1])
            print(odelovac)
            memory_attempt.append(user_tip)
            continue

if __name__ == '__main__':
    game_bulls_and_cows()
    

    

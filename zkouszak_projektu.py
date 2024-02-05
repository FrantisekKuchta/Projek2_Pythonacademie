import random
import timeit



####### Proměné ############
random.seed(150)
secret_number = str(random.randint(1000,9999))
print(secret_number)
odelovac = '-' * 47
game_go = True
try_games = 0
memory_attempt = []


####### definice vlastních funkcí
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
        bull = print(f'Bull: {bulls_cows[0]}')
    else:
        bull = print(f'Bulls: {bulls_cows[0]}')
    return bull

def write_cow_cows(value_cow):
    if value_cow == 1:
        cow = print(f'Cow: {bulls_cows[1]}')
    else:
        cow = print(f'Cows: {bulls_cows[1]}')
    return cow
    
              
        
################ Pozdrav############
print(f"""Hi there!\n{odelovac}
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.\n{odelovac}
Enter a number: \n{odelovac} """)

########### Hra #############
while game_go:
    user_tip = input('>>> ')
    try_games += 1
    
    if user_tip[0] == str(0):
       print('Must not start 0 =(')
       continue
    elif user_tip in memory_attempt:
        print('Repeating number  =O')
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
        print(timeit.timeit(stmt='game_go = False'))
    else:
        bulls_cows = get_bulls_cows(secret_number,user_tip)

        write_bull_bulls(bulls_cows[0])
        write_cow_cows(bulls_cows[1])
        print(odelovac)
        memory_attempt.append(user_tip)

import random
from unicodedata import numeric


# Try again after game is over
def trial():
    try_again=input('do you want to try again: [Y]/[N]')
    if try_again=='Y'.lower():
        guess()
    else:
        print('thank you for playing')


def guess():
    #Input name and difficulty
    p_name=input('what is your name : ')
    print(f'Welcome {p_name}\nPlease choose required difficulty')
    diff=input('[E]:Easy\n[N]:Normal\n[H]:Hard\n[Q]:quit\n')
    li=['E','N','H','Q'] 
    # if chosen difficulty not in list  
    while diff.upper() not in li:
        print('Please enter a valid choice')
        diff=input('Choose your difficulty\n[E]:Easy\n[N]:Normal\n[H]:Hard\n[Q]:quit\n')
    # Easy mode limit and number
    if diff=='E'.lower():
        rand=random.randint(1,10)
        limit=6
        print(f'you have {limit} attempts to guess number between 1 and 10')
    # Normal mode limit and number
    if diff=='N'.lower():
        rand=random.randint(1,20)
        limit=4
        print(f'you have {limit} attempts to guess number between 1 and 20')
    # Hard mode limit and number
    if diff=='H'.lower():
        rand=random.randint(1,50)
        limit=3
        print(f'you have {limit} attempts to guess number between 1 and 50')
    # Use Try so if user chose q it quits without Name error for limit
    try:
        while limit>0:
            limit-=1
            # Number is entered as a string so Value error will not be raised
            num=input('choose your number: ')
            if diff=='E'.lower():
                """
                Checking if the input is number so if user input a string it will not raise
                Value error instead will let him choose a number again
                """
                while num.isnumeric()==False or int(num)>10 or int(num)<1:
                    limit=limit
                    print('Please choose a valid number within given range')
                    num=input('choose your number: ')
            if diff=='N'.lower():
                while num.isnumeric()==False or int(num)>20 or int(num)<1:
                    limit=limit
                    print('Please choose a valid number within given range')
                    num=input('choose your number: ')
            if diff=='H'.lower():
                while num.isnumeric()==False or int(num)>50 or int(num)<1:
                    limit=limit
                    print('Please choose a valid number within given range')
                    num=input('choose your number: ')
            # User still have attempts but not the right number
            if int(num) !=rand and limit>0:
                print(f'You have {limit} attempts to try again') 
            # User won within attempts limit    
            if int(num)==rand and limit>0:
                if diff=='E'.lower():
                    print(f'Congratulations {p_name} you have won in {6-limit} attempts')
                    trial()
                    break   
                if diff=='N'.lower():
                    print(f'Congratulations {p_name} you have won in {4-limit} attempts')
                    trial()
                    break
                if diff=='H'.lower():
                    print(f'Congratulations {p_name} you have won in {3-limit} attempts')
                    trial()
                    break
            # Game over and try again  
            if limit==0:
                print('Game over')
                trial()               
    except NameError:
        if diff=='Q'.lower():
            print('Thank you for playing')               

guess()
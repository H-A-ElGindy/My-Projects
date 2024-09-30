import random
from unicodedata import numeric



def trial():
    try_again=input('do you want to try again: [Y]/[N]')
    if try_again=='Y'.lower():
        guess()
    else:
        print('thank you for playing')

def guess():
    p_name=input('what is your name : ')
    print(f'Welcome {p_name}\nPlease choose required difficulty')
    diff=input('[E]:Easy\n[N]:Normal\n[H]:Hard\n[Q]:quit\n')
    li=['E','N','H','Q']  
    while diff.upper() not in li:
        print('Please enter a valid choice')
        diff=input('Choose your difficulty\n[E]:Easy\n[N]:Normal\n[H]:Hard\n[Q]:quit\n')
    if diff=='E'.lower():
        rand=random.randint(1,10)
        limit=6
        print(f'you have {limit} attempts to guess number between 1 and 10')
    if diff=='N'.lower():
        rand=random.randint(1,20)
        limit=4
        print(f'you have {limit} attempts to guess number between 1 and 20')
    if diff=='H'.lower():
        rand=random.randint(1,50)
        limit=3
        print(f'you have {limit} attempts to guess number between 1 and 50')
    try:
        while limit>0:
            limit-=1
            num=input('choose your number: ')
            if diff=='E'.lower():
                while num.isnumeric()==False or int(num)>10 or int(num)<=0:
                    limit=limit
                    print('Please choose a valid number within given range')
                    num=input('choose your number: ')
            if diff=='N'.lower():
                while num.isnumeric()==False or int(num)>20 or int(num)<=0:
                    limit=limit
                    print('Please choose a valid number within given range')
                    num=input('choose your number: ')
            if diff=='H'.lower():
                while num.isnumeric()==False or int(num)>50 or int(num)<=0:
                    limit=limit
                    print('Please choose a valid number within given range')
                    num=input('choose your number: ')  
            if limit==0:
                print('Game over')
                trial()         
            if int(num) !=rand and limit>0:
                print(f'You have {limit} attempts to try again')     
            if int(num)==rand and limit>0:
                if diff=='E'.lower():
                    print(f'Congratulations {p_name} you have won in {6-limit} attempts')
                    break
                if diff=='N'.lower():
                    print(f'Congratulations {p_name} you have won in {4-limit} attempts')
                    break
                if diff=='H'.lower():
                    print(f'Congratulations {p_name} you have won in {3-limit} attempts')
                    break      
    except NameError:
        if diff=='Q'.lower():
            print('Thank you for playing')               

guess()
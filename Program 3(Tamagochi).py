# Game Tamagochi

print ('\n========================\n'
    '\"Welcome to tamagochi simulator!\"'
    '\n========================\n')
nama = input('Who is your pet name?\n')
pet = {'Name' : nama, 'Power' : 100}

def start():
    choice = input(
    '\n=====Choice=====\nWhat you want to do with ' + nama + '?\n'+
    '1. Give '  + nama + ' Eat\n'+
    '2. Look Power Status\n'+
    '3. Exit Simulator\n\n'
    )
    if choice == '1':
        goEat()
    elif choice == '2':
        goStatus()
    else:
        goExit()
def goEat():
    print ('\n===Your pet is eating===\n' + '\"nyam... nyam...\"' + 
            '\nYour Pet Power Added 100')
    pet['Power'] = pet['Power'] + 100
    start()
def goStatus():
    print ('\n=====Checking Status=====' + 
           '\nYour pet power is ' + str(pet['Power']))
    start()
def goExit():
    print ('\nLog Off, Good Bye\n=====END=====\n')
start()
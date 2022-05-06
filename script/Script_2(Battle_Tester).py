# Program Sederhana fanny vs ling

print ('\n================\nFanny vs Ling\nWho\'s' +
       ' gonna win?\n================\n')
Player1 = {'Name':'Fanny', 'Power':100}
Player2 = {'Name':'Ling', 'Power':200}
data1 = input('====Battle Begin====\nFanny' + 
        ' attacking ling.\nType \'next\' to see result.\n')
if data1 == 'next':
    print ('\n====Battle Result====\n' + 
        Player1['Name'] + ' lose against ' + Player2['Name'] + '.')
    print (Player1['Name'] + ' need to train more.\n')

def choice():
    text = input(
    '====Choice====\n' + 
    'What you want to do?\n'+
    '1. Train Fanny\n'+
    '2. Battle Again\n\n')
    if text == '1':
        goTrain()
    else:
        goBattle()
def goTrain():
    Player1['Power'] = Player1['Power'] + 100
    print ('\n====Training====\nFanny get more stronger.\n')
    choice()
def goBattle():
    if Player1['Power'] > Player2['Power']:
        print ('\n====Battle Result====\n' 
            + Player1['Name'], 'finnaly wins against',
            Player2['Name'] + '.\nCongratulations and GoodBye.\n' + 
            '====End====\n')
    else:
        print ('\n====Battle Again====\n' + Player1['Name'],
            'still lose against', Player2['Name'] + '.\n')
        choice()
choice()
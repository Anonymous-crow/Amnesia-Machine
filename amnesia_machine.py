import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import sys, math, pygame, random, time

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

PyrNO = 0

class Player:
    Name = "Null"
    ST = 0
    SP = 0
    MI = 0
    WI = 0

def setstat(NO):
    pass

print('welcome to the Amesia Machine')
stat_phase = True
while stat_phase:
    stattxt = ('Enter Player {} Stat:\n')
    p0 = Player()
    p0.Name = str(input('Enter Player Name:\n'))
    print("Player name is {}.  Is that correct?".format(p.Name))
    p0.ST = int(input(stattxt.format('Strength')))
    p0.SP = int(input(stattxt.format('Speed')))
    p0.MI = int(input(stattxt.format('Mind')))
    p0.WT = int(input(stattxt.format('Wit')))
    cont = input('add another player?')
    if cont == 'Yes':
        p1 = Player()
        p1.Name = str(input('Enter Player Name:\n'))
        print("Player name is {}.  Is that correct?".format(p.Name))
        p1.ST = int(input(stattxt.format('Strength')))
        p1.SP = int(input(stattxt.format('Speed')))
        p1.MI = int(input(stattxt.format('Mind')))
        p1.WT = int(input(stattxt.format('Wit')))
        cont = input('add another player?')
        if cont == 'Yes':
            p2 = Player()
            p2.Name = str(input('Enter Player Name:\n'))
            print("Player name is {}.  Is that correct?".format(p.Name))
            p2.ST = int(input(stattxt.format('Strength')))
            p2.SP = int(input(stattxt.format('Speed')))
            p2.MI = int(input(stattxt.format('Mind')))
            p2.WT = int(input(stattxt.format('Wit')))
            cont = input('add another player?')
            if cont == 'Yes':
                p3 = Player()
                p3.Name = str(input('Enter Player Name:\n'))
                print("Player name is {}.  Is that correct?".format(p.Name))
                p3.ST = int(input(stattxt.format('Strength')))
                p3.SP = int(input(stattxt.format('Speed')))
                p3.MI = int(input(stattxt.format('Mind')))
                p3.WT = int(input(stattxt.format('Wit')))
                print('you have reached max number of Players')


clear()
echo = 'Player {} {} stat is {}'
print (echo.format('1', 'Might', p.ST))
print (echo.format('1', 'Speed', P0.SP))
print (echo.format('1', 'Mind', p0.MI))
print (echo.format('1', 'Wit', p0.WT))

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import sys, math, pygame, random, time

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

player2 = 0
player3 = 0
player4 = 0

class Player:
    Name = "Null"
    ST = 0
    SP = 0
    MI = 0
    WI = 0

def setstat(NO):
    pass

print('welcome to the Amesia Machine')
stattxt = ('Enter Player {} Stat:\n')
p0 = Player()
p0.Name = str(input('Enter Player Name:\n'))
print("Player name is {}.  Is that correct?".format(p0.Name))
p0.ST = int(input(stattxt.format('Strength')))
p0.SP = int(input(stattxt.format('Speed')))
p0.MI = int(input(stattxt.format('Mind')))
p0.WT = int(input(stattxt.format('Wit')))
cont = input('add another player?')
if cont == 'Yes':
    player2 = 1
    p1 = Player()
    p1.Name = str(input('Enter Player Name:\n'))
    print("Player name is {}.  Is that correct?".format(p1.Name))
    p1.ST = int(input(stattxt.format('Strength')))
    p1.SP = int(input(stattxt.format('Speed')))
    p1.MI = int(input(stattxt.format('Mind')))
    p1.WT = int(input(stattxt.format('Wit')))
    cont = input('add another player?')
    if cont == 'Yes':
        player3 = 1
        p2 = Player()
        p2.Name = str(input('Enter Player Name:\n'))
        print("Player name is {}.  Is that correct?".format(p2.Name))
        p2.ST = int(input(stattxt.format('Strength')))
        p2.SP = int(input(stattxt.format('Speed')))
        p2.MI = int(input(stattxt.format('Mind')))
        p2.WT = int(input(stattxt.format('Wit')))
        cont = input('add another player?')
        if cont == 'Yes':
            player4 = 1
            p3 = Player()
            p3.Name = str(input('Enter Player Name:\n'))
            print("Player name is {}.  Is that correct?".format(p3.Name))
            p3.ST = int(input(stattxt.format('Strength')))
            p3.SP = int(input(stattxt.format('Speed')))
            p3.MI = int(input(stattxt.format('Mind')))
            p3.WT = int(input(stattxt.format('Wit')))
            print('you have reached max number of Players')


clear()

echo = 'Player {} {} stat is {}'
print (echo.format('1', 'Might', p0.ST))
print (echo.format('1', 'Speed', P0.SP))
print (echo.format('1', 'Mind', p0.MI))
print (echo.format('1', 'Wit', p0.WT))
if player2 == 1:
    print (echo.format('2', 'Might', p1.ST))
    print (echo.format('2', 'Speed', P1.SP))
    print (echo.format('2', 'Mind', p1.MI))
    print (echo.format('2', 'Wit', p1.WT))
if player3 == 1:
    print (echo.format('3', 'Might', p2.ST))
    print (echo.format('3', 'Speed', P2.SP))
    print (echo.format('3', 'Mind', p2.MI))
    print (echo.format('3', 'Wit', p2.WT))
if player4 == 1:
    print (echo.format('4', 'Might', p3.ST))
    print (echo.format('4', 'Speed', P3.SP))
    print (echo.format('4', 'Mind', p3.MI))
    print (echo.format('4', 'Wit', p3.WT))

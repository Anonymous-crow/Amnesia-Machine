import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import sys, math, pygame, random, time

def clear():
    os.system('cls' if os.name=='nt' else 'clear')
def pause():
    input("Press ENTER to continue...")

player2 = 0
player3 = 0
player4 = 0
playerNO = 1

class Player:
    Name = "Null"
    ST = 0
    SP = 0
    MI = 0
    WI = 0
    HP = 0
    MXHP = 0
    INJ = 0
    MXINJ = 0
    MP = 0
    MXMP = 0
    MOV = 0
    BLK = 0
    STANCE = 2
    AN = 10
    RN = 10
    INIT = 0
    PFS = 'ST' ##Preferred (F)ysical Stat
    DMG = 0

class NME:
    Name = "Gerblin"
    ST = 1
    SP = 2
    MI = 0
    WI = -1
    HP = 15
    MXHP = 15
    INJ = 2
    MXINJ = 2
    MP = 0
    MXMP = 0
    MOV = 30
    BLK = 0
    STANCE = 2
    AN = 10
    RN = 10
    INIT = 0
    PFS = 'ST'
    DMG = 0

def setstat(NO):
    pass

print('welcome to the Amesia Machine')
stattxt = ('Enter Player {} Stat:\n')
p0 = Player()
p0.Name = str(input('Enter Player Name:\n'))
print("Player name is {}.".format(p0.Name))
p0.ST = int(input(stattxt.format('Strength')))
p0.SP = int(input(stattxt.format('Speed')))
p0.MI = int(input(stattxt.format('Mind')))
p0.WT = int(input(stattxt.format('Wit')))
cont = input('add another player?\n')
if cont == 'Yes':
    player2 = 1
    playerNO = 2
    p1 = Player()
    p1.Name = str(input('Enter Player Name:\n'))
    print("Player name is {}.".format(p1.Name))
    p1.ST = int(input(stattxt.format('Strength')))
    p1.SP = int(input(stattxt.format('Speed')))
    p1.MI = int(input(stattxt.format('Mind')))
    p1.WT = int(input(stattxt.format('Wit')))
    cont = input('add another player?\n')
    if cont == 'Yes':
        player3 = 1
        playerNO = 3
        p2 = Player()
        p2.Name = str(input('Enter Player Name:\n'))
        print("Player name is {}.".format(p2.Name))
        p2.ST = int(input(stattxt.format('Strength')))
        p2.SP = int(input(stattxt.format('Speed')))
        p2.MI = int(input(stattxt.format('Mind')))
        p2.WT = int(input(stattxt.format('Wit')))
        cont = input('add another player?\n')
        if cont == 'Yes':
            player4 = 1
            playerNO = 4
            p3 = Player()
            p3.Name = str(input('Enter Player Name:\n'))
            print("Player name is {}.".format(p3.Name))
            p3.ST = int(input(stattxt.format('Strength')))
            p3.SP = int(input(stattxt.format('Speed')))
            p3.MI = int(input(stattxt.format('Mind')))
            p3.WT = int(input(stattxt.format('Wit')))
            print('you have reached max number of Players\n')


clear()
print('calculating stats...')
p0.MXHP = int(30 + (p0.ST + 4)*2)
if p0.MXHP < 24:
    p0.MXHP = 24
p0.HP = p0.MXHP
if p0.ST >= p0.SP:
    p0.MXINJ = 3 + p0.ST
elif p0.SP > p0.ST:
    p0.MXINJ = 3 + int(0.5*p0.SP)
if p0.MXINJ < 1:
    p0.MXINJ = 1
p0.INJ = p0.MXINJ
if p0.MI  >= p0.WT:
    p0.MXMP = int(2*(p0.MI + 1) + 2)
if p0.WT  > p0.MI:
    p0.MXMP = int(2*(p0.WT + 1) + 2)
p0.MP = p0.MXMP
p0.MOV = 5*(p0.SP + 4)
if p0.MOV < 10:
    p0.MOV = 10
if p0.ST >= p0.SP:
    p0.PFS = p0.ST
elif p0.SP > p0.ST:
    p0.PFS = p0.SP


if player2 == 1:
    p1.MXHP = 30 + (p1.ST + 4)*2
    if p1.MXHP < 24:
        p1.MXHP = 24
    p1.HP = p1.MXHP
    if p1.ST >= p1.SP:
        p1.MXINJ = 3 + p1.ST
    elif p1.SP > p1.ST:
        p1.MXINJ = 3 + int(0.5*p1.SP)
    if p1.MXINJ < 1:
        p1.MXINJ = 1
    p1.INJ = p1.MXINJ
    if p1.MI  >= p1.WT:
        p1.MXMP = int(2*(p1.MI + 1) + 2)
    if p1.WT  > p1.MI:
        p1.MXMP = int(2*(p1.WT + 1) + 2)
    p1.MP = p1.MXMP
    p1.MOV = 5*(p1.SP + 4)
    if p1.MOV < 10:
        p1.MOV = 10
    if p1.ST >= p1.SP:
        p1.PFS = p1.ST
    elif p1.SP > p1.ST:
        p1.PFS = p1.SP


if player3 == 1:
    p2.MXHP = 30 + (p2.ST + 4)*2
    if p2.MXHP < 24:
        p2.MXHP = 24
    p2.HP = p2.MXHP
    if p2.ST >= p2.SP:
        p2.MXINJ = 3 + p2.ST
    elif p2.SP > p2.ST:
        p2.MXINJ = 3 + int(0.5*p2.SP)
    if p2.MXINJ < 1:
        p2.MXINJ = 1
    p2.INJ = p2.MXINJ
    if p2.MI  >= p2.WT:
        p2.MXMP = int(2*(p2.MI + 1) + 2)
    if p2.WT  > p2.MI:
        p2.MXMP = int(2*(p2.WT + 1) + 2)
    p2.MP = p2.MXMP
    p2.MOV = 5*(p2.SP + 4)
    if p2.MOV < 10:
        p2.MOV = 10
    if p2.ST >= p2.SP:
        p2.PFS = p2.ST
    elif p2.SP > p2.ST:
        p2.PFS = p2.SP


if player4 == 1:
    p3.MXHP = 30 + (p3.ST + 4)*2
    if p3.MXHP < 24:
        p3.MXHP = 24
    p3.HP = p3.MXHP
    if p3.ST >= p3.SP:
        p3.MXINJ = 3 + p3.ST
    elif p3.SP > p3.ST:
        p3.MXINJ = 3 + int(0.5*p3.SP)
    if p3.MXINJ < 1:
        p3.MXINJ = 1
    p3.INJ = p3.MXINJ
    if p3.MI  >= p3.WT:
        p3.MXMP = int(2*(p3.MI + 1) + 2)
    if p3.WT  > p3.MI:
        p3.MXMP = int(2*(p3.WT + 1) + 2)
    p3.MP = p3.MXMP
    p3.MOV = 5*(p3.SP + 4)
    if p3.MOV < 10:
        p3.MOV = 10
    if p3.ST >= p3.SP:
        p3.PFS = p3.ST
    elif p3.SP > p3.ST:
        p3.PFS = p3.SP

clear()

echo = 'Player {} {} stat is {}'
print (echo.format('1', 'Might', p0.ST))
print (echo.format('1', 'Speed', p0.SP))
print (echo.format('1', 'Mind', p0.MI))
print (echo.format('1', 'Wit', p0.WT))
print (echo.format('1', 'HP', p0.MXHP))
print (echo.format('1', 'Injuries', p0.MXINJ))
print (echo.format('1', 'Mana', p0.MXMP))
print (echo.format('1', 'Movement', p0.MOV))
print('\n\n')
if player2 == 1:
    print (echo.format('2', 'Might', p1.ST))
    print (echo.format('2', 'Speed', p1.SP))
    print (echo.format('2', 'Mind', p1.MI))
    print (echo.format('2', 'Wit', p1.WT))
    print (echo.format('2', 'HP', p1.MXHP))
    print (echo.format('2', 'Injuries', p1.MXINJ))
    print (echo.format('2', 'Mana', p1.MXMP))
    print (echo.format('2', 'Movement', p1.MOV))
    print('\n\n')
if player3 == 1:
    print (echo.format('3', 'Might', p2.ST))
    print (echo.format('3', 'Speed', P2.SP))
    print (echo.format('3', 'Mind', p2.MI))
    print (echo.format('3', 'Wit', p2.WT))
    print (echo.format('3', 'HP', p2.MXHP))
    print (echo.format('3', 'Injuries', p2.MXINJ))
    print (echo.format('3', 'Mana', p2.MXMP))
    print (echo.format('3', 'Movement', p2.MOV))
    print('\n\n')
if player4 == 1:
    print (echo.format('4', 'Might', p3.ST))
    print (echo.format('4', 'Speed', P3.SP))
    print (echo.format('4', 'Mind', p3.MI))
    print (echo.format('4', 'Wit', p3.WT))
    print (echo.format('4', 'HP', p3.MXHP))
    print (echo.format('4', 'Injuries', p3.MXINJ))
    print (echo.format('4', 'Mana', p3.MXMP))
    print (echo.format('4', 'Movement', p3.MOV))
    print('\n\n')
pause()
clear()

GBLN = Enemy()
GBLN.HP = 20
GBLN.INIT = 7
print("A wild goblin attacks the party!\n\n")
if GBLN.INIT >= (p0.SP + p0.WT):
    print("The crafty goblin goes first!")
    TURN = NME
elif GBLN.INIT < (p0.SP + p0.WT):
    print("The party has the upper hand!")
    TURN = PTY
while GBLN.HP > 0 and p0.HP > 0:
    echo = 'Player {} {} stat is {}'
    print (echo.format('1', 'Might', p0.ST))
    print (echo.format('1', 'Speed', p0.SP))
    print (echo.format('1', 'Mind', p0.MI))
    print (echo.format('1', 'Wit', p0.WT))
    print (echo.format('1', 'HP', p0.MXHP))
    print (echo.format('1', 'Injuries', p0.MXINJ))
    print (echo.format('1', 'Mana', p0.MXMP))
    print (echo.format('1', 'Movement', p0.MOV))
    print('\n\n')
    pause()
    print('\n\n')
    if TURN == NME:
        clear()
        print('The goblin enters a stance...' '\n')
        GBLN.STANCE = random.randint(1, 3)
        if GBLN.STANCE == 1:
            GBLN.AN = 6
            GBLN.RN = 14
        if GBLN.STANCE == 2:
            GBLN.AN = 10
            GBLN.RN = 10
        if GBLN.STANCE == 3:
            GBLN.AN = 14
            GBLN.RN = 6
        print('The goblin attacks!' '\n')
        if (GBLN.AN + 3) > (p0.RN + p0.PFS):
            GBLN.DMG = int(8*(GBLN.AN + 3 - p0.RN + p0.PFS))
            p0.HP -= GBLN.DMG
            print('The goblin hits for ', str(GBLN.DMG), ' damage!' '\n\n')
        elif not (GBLN.AN + 3) > (p0.RN + p0.PFS):
            print('The goblin misses!' '\n\n')
        pause()
        clear()

from Options_arch.Lang import Lang_TAB
from Func import cls
import sys
import UI
import Start_Pick


SYM_0 = ' |'
ENDL = '\n'
SPACE = ' '

STAT = [0, 0, 0, 0, 0] #INT, STR, DEX, HP, MANA
STAT_TO_ADD = [1, 1, 1, 10, 5] #INT, STR, DEX, HP, MANA
STAT_ON_START = [0, 0, 0, 0, 0]

FLOOR_NUM = 1

MONEY_STAT = 150

CLASS_NAME = ""

#Exp
LEVEL_NOW = 1
EXP_NOW = 0
LEVEL_PERCENT = 0.0
EXP_TABLE = [ #level, elapsed exp
    [1, 30],
    [2, 40],
    [3, 50],
    [4, 75],
    [5, 100],
    [6, 125],
    [7, 150],
    [8, 200],
    [9, 250],
    [10, 300],
    [11, 400],
    [12, 600],
    [13, 750],
    [14, 900],
    [15, 1000]
]

def __STAT_SHOW__(EXP_NOW, LEVEL_NOW, LANG_INDEX):
    CLASS_NAME = Start_Pick.Return_Class_Name(LANG_INDEX)
    for x in range(0, 15):
        if EXP_NOW >= EXP_TABLE[x][1]:
            EXP_TO_ADD = EXP_NOW - EXP_TABLE[LEVEL_NOW - 1][1] 
            LEVEL_NOW = EXP_TABLE[LEVEL_NOW][0]
            EXP_NOW = 0
            EXP_NOW = EXP_NOW + EXP_TO_ADD

        LEVEL_PERCENT = (EXP_NOW * 100)/EXP_TABLE[LEVEL_NOW - 1][1]

    UI.__Ceil_UI__(UI.CEIL_LEN) 

    sys.stdout.write(ENDL)
    sys.stdout.write(f"{SPACE} INT = {STAT[0] + (STAT_TO_ADD[0] * LEVEL_NOW)}{SYM_0} STR = {STAT[1] + (STAT_TO_ADD[1] * LEVEL_NOW)}{SYM_0} DEX = {STAT[2] + (STAT_TO_ADD[2] * LEVEL_NOW)}{SYM_0} HP = {STAT[3] + (STAT_TO_ADD[3] * LEVEL_NOW)}{SYM_0} MANA = {STAT[4] + (STAT_TO_ADD[4] * LEVEL_NOW)}".center(UI.STAT_0 - 5, ' '))
    sys.stdout.write(f"{SPACE} Class = '{CLASS_NAME}'".center(UI.STAT_2, ' '))
    sys.stdout.write(f"{SPACE} {Lang_TAB[LANG_INDEX][15]} = {MONEY_STAT} EUR{SYM_0} Exp = {EXP_NOW}/{EXP_TABLE[LEVEL_NOW - 1][1]}{SYM_0} Level = {EXP_TABLE[LEVEL_NOW - 1][0]}{SYM_0} Level Perc = {round(LEVEL_PERCENT, 1)}%".center(UI.STAT_1 - 5, ' '))
    if FLOOR_NUM % 5 == 0: 
        sys.stdout.write(f"{SPACE} {Lang_TAB[LANG_INDEX][16]}: {FLOOR_NUM} - BOSS".center(UI.STAT_2, ' '))
    else:
        sys.stdout.write(f"{SPACE} {Lang_TAB[LANG_INDEX][16]}: {FLOOR_NUM}".center(UI.STAT_2, ' '))
    
    UI.__Floor_UI__(UI.FLOOR_LEN)
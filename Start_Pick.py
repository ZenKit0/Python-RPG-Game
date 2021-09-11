from Options_arch.Lang import Lang_TAB
import sys
import os
import Func
import Stats_UI

def CLASS_(LANG_INDEX, x):
    CLASS = [Lang_TAB[LANG_INDEX][47], Lang_TAB[LANG_INDEX][48], Lang_TAB[LANG_INDEX][49], Lang_TAB[LANG_INDEX][50]]
    return CLASS[x]

ATTACK = [0, 2, 4, 6]
CLASS_INDEX_TAB = [0, 1, 2, 3]
CLASS_INDEX = 0

ATTACK_NUMBER = 0

PICKED_CLASS = ""
CLASS_STATS = [
    [5, 1, 0, 30, 70],
    [0, 6, 2, 50, 30],
    [1, 3, 5, 25, 45],
    [0, 2, 1, 120, 25]
]

def START_PICK(LANG_INDEX):
    CLASS_PICK = 0

    sys.stdout.write(Lang_TAB[LANG_INDEX][45])
    for x in range(0, 4):
        print(CLASS_(LANG_INDEX, x))
    CLASS_PICK = int(input(Lang_TAB[LANG_INDEX][46]))
    
    IsValidNumber = False
    if CLASS_PICK >= 1 and CLASS_PICK <= 4:
        IsValidNumber = True
        for i in range(0, 5):
            Stats_UI.STAT[i] = Stats_UI.STAT[i] + CLASS_STATS[CLASS_PICK - 1][i]
            Stats_UI.STAT_ON_START[i] = Stats_UI.STAT_ON_START[i] + CLASS_STATS[CLASS_PICK - 1][i]
        Func.cls()
    else:
        while IsValidNumber == False:
            Func.cls()
            print(Lang_TAB[LANG_INDEX][4])
            sys.stdout.write(Lang_TAB[LANG_INDEX][45])
            for x in range(0, 4):
                print(CLASS_(LANG_INDEX, x))
            CLASS_PICK = int(input(Lang_TAB[LANG_INDEX][46]))
            if CLASS_PICK >= 1 and CLASS_PICK <= 4:
                IsValidNumber = True
                for i in range(0, 5):
                    Stats_UI.STAT[i] = Stats_UI.STAT[i] + CLASS_STATS[CLASS_PICK - 1][i]
                    Stats_UI.STAT_ON_START[i] = Stats_UI.STAT_ON_START[i] + CLASS_STATS[CLASS_PICK - 1][i]
                Func.cls()

def Return_Class_Name(LANG_INDEX):
    for x in range(0, 4):
        i = 1
        if Stats_UI.STAT_ON_START[i] == CLASS_STATS[x][i]:
            CLASS_NAME = CLASS_(LANG_INDEX, x)
            return CLASS_NAME[3:]

def Return_Class_Index():
    for x in range(0, 4):
        i = 1
        if Stats_UI.STAT_ON_START[i] == CLASS_STATS[x][i]:
            CLASS_INDEX = CLASS_INDEX_TAB[x]
            return CLASS_INDEX

def Return_Attack_Index():
    for x in range(0, 4):
        i = 1
        if Stats_UI.STAT_ON_START[i] == CLASS_STATS[x][i]:
            ATTACK_NUMBER = ATTACK[x]
            return ATTACK_NUMBER

def ConverNumToClassName(NUM, LANG_INDEX):
    if NUM == 0:
        return Lang_TAB[LANG_INDEX][47]
    elif NUM == 1:
        return Lang_TAB[LANG_INDEX][48]
    elif NUM == 2:
        return Lang_TAB[LANG_INDEX][49]
    elif NUM == 3:
        return Lang_TAB[LANG_INDEX][50]

def ConverClassNameToNum(STR, LANG_INDEX):
    if STR == Lang_TAB[LANG_INDEX][47]:
        return 0
    elif STR == Lang_TAB[LANG_INDEX][48]:
        return 1
    elif STR == Lang_TAB[LANG_INDEX][49]:
        return 2
    elif STR == Lang_TAB[LANG_INDEX][50]:
        return 3
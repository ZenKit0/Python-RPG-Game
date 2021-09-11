from Options_arch.Lang import Lang_TAB
import sys
import Func
import random
import Stats_UI

SYM_0_0 = '#'
UI_LENGTH = 40

Item_Cost = 0
STAT_NAME = ["INT", "STR", "DEX", "HP", "MANA"]

Currency = "EUR"

Items = [
    [
        ["Stick", 10, 1], 
        ["Cake", 15, 1], 
        ["Beer", 2, 1], 
        ["Bread", 7, 10],
        ["Cheese", 10, 15]
    ],
    [
        ["Weapon", 100, 7], 
        ["Firework", 25, 1], 
        ["Pho", 16, 1], 
        ["Ammunation", 20, 10],
        ["Void Bad", 25, 25]
    ],
    [
        ["Hat", 2, 1], 
        ["Shoes", 10, 1], 
        ["Sparkling Water", 1, 1], 
        ["Yoghurt", 3, 10],
        ["Selenium", 100, 60]
    ],
]

def Back_To_Main():
    Func.cls()

def TB_Shop_UI(LANG_INDEX): #top, bottom shop UI
    Func.endl()
    for x in range(1, UI_LENGTH + 1):
        sys.stdout.write(SYM_0_0)
        if x == UI_LENGTH / 2:
            sys.stdout.write(Lang_TAB[LANG_INDEX][38])
    Func.endl()

def Shop(LANG_INDEX):
    Buy(LANG_INDEX)

def Buy(LANG_INDEX):
    TB_Shop_UI(LANG_INDEX)
    Func.endl()
    RAND = random.randint(0, len(Items) - 1)
    for x in range(0, 5):
        print(f"{x + 1}. {Items[RAND][x][0]} - {Items[RAND][x][1]} {Currency} || +{Items[RAND][x][2]} {STAT_NAME[x]}")
    TB_Shop_UI(LANG_INDEX)
    CHOOSEN_OPTION = int(input(Lang_TAB[LANG_INDEX][39]))
    if CHOOSEN_OPTION == 1:
        CHOOSEN_ITEM = int(input(Lang_TAB[LANG_INDEX][40]))
        CHOOSEN_ITEM_NUM = [1, 2, 3, 4, 5]
        if CHOOSEN_ITEM in CHOOSEN_ITEM_NUM:
            if Stats_UI.MONEY_STAT > Items[RAND][CHOOSEN_ITEM - 1][1]:
                Stats_UI.MONEY_STAT = Stats_UI.MONEY_STAT - Items[RAND][CHOOSEN_ITEM - 1][1]
                Stats_UI.STAT[CHOOSEN_ITEM - 1] = Stats_UI.STAT[CHOOSEN_ITEM - 1] + Items[RAND][CHOOSEN_ITEM - 1][2]
            else:
                print(Lang_TAB[LANG_INDEX][41])
                input()
        else:
            print(Lang_TAB[LANG_INDEX][42])
            input()
    else:
        Back_To_Main()
from Options_arch.Lang import Lang_TAB
from Start_Pick import ConverNumToClassName, Return_Class_Index, Return_Class_Name
import Func
import Stats_UI
import os
 
DATA_LINES = 5

#### Data Explain

#Stats
#Class
#Money, EXP, Level
#Floor
#Stats on start

#### Data Explain

def Read_Start(LANG_INDEX):
    FileExist = False
    Func.cls()
    while FileExist == False:
        print(Lang_TAB[LANG_INDEX][7])
        for x in range(1, 5):
            print(f"{x}. Save_{x}")
        SAVE_CHOOSE = int(input(Lang_TAB[LANG_INDEX][8]))
        if SAVE_CHOOSE >= 1 and SAVE_CHOOSE <= 4:
            if os.path.exists(f"./SaveData/Save_{SAVE_CHOOSE}.txt"):
                Read(SAVE_CHOOSE, LANG_INDEX)
                FileExist = True
            else:
                print(Lang_TAB[LANG_INDEX][9])
                input(Lang_TAB[LANG_INDEX][10])
                Func.cls()
        else:
            print(Lang_TAB[LANG_INDEX][11])
            Func.cls()

def Read(FileIndex, LANG_INDEX):
    SaveDataTab = []
    file = open("SaveData/Save_" + f"{FileIndex}.txt", "r")
    for i in range(0, DATA_LINES):
        Data = file.readline()
        SaveDataTab.append(Data.split(' '))
    for NUM in range(0, len(Stats_UI.STAT)):
        Stats_UI.STAT[NUM] = int(SaveDataTab[0][NUM]) - (Stats_UI.STAT_TO_ADD[NUM] * Stats_UI.LEVEL_NOW)
    for NUM in range(0, len(Stats_UI.STAT_ON_START)):
        Stats_UI.STAT_ON_START[NUM] = int(SaveDataTab[4][NUM])
    Stats_UI.CLASS_NAME = ConverNumToClassName(int(SaveDataTab[1][0]), LANG_INDEX)
    Stats_UI.MONEY_STAT = int(SaveDataTab[2][0])
    Stats_UI.EXP_NOW = int(SaveDataTab[2][1])
    Stats_UI.LEVEL_NOW = int(SaveDataTab[2][2])
    Stats_UI.FLOOR_NUM = int(SaveDataTab[3][0])
    Func.cls()

def Save_Start(LANG_INDEX):
    Func.cls()
    print(Lang_TAB[LANG_INDEX][12])
    for x in range(1, 5):
        print(f"{x}. Save_{x}")
    SAVE_CHOOSE = int(input(Lang_TAB[LANG_INDEX][8]))
    if SAVE_CHOOSE >= 1 and SAVE_CHOOSE <= 4:
        Save(SAVE_CHOOSE)
    else:
        print(Lang_TAB[LANG_INDEX][11])
        input()

def Save(FileIndex):
    FIRST_DATA = []
    SEC_DATA = [f"\n{Return_Class_Index()}\n"]
    THIRD_DATA = [f"{Stats_UI.MONEY_STAT} ", f"{Stats_UI.EXP_NOW} ", f"{Stats_UI.LEVEL_NOW}\n"]
    FOURTH_DATA = [f"{Stats_UI.FLOOR_NUM}\n"]
    FIFTH_DATA = []
    DATA = [FIRST_DATA, SEC_DATA, THIRD_DATA, FOURTH_DATA, FIFTH_DATA, "\n---"]
    for NUM in range(0, len(Stats_UI.STAT)):
        FIRST_DATA.append(f"{Stats_UI.STAT[NUM] + (Stats_UI.STAT_TO_ADD[NUM] * Stats_UI.LEVEL_NOW)} ")
    for NUM in range(0, len(Stats_UI.STAT_ON_START)):
        FIFTH_DATA.append(f"{Stats_UI.STAT_ON_START[NUM]} ")
    file = open(f"SaveData/Save_{FileIndex}.txt", "w")
    for x in DATA:
        file.writelines(x)
    file.close()

def OptionPick(LANG_INDEX):
    print(Lang_TAB[LANG_INDEX][0])
    print(Lang_TAB[LANG_INDEX][1])
    print(Lang_TAB[LANG_INDEX][2])
    CHOOSE = int(input(Lang_TAB[LANG_INDEX][3]))
    if CHOOSE == 1:
        Read_Start(LANG_INDEX)
    elif CHOOSE == 2:
        Func.cls()
    else:
        print(Lang_TAB[LANG_INDEX][4])
    return CHOOSE

def Main_Option_Pick(LANG_INDEX):
    print(Lang_TAB[LANG_INDEX][0])
    print(Lang_TAB[LANG_INDEX][5])
    print(Lang_TAB[LANG_INDEX][6])
    OPTION_CHOOSE = int(input(Lang_TAB[LANG_INDEX][3]))
    if OPTION_CHOOSE == 1:
        Save_Start(LANG_INDEX)
    elif OPTION_CHOOSE == 2:
        Read_Start(LANG_INDEX)
    else:
        print(Lang_TAB[LANG_INDEX][4])

def Encrypt_Save(Text):
    print()

def Decrypt_Save(Text):
    print()
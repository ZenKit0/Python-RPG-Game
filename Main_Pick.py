from Options_arch.Lang import Lang_TAB
import sys
from time import sleep
import Operations.Fight
import Operations.Shop
import Func
import SaveData
import Options

def __Main_Pick__(LANG_INDEX):
    OPERATIONS = [Lang_TAB[LANG_INDEX][17], Lang_TAB[LANG_INDEX][18], Lang_TAB[LANG_INDEX][19], Lang_TAB[LANG_INDEX][20], Lang_TAB[LANG_INDEX][21]] #"4. Quests\n"
    sys.stdout.write(f"\n{Lang_TAB[LANG_INDEX][0]}\n")
    for x in OPERATIONS:
        sys.stdout.write(x)
    CHOOSE = int(input(f"\n{Lang_TAB[LANG_INDEX][3]}"))
    if CHOOSE == 1:
        Operations.Fight.Start_Fight(LANG_INDEX)
    elif CHOOSE == 2:
        Operations.Shop.Shop(LANG_INDEX)
    elif CHOOSE == 3:
        SaveData.Main_Option_Pick(LANG_INDEX)
    elif CHOOSE == 4:
        Options.Option_Open(LANG_INDEX)
    elif CHOOSE == 5:
        Close_Time = 3
        print(Lang_TAB[LANG_INDEX][22] % Close_Time)
        for i in reversed(range(1, Close_Time + 1)):
            print(f"{i}..")
            sleep(1)
        quit()
    else:
        Func.cls()
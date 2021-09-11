from Options_arch.Lang import Language_start
import UI
import Stats_UI
import Start_Pick
import Func
from time import sleep
import Main_Pick
import SaveData

Picked_Lang = Language_start()
CHOOSE = SaveData.OptionPick(Picked_Lang)
if CHOOSE == 1:
    while True:
        Stats_UI.__STAT_SHOW__(Stats_UI.EXP_NOW, Stats_UI.LEVEL_NOW, Picked_Lang)
        Main_Pick.__Main_Pick__(Picked_Lang)
        Func.cls()
elif CHOOSE == 2:
    Start_Pick.START_PICK(Picked_Lang)
    Stats_UI.CLASS_NAME = Start_Pick.Return_Class_Name(Picked_Lang)
    while True:
        Stats_UI.__STAT_SHOW__(Stats_UI.EXP_NOW, Stats_UI.LEVEL_NOW, Picked_Lang)
        Main_Pick.__Main_Pick__(Picked_Lang)
        Func.cls()

input()
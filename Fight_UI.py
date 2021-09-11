import sys
import UI
import Func

SYM_0 = ' |'
SPACE = ' '

def __Fight_UI__(CurrentHP, CurrentYourHP, CurrentMANA, NAME, LEVEL, INT, STR, DEX, MIN_MONEY, MAX_MONEY, MIN_EXP, MAX_EXP):
    Func.cls()
    UI.__Ceil_UI__(UI.CEIL_LEN)
    Func.endl()
    sys.stdout.write(f"Mob name = '{NAME}'".center(UI.STAT_0))
    Func.endl()
    sys.stdout.write(f"Level = {LEVEL}{SYM_0} INT = {INT}{SYM_0} STR = {STR}{SYM_0} DEX = {DEX}{SYM_0} HP = {CurrentHP}".center(UI.STAT_0))
    Func.endl()
    sys.stdout.write(f"Min Money = {MIN_MONEY}{SYM_0} Max Money = {MAX_MONEY}{SYM_0} Min EXP = {MIN_EXP}{SYM_0} Max EXP = {MAX_EXP}".center(UI.STAT_0))
    UI.__Center_UI__(UI.UI_LEN)
    sys.stdout.write(f"Your HP = {CurrentYourHP}{SYM_0} Your Mana = {CurrentMANA}".center(UI.STAT_0))
    UI.__Floor_UI__(UI.FLOOR_LEN)

def __BOSS_Fight_UI__(CurrentHP, CurrentYourHP, CurrentMANA, NAME, LEVEL, INT, STR, DEX, MIN_MONEY, MAX_MONEY, MIN_EXP, MAX_EXP):
    Func.cls()
    UI.__Ceil_UI_BOSS__(UI.CEIL_LEN)
    Func.endl()
    sys.stdout.write(f"Boss name = '{NAME}'".center(UI.STAT_0))
    Func.endl()
    sys.stdout.write(f"Level = {LEVEL}{SYM_0} INT = {INT}{SYM_0} STR = {STR}{SYM_0} DEX = {DEX}{SYM_0} HP = {CurrentHP}".center(UI.STAT_0))
    Func.endl()
    sys.stdout.write(f"Min Money = {MIN_MONEY}{SYM_0} Max Money = {MAX_MONEY}{SYM_0} Min EXP = {MIN_EXP}{SYM_0} Max EXP = {MAX_EXP}".center(UI.STAT_0))
    UI.__Center_UI_BOSS__(UI.UI_LEN)
    sys.stdout.write(f"Your HP = {CurrentYourHP}{SYM_0} Your Mana = {CurrentMANA}".center(UI.STAT_0))
    Func.endl()
    UI.__Floor_UI_BOSS__(UI.FLOOR_LEN)
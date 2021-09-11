from Options_arch.Lang import Lang_TAB
import random
import sys
import Data.Mob_Data
import Data.Character_Data
import Data.Boss_Data
import Start_Pick
import Func
import Fight_UI
import Stats_UI
import UI

STATS = ["Level", "INT", "STR", "DEX", "VIT", "HP"]

IS_MOB_DEFEATED = False
ATTACK_NAME = ""

ATTACK_NAMES = []
ATTACK_POWER = []
ATTACK_MANA = []

for x in range(0, 4):
    ATTACK_NAMES.append(Data.Character_Data.char_data_tab[x][1])
    ATTACK_NAMES.append(Data.Character_Data.char_data_tab[x][3])
        
    ATTACK_POWER.append(Data.Character_Data.char_data_tab[x][2])
    ATTACK_POWER.append(Data.Character_Data.char_data_tab[x][4])

    ATTACK_MANA.append(Data.Character_Data.char_data_tab[x][5])
    ATTACK_MANA.append(Data.Character_Data.char_data_tab[x][6])

def Random_Number_MOB(MOB_LEVEL):
    RAND = random.randint(1, 3)#Sort_Mob_to_Player(MOB_LEVEL, Stats_UI.LEVEL_NOW))
    return RAND

def Random_Number_BOSS():
    RAND = random.randint(1, Data.Boss_Data.Line_Count - 1)
    return RAND

def Back_To_Main():
    Func.cls()

def Gain_exp(MIN_VALUE, MAX_VALUE):
    EXP = random.randint(int(MIN_VALUE), int(MAX_VALUE))
    return EXP

def Gain_Money(MIN_VALUE, MAX_VALUE):
    MONEY = random.randint(int(MIN_VALUE), int(MAX_VALUE))
    return MONEY

#Sort mob to player level
#In work
def Sort_Mob_to_Player(MOB_LVL, PLAYER_LVL):
    MOB_INDEX = 0
    for i in range(0, Data.Mob_Data.Line_Count - 2):
        if MOB_LVL <= PLAYER_LVL + 2 or MOB_LVL >= PLAYER_LVL - 2:
            MOB_INDEX = i
    return MOB_INDEX

#/In work

def RAND_HIT(MIN_VALUE, CLASS):
    #data_mage = int(Data.Character_Data.char_data_tab[0][2])
    RAND_HIT_VAL = random.randint(int(MIN_VALUE), int(CLASS))
    return RAND_HIT_VAL

def MOB_HIT(MIN_VALUE, MAX_VALUE):
    RAND_HIT_VAL = random.randint(int(MIN_VALUE), int(MAX_VALUE))
    return RAND_HIT_VAL

def Mob_took_Money(MIN_VALUE, MAX_VALUE, MOB_NAME, LANG_INDEX):
    RAND_TOOK = random.randint(int(MIN_VALUE), int(MAX_VALUE))
    Stats_UI.MONEY_STAT = Stats_UI.MONEY_STAT - RAND_TOOK
    print(Lang_TAB[LANG_INDEX][37] % (MOB_NAME, RAND_TOOK))
    return RAND_TOOK

def Check_MANA_HP_T_MONEY(CURRENT_MANA, CURRENT_HP, MIN_MOB_MON, MAX_MOB_MON, MOB_NAME, LANG_INDEX):
    if CURRENT_MANA <= 0 and CURRENT_HP >= 0:
        print(Lang_TAB[LANG_INDEX][27])
        Mob_took_Money(MIN_MOB_MON, MAX_MOB_MON, MOB_NAME, LANG_INDEX)
        input(Lang_TAB[LANG_INDEX][10])
    elif CURRENT_MANA >= 0 and CURRENT_HP <= 0:
        print(Lang_TAB[LANG_INDEX][35])
        Mob_took_Money(MIN_MOB_MON, MAX_MOB_MON, MOB_NAME, LANG_INDEX)
        input(Lang_TAB[LANG_INDEX][10])
    elif CURRENT_MANA <= 0 and CURRENT_HP <= 0:
        print(Lang_TAB[LANG_INDEX][36])
        Mob_took_Money(MIN_MOB_MON, MAX_MOB_MON, MOB_NAME, LANG_INDEX)
        input(Lang_TAB[LANG_INDEX][10])

def Boss_Fight(RAND, CURRENT_HP, CURRENT_MANA, LANG_INDEX):  
    BOSS_HP_NOW = int(Data.Boss_Data.boss_data_tab[RAND - 1][5])
    BOSS_NAME = Data.Boss_Data.boss_data_tab[RAND - 1][0]
    BOSS_STATS = []
    for y in range(1, 6):
        BOSS_STATS.append(int(Data.Boss_Data.boss_data_tab[RAND - 1][y]))
    print(BOSS_STATS)
    BOSS_ATTACK_NAME = Data.Boss_Data.boss_data_tab[RAND - 1][6]
    MIN_BOSS_MONEY = int(Data.Boss_Data.boss_data_tab[RAND - 1][8])
    MAX_BOSS_MONEY = int(Data.Boss_Data.boss_data_tab[RAND - 1][9])
    MIN_BOSS_EXP = int(Data.Boss_Data.boss_data_tab[RAND - 1][10])
    MAX_BOSS_EXP = int(Data.Boss_Data.boss_data_tab[RAND - 1][11])
    MIN_BOSS_MON_T = int(Data.Boss_Data.boss_data_tab[RAND - 1][12])
    MAX_BOSS_MON_T = int(Data.Boss_Data.boss_data_tab[RAND - 1][13])

    while BOSS_HP_NOW > 0 and CURRENT_MANA > 0 and CURRENT_HP > 0:
        Fight_UI.__BOSS_Fight_UI__(BOSS_HP_NOW, CURRENT_HP, CURRENT_MANA, BOSS_NAME, BOSS_STATS[0], BOSS_STATS[1], BOSS_STATS[2], BOSS_STATS[3], MIN_BOSS_MONEY, MAX_BOSS_MONEY, MIN_BOSS_EXP, MAX_BOSS_EXP)
        CLASS_PICK_VAL = Start_Pick.Return_Attack_Index()
        EXP_TABLE_UI = Stats_UI.EXP_TABLE
        LEVEL_NOW_UI = Stats_UI.LEVEL_NOW
        if CLASS_PICK_VAL == 0:
            Attack_1 = RAND_HIT(int(ATTACK_POWER[CLASS_PICK_VAL]), int(ATTACK_POWER[CLASS_PICK_VAL]) * EXP_TABLE_UI[LEVEL_NOW_UI - 1][0] * (Stats_UI.STAT[0] * Stats_UI.LEVEL_NOW // 2) ) // 4
            Attack_2 = RAND_HIT(int(ATTACK_POWER[CLASS_PICK_VAL + 1]), int(ATTACK_POWER[CLASS_PICK_VAL + 1]) * EXP_TABLE_UI[LEVEL_NOW_UI - 1][0] * (Stats_UI.STAT[0] * Stats_UI.LEVEL_NOW // 2)) // 4
            if Attack_1 > Attack_2:
                while Attack_1 > Attack_2:
                    Attack_1 = RAND_HIT(int(ATTACK_POWER[CLASS_PICK_VAL]), int(ATTACK_POWER[CLASS_PICK_VAL]) * EXP_TABLE_UI[LEVEL_NOW_UI - 1][0] * (Stats_UI.STAT[0] * Stats_UI.LEVEL_NOW // 2) ) // 4
                    Attack_2 = RAND_HIT(int(ATTACK_POWER[CLASS_PICK_VAL + 1]), int(ATTACK_POWER[CLASS_PICK_VAL + 1]) * EXP_TABLE_UI[LEVEL_NOW_UI - 1][0] * (Stats_UI.STAT[0] * Stats_UI.LEVEL_NOW // 2)) // 4
        elif CLASS_PICK_VAL == 2:
            Attack_1 = RAND_HIT(int(ATTACK_POWER[CLASS_PICK_VAL]), int(ATTACK_POWER[CLASS_PICK_VAL]) * EXP_TABLE_UI[LEVEL_NOW_UI - 1][0] * Stats_UI.STAT[2] * Stats_UI.LEVEL_NOW) // 4
            Attack_2 = RAND_HIT(int(ATTACK_POWER[CLASS_PICK_VAL + 1]), int(ATTACK_POWER[CLASS_PICK_VAL + 1]) * EXP_TABLE_UI[LEVEL_NOW_UI - 1][0] * Stats_UI.STAT[2] * Stats_UI.LEVEL_NOW) // 4
        else:
            Attack_1 = RAND_HIT(int(ATTACK_POWER[CLASS_PICK_VAL]), int(ATTACK_POWER[CLASS_PICK_VAL]) * EXP_TABLE_UI[LEVEL_NOW_UI - 1][0] * Stats_UI.STAT[1] * Stats_UI.LEVEL_NOW) // 4
            Attack_2 = RAND_HIT(int(ATTACK_POWER[CLASS_PICK_VAL + 1]), int(ATTACK_POWER[CLASS_PICK_VAL + 1]) * EXP_TABLE_UI[LEVEL_NOW_UI - 1][0] * Stats_UI.STAT[1] * Stats_UI.LEVEL_NOW) // 4
        Mana_1 = RAND_HIT(int(ATTACK_MANA[CLASS_PICK_VAL]), int(ATTACK_MANA[CLASS_PICK_VAL]) * EXP_TABLE_UI[LEVEL_NOW_UI - 1][0])
        Mana_2 = RAND_HIT(int(ATTACK_MANA[CLASS_PICK_VAL + 1]), int(ATTACK_MANA[CLASS_PICK_VAL + 1]) * EXP_TABLE_UI[LEVEL_NOW_UI - 1][0])
        BOSS_ATTACK = MOB_HIT(1, Data.Boss_Data.boss_data_tab[RAND - 1][7])
        if CURRENT_MANA > 0 and CURRENT_HP > 0:
            print(Lang_TAB[LANG_INDEX][33])
            print(f"1. {Lang_TAB[LANG_INDEX][34]}" % (ATTACK_NAMES[CLASS_PICK_VAL], Attack_1, Mana_1))
            print(f"2. {Lang_TAB[LANG_INDEX][34]}" % (ATTACK_NAMES[CLASS_PICK_VAL + 1], Attack_2, Mana_2))
            ATTACK_CHOOSE = int(input(Lang_TAB[LANG_INDEX][26]))
            if ATTACK_CHOOSE == 1:
                if CURRENT_MANA < Mana_1:
                    print(Lang_TAB[LANG_INDEX][27])
                else:
                    UI.__Fight_Center_UI__(UI.UI_LEN)
                    print(Lang_TAB[LANG_INDEX][28] % (BOSS_NAME, Attack_1))
                    UI.__Fight_Center_UI__(UI.UI_LEN)
                    CURRENT_MANA = CURRENT_MANA - Mana_1
                    BOSS_HP_NOW = BOSS_HP_NOW - Attack_1
            elif ATTACK_CHOOSE == 2:
                if CURRENT_MANA < Mana_2:
                    Func.endl()
                    print(Lang_TAB[LANG_INDEX][27])
                    Func.endl()
                else:
                    UI.__Fight_Center_UI__(UI.UI_LEN)
                    print(Lang_TAB[LANG_INDEX][28] % (BOSS_NAME, Attack_2))
                    UI.__Fight_Center_UI__(UI.UI_LEN)
                    CURRENT_MANA = CURRENT_MANA - Mana_2
                    BOSS_HP_NOW = BOSS_HP_NOW - Attack_2
            else:
                print(Lang_TAB[LANG_INDEX][29])
            
            if BOSS_HP_NOW > 0:
                print(Lang_TAB[LANG_INDEX][30] % (BOSS_NAME, BOSS_ATTACK_NAME, BOSS_ATTACK))
                UI.__Fight_Center_UI__(UI.UI_LEN)
                Func.endl()
                CURRENT_HP = CURRENT_HP - BOSS_ATTACK
                input(Lang_TAB[LANG_INDEX][10])
                Func.endl()
                Check_MANA_HP_T_MONEY(CURRENT_MANA, CURRENT_HP, MIN_BOSS_MON_T, MAX_BOSS_MON_T, BOSS_NAME, LANG_INDEX)

        if BOSS_HP_NOW <= 0:
            Func.endl()
            MONEY = Gain_Money(MIN_BOSS_MONEY, MAX_BOSS_MONEY)
            EXP = Gain_exp(MIN_BOSS_EXP, MAX_BOSS_EXP)
            print(f"You killed {BOSS_NAME}")
            print(f"Gained: {MONEY} EUR and {EXP} EXP")
            Stats_UI.FLOOR_NUM = Stats_UI.FLOOR_NUM + 1
            Stats_UI.MONEY_STAT = Stats_UI.MONEY_STAT + MONEY
            Stats_UI.EXP_NOW = Stats_UI.EXP_NOW + EXP
            input(Lang_TAB[LANG_INDEX][10])
        Func.cls()
        Func.endl()

def Fight(RAND, CURRENT_HP, CURRENT_MANA, LANG_INDEX):
    MOB_HP_NOW = int(Data.Mob_Data.mob_data_tab[RAND - 1][5])
    MOB_NAME = Data.Mob_Data.mob_data_tab[RAND - 1][0]

    MOB_ATTACK_NAME = Data.Mob_Data.mob_data_tab[RAND - 1][6]
    MIN_MOB_MONEY = int(Data.Mob_Data.mob_data_tab[RAND - 1][8])
    MAX_MOB_MONEY = int(Data.Mob_Data.mob_data_tab[RAND - 1][9])
    MIN_MOB_EXP = int(Data.Mob_Data.mob_data_tab[RAND - 1][10])
    MAX_MOB_EXP = int(Data.Mob_Data.mob_data_tab[RAND - 1][11])
    MIN_MOB_MON_T = int(Data.Mob_Data.mob_data_tab[RAND - 1][12])
    MAX_MOB_MON_T = int(Data.Mob_Data.mob_data_tab[RAND - 1][13])

    MOB_STATS = []
    for y in range(1, 6):
        MOB_STATS.append(int(Data.Mob_Data.mob_data_tab[RAND - 1][y]))
    
    Fight_UI.__Fight_UI__(MOB_HP_NOW, CURRENT_HP, CURRENT_MANA, MOB_NAME, MOB_STATS[0], MOB_STATS[1], MOB_STATS[2], MOB_STATS[3], MIN_MOB_MONEY, MAX_MOB_MONEY, MIN_MOB_EXP, MAX_MOB_EXP)
    Func.endl()
    sys.stdout.write(Lang_TAB[LANG_INDEX][23] % MOB_NAME)
    Func.endl()
    print(Lang_TAB[LANG_INDEX][24])
    print(Lang_TAB[LANG_INDEX][25])
    OPTION = int(input(Lang_TAB[LANG_INDEX][3]))
    if OPTION == 1:
        while MOB_HP_NOW > 0 and CURRENT_MANA > 0 and CURRENT_HP > 0:
            Fight_UI.__Fight_UI__(MOB_HP_NOW, CURRENT_HP, CURRENT_MANA, MOB_NAME, MOB_STATS[0], MOB_STATS[1], MOB_STATS[2], MOB_STATS[3], MIN_MOB_MONEY, MAX_MOB_MONEY, MIN_MOB_EXP, MAX_MOB_EXP)
            CLASS_PICK_VAL = Start_Pick.Return_Attack_Index()
            EXP_TABLE_UI = Stats_UI.EXP_TABLE
            LEVEL_NOW_UI = Stats_UI.LEVEL_NOW
            if CLASS_PICK_VAL == 0:
                Attack_1 = RAND_HIT(int(ATTACK_POWER[CLASS_PICK_VAL]), int(ATTACK_POWER[CLASS_PICK_VAL]) * EXP_TABLE_UI[LEVEL_NOW_UI - 1][0] * (Stats_UI.STAT[0] * Stats_UI.LEVEL_NOW // 2) ) // 4
                Attack_2 = RAND_HIT(int(ATTACK_POWER[CLASS_PICK_VAL + 1]), int(ATTACK_POWER[CLASS_PICK_VAL + 1]) * EXP_TABLE_UI[LEVEL_NOW_UI - 1][0] * (Stats_UI.STAT[0] * Stats_UI.LEVEL_NOW // 2)) // 4
                if Attack_1 > Attack_2:
                    while Attack_1 > Attack_2:
                        Attack_1 = RAND_HIT(int(ATTACK_POWER[CLASS_PICK_VAL]), int(ATTACK_POWER[CLASS_PICK_VAL]) * EXP_TABLE_UI[LEVEL_NOW_UI - 1][0] * (Stats_UI.STAT[0] * Stats_UI.LEVEL_NOW // 2) ) // 4
                        Attack_2 = RAND_HIT(int(ATTACK_POWER[CLASS_PICK_VAL + 1]), int(ATTACK_POWER[CLASS_PICK_VAL + 1]) * EXP_TABLE_UI[LEVEL_NOW_UI - 1][0] * (Stats_UI.STAT[0] * Stats_UI.LEVEL_NOW // 2)) // 4
            elif CLASS_PICK_VAL == 2:
                Attack_1 = RAND_HIT(int(ATTACK_POWER[CLASS_PICK_VAL]), int(ATTACK_POWER[CLASS_PICK_VAL]) * EXP_TABLE_UI[LEVEL_NOW_UI - 1][0] * Stats_UI.STAT[2] * Stats_UI.LEVEL_NOW) // 4
                Attack_2 = RAND_HIT(int(ATTACK_POWER[CLASS_PICK_VAL + 1]), int(ATTACK_POWER[CLASS_PICK_VAL + 1]) * EXP_TABLE_UI[LEVEL_NOW_UI - 1][0] * Stats_UI.STAT[2] * Stats_UI.LEVEL_NOW) // 4
            else:
                Attack_1 = RAND_HIT(int(ATTACK_POWER[CLASS_PICK_VAL]), int(ATTACK_POWER[CLASS_PICK_VAL]) * EXP_TABLE_UI[LEVEL_NOW_UI - 1][0] * Stats_UI.STAT[1] * Stats_UI.LEVEL_NOW) // 4
                Attack_2 = RAND_HIT(int(ATTACK_POWER[CLASS_PICK_VAL + 1]), int(ATTACK_POWER[CLASS_PICK_VAL + 1]) * EXP_TABLE_UI[LEVEL_NOW_UI - 1][0] * Stats_UI.STAT[1] * Stats_UI.LEVEL_NOW) // 4
            Mana_1 = RAND_HIT(int(ATTACK_MANA[CLASS_PICK_VAL]), int(ATTACK_MANA[CLASS_PICK_VAL]) * EXP_TABLE_UI[LEVEL_NOW_UI - 1][0]) * 3
            Mana_2 = RAND_HIT(int(ATTACK_MANA[CLASS_PICK_VAL + 1]), int(ATTACK_MANA[CLASS_PICK_VAL + 1]) * EXP_TABLE_UI[LEVEL_NOW_UI - 1][0]) * 3
            MOB_ATTACK = MOB_HIT(1, Data.Mob_Data.mob_data_tab[RAND - 1][7])
            if CURRENT_MANA > 0 and CURRENT_HP > 0:
                print(Lang_TAB[LANG_INDEX][33])
                print(f"1. {Lang_TAB[LANG_INDEX][34]}" % (ATTACK_NAMES[CLASS_PICK_VAL], Attack_1, Mana_1))
                print(f"2. {Lang_TAB[LANG_INDEX][34]}" % (ATTACK_NAMES[CLASS_PICK_VAL + 1], Attack_2, Mana_2))
                ATTACK_CHOOSE = int(input(Lang_TAB[LANG_INDEX][26]))
                if ATTACK_CHOOSE == 1:
                    if CURRENT_MANA < Mana_1:
                        print(Lang_TAB[LANG_INDEX][27])
                    else:
                        UI.__Fight_Center_UI__(UI.UI_LEN)
                        print(Lang_TAB[LANG_INDEX][28] % (MOB_NAME, Attack_1))
                        UI.__Fight_Center_UI__(UI.UI_LEN)
                        CURRENT_MANA = CURRENT_MANA - Mana_1
                        MOB_HP_NOW = MOB_HP_NOW - Attack_1
                elif ATTACK_CHOOSE == 2:
                    if CURRENT_MANA < Mana_2:
                        Func.endl()
                        print(Lang_TAB[LANG_INDEX][27])
                        Func.endl()
                    else:
                        UI.__Fight_Center_UI__(UI.UI_LEN)
                        print(Lang_TAB[LANG_INDEX][28] % (MOB_NAME, Attack_2))
                        UI.__Fight_Center_UI__(UI.UI_LEN)
                        CURRENT_MANA = CURRENT_MANA - Mana_2
                        MOB_HP_NOW = MOB_HP_NOW - Attack_2
                else:
                    print(Lang_TAB[LANG_INDEX][29])
                
                if MOB_HP_NOW > 0:
                    print(Lang_TAB[LANG_INDEX][30] % (MOB_NAME, MOB_ATTACK_NAME, MOB_ATTACK))
                    UI.__Fight_Center_UI__(UI.UI_LEN)
                    Func.endl()
                    CURRENT_HP = CURRENT_HP - MOB_ATTACK
                    input(Lang_TAB[LANG_INDEX][10])
                    Func.endl()
                    Check_MANA_HP_T_MONEY(CURRENT_MANA, CURRENT_HP, MIN_MOB_MON_T, MAX_MOB_MON_T, MOB_NAME, LANG_INDEX)

            if MOB_HP_NOW < 0:
                Func.endl()
                MONEY = Gain_Money(MIN_MOB_MONEY, MAX_MOB_MONEY)
                EXP = Gain_exp(MIN_MOB_EXP, MAX_MOB_EXP)
                print(Lang_TAB[LANG_INDEX][31] % MOB_NAME)
                print(Lang_TAB[LANG_INDEX][32] % (MONEY, EXP))
                Stats_UI.FLOOR_NUM = Stats_UI.FLOOR_NUM + 1
                Stats_UI.MONEY_STAT = Stats_UI.MONEY_STAT + MONEY
                Stats_UI.EXP_NOW = Stats_UI.EXP_NOW + EXP
                input(Lang_TAB[LANG_INDEX][10])
            Func.cls()
            Func.endl()
    elif OPTION == 2:
        Back_To_Main()

#Main Fight
def Start_Fight(LANG_INDEX):
    RAND_0 = random.randint(1, Data.Mob_Data.Line_Count - 1)
    MOB_INDEX = Sort_Mob_to_Player(int(Data.Mob_Data.mob_data_tab[RAND_0 - 1][1]), Stats_UI.LEVEL_NOW)
    RAND = random.randint(1, MOB_INDEX + 1)
    RAND_BOSS = Random_Number_BOSS()
    Func.endl()

    CURRENT_HP = int(Stats_UI.STAT[3]) + (Stats_UI.STAT_TO_ADD[3] * Stats_UI.LEVEL_NOW)
    CURRENT_MANA = int(Stats_UI.STAT[4]) + (Stats_UI.STAT_TO_ADD[4] * Stats_UI.LEVEL_NOW)

    if Stats_UI.FLOOR_NUM % 5 == 0:
        Boss_Fight(RAND_BOSS, CURRENT_HP, CURRENT_MANA, LANG_INDEX)
    else:
        Fight(RAND, CURRENT_HP, CURRENT_MANA, LANG_INDEX)
        

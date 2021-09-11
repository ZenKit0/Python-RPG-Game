import sys
import Func

STAT_0 = 100
STAT_1 = 100
STAT_2 = 145

if STAT_0 >= STAT_1:
    UI_LEN = STAT_0
else:
    UI_LEN = STAT_1

CEIL_LEN = UI_LEN
FLOOR_LEN = UI_LEN

SYM_0 = '#'
SYM_1 = '-'

SYM_2 = '='
SYM_3 = '-'

def __Ceil_UI__(LEN):
    for x in range(1, LEN):
        sys.stdout.write(SYM_0),
    Func.endl()
    sys.stdout.write(SYM_0)
    for i in range(2, LEN - 1):
        sys.stdout.write(SYM_1)
        if i == LEN - 2:
            sys.stdout.write(SYM_0)

def __Ceil_UI_0__(LEN):
    for x in range(1, LEN):
        sys.stdout.write(SYM_0),
    Func.endl()
    sys.stdout.write(SYM_0)
    for i in range(2, LEN - 1):
        sys.stdout.write(SYM_1)
        if i == LEN - 2:
            sys.stdout.write(SYM_0)

def __Ceil_UI_BOSS__(LEN):
    for x in range(1, LEN):
        sys.stdout.write(SYM_2),
    Func.endl()
    sys.stdout.write(SYM_2)
    for i in range(2, LEN - 1):
        sys.stdout.write(SYM_3)
        if i == LEN - 2:
            sys.stdout.write(SYM_2)

def __Floor_UI__(LEN):
    Func.endl()
    sys.stdout.write(SYM_0)
    for i in range(2, LEN - 1):
        sys.stdout.write(SYM_1)
        if i == LEN - 2:
            sys.stdout.write(SYM_0)
            Func.endl()
    for x in range(1, LEN):
        sys.stdout.write(SYM_0)
    Func.endl()

def __Floor_UI_1__(LEN):
    sys.stdout.write(SYM_0)
    for i in range(2, LEN - 1):
        sys.stdout.write(SYM_1)
        if i == LEN - 2:
            sys.stdout.write(SYM_0)
            Func.endl()
    for x in range(1, LEN):
        sys.stdout.write(SYM_0)
    Func.endl()

def __Floor_UI_BOSS__(LEN):
    sys.stdout.write(SYM_2)
    for i in range(2, LEN - 1):
        sys.stdout.write(SYM_3)
        if i == LEN - 2:
            sys.stdout.write(SYM_2)
            Func.endl()
    for x in range(1, LEN):
        sys.stdout.write(SYM_2)
    Func.endl()

def __Center_UI__(LEN):
    Func.endl()
    for x in range(1, LEN):
        sys.stdout.write(SYM_1)
    Func.endl()

def __Center_UI_BOSS__(LEN):
    Func.endl()
    for x in range(1, LEN):
        sys.stdout.write(SYM_3)
    Func.endl()

def __Fight_Center_UI__(LEN):
    for x in range(1, LEN // 2):
        sys.stdout.write(SYM_1)
    Func.endl() 
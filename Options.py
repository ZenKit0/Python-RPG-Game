from Options_arch.Lang import Lang_TAB, Language

def Option_Open(LANG_INDEX):
    Options_tab = [Lang_TAB[LANG_INDEX][43]]
    for i in Options_tab:
        print(i)
    Option_Choose = int(input(Lang_TAB[LANG_INDEX][3]))
    if Option_Choose == 1:
        Language(LANG_INDEX)
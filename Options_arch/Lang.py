from Func import cls


Languages = ["1. English", "2. Polski"]

Lang_TAB = [
    [ #ENG
        "What do you want to do:", #0
        "1. Continue", #1
        "2. New Game", #2
        "Choose number of operation: ", #3
        "There is not an option with that number!", #4
        "1. Save Game", #5
        "2. Load Save", #6
        "Choose save to read: ", #7
        "Pick a number of save: ", #8
        "File doesn't exist!", #9
        "Click Enter to continue", #10
        "There are not save with this index!", #11
        "Choose number to save game: ", #12
        "Pick a number of save: ", #13
        "Class", #14
        "Money", #15
        "Floor", #16
        "1. Go fight!\n", #17
        "2. Go to shop!\n", #18
        "3. Save operations\n", #19
        "4. Options\n", #20
        "5. Quit!\n", #21
        "In %d sec app will be closed!", #22
        "Do you want to fight with %s?", #23
        "1. YES!", #24
        "2. NO.", #25
        "Write attack number: ", #26
        "You don't have enought Mana", #27
        "%s got hit from you: -%d HP.", #28
        "You choose wrong Attack!", #29
        "%s hit you from %s: -%d HP", #30
        "You killed %s", #31
        "Gained: %d EUR and %d EXP", #32
        "Choose attack: ", #33
        "%s Power: %d, Mana cost: %d", #34
        "You don't have enough HP!", #35
        "You don't have enough HP and Mana!", #36
        "%s took from you: %d EUR!", #37
        " SHOP ", #38
        "What do you want to do: \n1. Buy item \n2. Back \nChoose Number: ", #39
        "Choose item which you want to buy: ", #40
        "\nYou don't have enough money!", #41
        "\nPick correct item!", #42
        "1. Language", #43
        "Pick language: ", #44
        "Pick class: \n", #45
        "Choose number: ", #46
        "1. Mage", #47
        "2. Warrior", #48
        "3. Assassin", #49
        "4. Tank" #50
    ],
    [ #PL
        "Co chcesz zrobić:", #0
        "1. Kontynuuj", #1
        "2. Nowa Gra", #2
        "Wybierz numer: ", #3
        "Nie ma opcji z takim numerem!", #4
        "1. Zapisz Grę", #5
        "2. Wczytaj Grę", #6
        "Wybierz zapis do odczytu: ", #7
        "Wybierz numer zapisu: ", #8
        "Plik nie istnieje!", #9
        "Wciśnij enter aby kontynuować", #10
        "Nie ma zapisu z takim indexem!", #11
        "Wybierz numer do zapisu gry: ", #12
        "Wybierz numer zapisu: ", #13
        "Klasa", #14
        "Pieniądze", #15
        "Podłoga", #16
        "1. Idę walczyć!\n", #17
        "2. Idę do sklepu!\n", #18
        "3. Operacje zapisu\n", #19
        "4. Opcje\n", #20
        "5. Wyjdź!\n", #21
        "Za %d sek Gra się zamknie!", #22
        "Chcesz walczyć z %s?", #23
        "1. TAK!", #24
        "2. NIE.", #25
        "Napisz numer ataku: ", #26
        "Nie masz wystarczającej ilości many", #27
        "%s dostał od ciebie: -%d HP.", #28
        "Wybrałeś zły atak!", #29
        "%s uderzył się z %s: -%d HP", #30
        "You killed %s", #31
        "Zdobyłeś: %d EUR i %d EXP", #32
        "Wybierz atak: ", #33
        "%s Moc: %d, Koszt Many: %d", #34
        "Nie masz wystarczająco HP!", #35
        "Nie masz wystarczająco HP i Mana!", #36
        "%s ukradł ci: %d EUR!", #37
        " SKLEP ", #38
        "Co chcesz zrobić: \n1. Kupić przedmiot \n2. Wrócić \nWybierz numer: ", #39
        "Wybierz przedmiot który chcesz kupić: ", #40
        "\nNie masz wystarczająco pieniędzy!", #41
        "\nWybierz odpowiedni przedmiot!", #42
        "1. Język", #43
        "Wybierz Język: ", #44
        "Wybierz klasę: \n", #45
        "Wybierz numer: ", #46
        "1. Mag", #47
        "2. Wojownik", #48
        "3. Assassyn", #49
        "4. Obrońca" #50
    ]
]

def Language_start():
    for x in Languages:
        print(x)
    Lang_Choose = int(input("Pick language: "))
    if Lang_Choose == 1:
        cls()
        return 0
    elif Lang_Choose == 2:
        cls()
        return 1

def Language(LANG_INDEX):
    for x in Languages:
        print(x)
    Lang_Choose = int(input(Lang_TAB[LANG_INDEX][44]))
    if Lang_Choose == 1:
        cls()
        return 0
    elif Lang_Choose == 2:
        cls()
        return 1
    
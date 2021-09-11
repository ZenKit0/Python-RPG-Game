LEN_F = open("Data/Character_Data.txt", "r")
Line_Count = len(LEN_F.readlines())

Char_data = open("Data/Character_Data.txt", "r")
Char_data.readline()

char_data_tab = []

for x in range(1, Line_Count):
    data = Char_data.readline()
    char_data_tab.append(data.split(' ')) 

#0 = Class Name, 1 = 1 attack name, 2 = 1 attack power, 3 = 2 attack name, 4 = 2 attack power, 5 = 1 atack mana, 6 = 2 attack mana
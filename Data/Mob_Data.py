LEN_F = open("Data/Mob_Data.txt", "r")
Line_Count = len(LEN_F.readlines())

Mob_data = open("Data/Mob_Data.txt", "r")
Mob_data.readline()

mob_data_tab = []

for x in range(1, Line_Count):
    data = Mob_data.readline()
    mob_data_tab.append(data.split(' '))
LEN_F = open("Data/Boss_Data.txt", "r")
Line_Count = len(LEN_F.readlines())

Boss_data = open("Data/Boss_Data.txt", "r")
Boss_data.readline()

boss_data_tab = []

for x in range(1, Line_Count):
    data = Boss_data.readline()
    boss_data_tab.append(data.split(' '))
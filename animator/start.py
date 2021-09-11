import sys
import time
import os

logo = [
    ["#", "##", "###", "####", "######", "#######", "########", "#########"]
]

sym = "#"
data = []

LENGTH = 25

for x in range(0, LENGTH):
    os.system("cls")
    data.append(sym)
    #print(logo[0][x])
    print(data[x])
    sym += "#"
    time.sleep(0.005)


for x in range(0, LENGTH):
    os.system("cls")
    print(data[LENGTH - 1])
    #data.append(sym)
    #print(logo[0][x])
    print(data[x])
    #sym += "#"
    time.sleep(0.005)

input()#z
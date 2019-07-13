import webbrowser
import random
import time

playlist_choice = input("Do you want watch car or animal videos for your breaks?\nEnter A or C: ").upper()


total_breaks = int(input('How many breaks would you like to take? '))
break_occurance = int(input("How often would you like to take a break? (in seconds)  "))
break_count = 0
animal_playlist = ["https://www.youtube.com/watch?v=mwENYk66q6M",",https://www.youtube.com/watch?v=pCUtPE4cAsk","https://www.youtube.com/watch?v=RKU6x1n9Hak"]
car_playlist = ["https://www.youtube.com/watch?v=l85DvmhSvrQ","https://www.youtube.com/watch?v=VXS5xgKk-mU","https://www.youtube.com/watch?v=q3gxOpv8cxc"]

while (total_breaks>break_count):
    if playlist_choice == 'A':
        time.sleep(break_occurance)
        webbrowser.open(random.choice(animal_playlist))
        break_count += 1
    elif playlist_choice == 'C':
        time.sleep(break_occurance)
        webbrowser.open(random.choice(car_playlist))
        break_count += 1

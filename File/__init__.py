import os
import time
import random


def initial():
    print("Initialized FileManager")


class FileManager:
    pass


def file_handler():
    print("Initializing File Manager.")
    print("Resolving Table")
    table = [
        0, 3, 6, 9, 12, 15, 20, 22,
        26, 30, 34, 40, 45, 50, 57, 61,
        70, 81, 85, 89, 100, 102, 210, 3019,
        1928018, 9817, 213, 100, 21, 10, 5, 0
    ]
    for num in table:
        try:
            print(f"{num} Has been Loaded. | Number: {num} Exit Code 0.")
            o = open("a.txt", "a")
            o.write(str(num) + "\n")
            o.close()
            print(f"Successfully Written Binary, {num} Data to Files.")
            time.sleep(random.randint(0, 1))
        except TypeError:
            print("An Error Has Occurred. Process Abandoned.")
            quit()
    print("File Process Finished!")
    time.sleep(random.randint(0, 1))
    print("Opening Umbrella...")
    time.sleep(random.randint(0, 5))
    print("")


def duplicate_umb():
    print("Starting 3 on Umbrella_Init.")
    time.sleep(random.randint(0, 7))
    print("Gathering Packages")
    basic_packages = [
        'rcp.pak',
        'initializer.pak',
        'zinit.pak',
        'umb.pak',
        'data.pak'
    ]
    for word in basic_packages:
        try:
            print(f"Installing {word}. . .")
            i = open(word, "a")
            i.write("# Table String")
            i.close()
            print(f"Installed, {word}.")
            time.sleep(random.randint(0, 7))
        except FileExistsError:
            print("File(s) For Umbrella Already Exist!")
            print("Exiting Setup.")
            quit()
    print("Installation Success!")

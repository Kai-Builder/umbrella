# Umbrella Installer
# Get Started
import sys
import getopt
import os
import time
import subprocess

import random

args = ["--fast", "--org", "--installer", "--dontindex", "-cancelafter"]


dir = os.getcwd()


def rcp_dev():
    print("You are Currently Running a Joint of RCP (DERIVED).")
    print("Full Prompt @ https://github.com/Roe-s-Command-Prompt/RCP")
    global command
    while True:
        command = input(">>>")
        if command.strip() == "umbrella":
            print("What Would you Like to Do With Umbrella?")
            print("[umbrella install <mod>] -- Installs <mod>. Classic!")
            print("[umbrella switch <bool>] -- Switches <bool> To String.")
            print("[umbrella install module(self)] -- Concatenates Self (Umbrella) To a Module, Then Installs "
                  "it.\n\tOutput: umbrella install umbrella")
            print("[umbrella kill self] -- Quits the Terminal.")
            print("[umbrella help CLI] -- This Teaches you Umbrella's CLI (Command Line Interface).")
            print("[umbrella install argcli] -- This is the Sys.Module For the ARGCLI Command Prompt. (in-CLI)")
            print("[umbrella agent] -- This is the Umbrella Agent Module. Comes out-of-the-box.")
            print("[umbrella C] -- This is the C Release Of Umbrella. Requires the UID (Umbrella Install driver).")
            print("[umbrella index UmbrellaList.txt] -- Gives you a clear InSight Of UmbrellaLists And how they work.")
            print("[umbrella execute <file>] -- Executes <file>")
        elif command.strip() == "umbrella install RCP (DERIVED)":
            print("Installing RCP (DERIVED).")
            os.system("git clone https://github.com/Roe-s-Command-Prompt/RCP")
            print(f"Installed RCP (DERIVED) In Directory {dir}\RCP\RCP1.0.4.exe")
        elif command.strip() == "umbrella install help.txt":
            print("Installing Help.txt")
            p = open("help.txt", "w")
            p.write("Getting Started With Umbrella.\n"
                    "Umbrella Is a Installer App For RCP (DERIVED) (https://github.com/Roe-s-Command-Prompt/RCP). It uses "
                    "Python3 For All It's Functionality.\n "
                    "It only installs Features. NOT Teach you them.\n"
                    "If you want to support Umbrella, Contribute https://github.com/Roe-s-Command-Prompt/RCP here.")
            p.close()
            time.sleep(random.randint(0, 10))
            print("Installed Help.txt.")
        elif command.strip() == "umbrella switch":
            print("Variable")
            va = input(">>>")
            if va == "true":
                print("false")
            else:
                print("true")
        elif command.strip() == "umbrella install module(self)":
            os.system("git clone https://github.com/Kai-Builder/umbrella")
        elif command.strip() == "umbrella kill self":
            quit()
        elif command.strip() == "umbrella help CLI":
            print("The CLI Is a Command Prompt Way to execute commands without leaving the Windows Command "
                  "Prompt.\nThis Feature isn't available "
                  "\nYet But when it is I'll be sure to let you know.")
        elif command.strip() == "umbrella install argcli":
            print("ArgClient is a C++ Program that is More Powerful in terms of what it allows you to accomplish with "
                  "the IPCLI. (In Program Command Line Interface)")
            print("AC Isn't available in the pre-release Of Umbrella, But is sure to come in future updates. Thanks!")
        elif command.strip() == "umbrella agent":
            print("The Umbrella Agent"
                  "Is a Simple Monitor System to Test out Different VSYSTEMS."
                  "For Use, Type umbrella agent <foo> To Use Commands.")
        elif command.strip() == "umbrella C":
            print("nil")
        elif command.strip() == "umbrella index UmbrellaList.txt":
            print("Umbrella Lists are simple ways to manage the amount of storage That goes into UB.\n\n\tWritten In "
                  "C++\n\tPublished in Python.")
        elif command.strip() == "umbrella execute":
            print("Finding file ?")
            i = input(">")
            subprocess.call([i])
        elif command.strip() == "printer":
            print("Opening Printer, Modified And Re-Published By Kai-Builder.")
            print("Speak into the printer.")
            u = input(">")
            print(u)
        elif command.strip() == "":
            print("nil")
        else:
            print(f"Umbrella Client Does not recognize {command} As a Valid Command.\n\nContribute At https://github.com/Kai-Builder/umbrella")
print("Booting: If you have trouble booting, read the descripton to see requirements.")
#tools/librarys
import time
import getpass
#camera load
import numpy as np
import cv2
CAPTURE = False
#dir load
import os
os.chdir("/home")
#numgame load
NUMGAME = False
i = 0
import random
#calc load
CALC = False
import math
#count load
c = -1
password = getpass.getpass("Enter Admin Password(default 1234): ")
if password == '1234':
    print("=== AxiomDOS ===")
    print("= Welcome User =")
    print("there are some bugs")
    print("Type HELP for commands")
    while 1<2:
        dos = input()
        if dos == 'HELP':
            print("here are some codes to get started!")
            print("VER -- shows version for sh and c+a")
            print("TIME -- shows the time in your time zone")
            print("DATE -- shows the year/month/day")
            print("CAPTURE -- opens a camera app")
            print("OPEN -- opens a file")
            print("DIR -- shows directory")
            print("CD -- changes directory")
            print("CLS -- clears shell")
            print("NUMGAME -- opens a simple nuber game")
            print("CALC -- opens a calculator")
            print("exit -- why would you need a definition")
        else:
            if dos == 'VER':
                print("Version -- sh-0.2, C+A-1.3")
            else:
                if dos == 'TIME':
                    print(time.strftime("%H:%M"))
                    print(time.strftime("%I:%M"))
                else:
                    if dos == 'EXIT':
                        print("bye bye")
                        quit()
                    else:
                        if dos == 'DATE':
                            print(time.strftime("%D"))
                        else:
                            if dos == 'NUMGAME':
                                NUMGAME  = True
                                while NUMGAME == True:
                                    guess = input("pick a number 1-3 or type DOS to leave to DOS ")
                                    number = random.randint(1,3)
                                    if guess.isdigit() == number:
                                        print("correct +1 point see points at end")
                                        i = i + 1
                                    else:
                                        if guess == 'DOS':
                                            print("you had ", i, " points")
                                            NUMGAME = False
                                        else:
                                            print("Good Try! better luck next time.")
                            else:
                                if dos == 'CALC':
                                    CALC == True
                                    print("calculator codes: add, subtract, divide, multiply, sqrt, DOS")
                                    while CALC == True:
                                        calc = input()
                                        if calc == 'add':
                                            digit1 = float(input("enter first digit: "))
                                            digit2 = float(input("enter second digit: "))
                                            answer = digit1 + digit2
                                            print(answer)
                                        if calc == 'subtract':
                                            digit3 = float(input("enter first digit: "))
                                            digit4 = float(input("enter second digit: "))
                                            answer = digit3 - digit4
                                            print(answer)
                                        if calc == 'divide':
                                            digit5 = float(input("enter first digit: "))
                                            digit6 = float(input("enter second digit: "))
                                            answer = digit5 / digit6
                                            print(answer)
                                        if calc == 'multiply':
                                            digit7 = float(input("enter first digit: "))
                                            digit8 = float(input("enter second digit: "))
                                            answer = digit7 * digit8
                                            print(answer)
                                        if calc == 'sqrt':
                                            digit = float(input("enter digit: "))
                                            answer = math.sqrt(digit)
                                            print(answer)
                                        if calc == 'DOS':
                                            print("why): bye bye")
                                            CALC = False
                                        else:
                                            print("may you pls type ona those codes up there")
                                else:
                                    if dos == "DIR":
                                        for item in os.listdir("."):
                                            print(item)
                                    else:
                                        if dos == "CD":
                                            path = input("New Directory: ")
                                            if os.path.isdir(path):
                                                print("success(:")
                                            else:
                                                print("path not found|:")
                                        else:
                                            if dos == 'COUNT':
                                                a = int(input("count to: "))
                                                time.sleep(10)
                                                print("btw this timer goes in centurys not seconds or minutes")
                                                while c!=a:
                                                    time.sleep(3153599990)
                                                    c = c + 1
                                                    print(c, "day")
                                            else:
                                                if dos == 'OPEN':
                                                    openfile = input("please type file in directory: ")
                                                    try:
                                                        with open(openfile, "r") as f:
                                                            print(f.read())
                                                    except Exception as e:
                                                        print("error:", e)                                 
                                                else:
                                                    if dos == 'NEWS':
                                                        print("=== AXIOM NEWS ===")
                                                        print("ver 1.3 Y26/M11/D01")
                                                        print("planned character")
                                                        print("   bug fixes")
                                                        print("_______________________")
                                                        print("stay tuned for updates")
                                                    else:
                                                        if dos == 'DOS':
                                                            print()
                                                        else:
                                                            if dos == 'CLS':
                                                                os.system("cls")
                                                            else:
                                                                if dos == 'CAPTURE':
                                                                    CAPTURE==TRUE
                                                                    cap = cv2.VideoCapture(0, cv2.CAP_V4L2)
#                                                                    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
#                                                                    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
                                                                    time.sleep(2)
                                                                    while CAPTURE==True:
                                                                        ret, frame = cap.read()
                                                                        cv2.imshow('frame', frame)
                                                                        if cv2.waitKey(1) == ord('q'):
                                                                            break
                                                                        cap.release()
                                                                        cv2.destroyAllWindows()
                                                                    else:
                                                                        print("command not found):")
else:
    print("wrong, please try again by rebooting")

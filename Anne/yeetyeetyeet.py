#!/usr/bin/env python3
import os
import time

clear = lambda: os.system('cls')

def FailAnswer():
    print("I require yes or no only if you cant even spell you dont deserve a komputer!")
    time.sleep(5)

def question():
    print("So did you just say yeet three times?")
    ans = input()
    if ans not in ("yes","no"):
        FailAnswer()
        clear()
        question()
    else:
        question2()

def question2():
    print("and you thought that this was a good idea?")
    ans = input()
    if ans not in ("yes","no"):
        FailAnswer()
        clear()
        question2()
    else:
        finisher()

def finisher():
    print("well look i need you to really think about your shitty vocabulary and your words")
    time.sleep(5)
    print("If you want to use me for a good purpose then use me otherwise i am going ot leave")
    time.sleep(5)
    print("turn me back on when you are finished being a fuck boy")
    time.sleep(5)
    os.system("shutdown now")

def main():
    question()

if __name__ == "__main__":
    main()

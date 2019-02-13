#!/usr/bin/env python3

def SuperMath():
    print("Throw me that Equation")
    equation = input().split()
    if equation[0] in ("yeet","*","cool"):
        print("Well that equals the Yeetest Shit you could ever imagine my homie-G")
    else:
        print("LAME")

def main():
    print("what do you want to do?")
    ans = input()
    if ans == "supermath":
        SuperMath()

if __name__ == "__main__":
    main()

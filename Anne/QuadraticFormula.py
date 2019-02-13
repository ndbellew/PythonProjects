#!/bin/python3

def QuadraticFormula (a,b,c):
    val1,val2 = 0,0
    sqB = b**2
    try:
        val1 = (-b+(sqB-4*a*c)**.5)/(2*a)
        val2 = (-b-(sqB-4*a*c)**.5)/(2*a)
    except ArithmeticError:
        print("One of the values was not good")
    return val1,val2

def main():
    abc = input("input a, b, and c in one line with spaces seperating.\n").split()
    a,b,c = float(abc[0]),float(abc[1]),float(abc[2])
    ans1,ans2 = QuadraticFormula(a,b,c)
    print("your answers are the following\n",ans1)
    print(ans2)

if __name__ == "__main__":
    main()

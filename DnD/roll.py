import random

def roll():
    return random.randint(5,20)


def main():
    print("Strength: ",roll())
    print("Dexterity: ", roll())
    print("Constitution: ",roll())
    print("Intelligence: ",roll())
    print("Wisdom: ",roll())
    print("Charisma: ",roll())


if __name__=="__main__":
    main()

import random


# what happens when you always swap door given one of the wrong doors is opened
def switchdoor(n):
    correct_times = 0
    for i in range(0, n):
        correct_door = random.randint(0, 2)
        door_picked = random.randint(0, 2)
        # if the wrong door is picked at first then you always switch to the right door
        if door_picked != correct_door:
            correct_times += 1
    print(correct_times)


# what happens when you never swap door given one of the wrong doors is opened
def dontswitch(n):
    correct_times = 0
    for i in range(0, n):
        correct_door = random.randint(0, 2)
        door_picked = random.randint(0, 2)
        # only correct when you pick the correct door at the start
        if door_picked == correct_door:
            correct_times += 1
    print(correct_times)


# convenience wrapper
def main(n):
    switchdoor(n)
    dontswitch(n)


if __name__ == "__main__":
    n = int(input("how many times to iterate? "))
    main(n)

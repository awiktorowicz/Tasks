from fastapi import FastAPI
import random
import math

app = FastAPI()


@app.get('/')
# Random number generator
def random_numbers():
    global y, x
    INTEGERS = 100
    sumX = 0
    sumY = 0

    # Random number generator
    scanner = open("numbers.txt", "w")
    for i in range(INTEGERS):
        x = random.randrange(0, INTEGERS)
        y = random.randrange(0, INTEGERS)
        scanner.write(str(x) + ", " + str(y))
        scanner.write("\n")
        sumX += x
        sumY += y
    scanner.close()

    # Find optimal center coordinates
    perfectX = sumX / INTEGERS
    perfectY = sumY / INTEGERS

    # Grouping
    first_group = []
    second_group = []
    third_group = []
    fourth_group = []

    scanner = open("numbers.txt", "r")

    for i in range(INTEGERS):
        reader = scanner.readline()
        result = [i.strip() for i in reader.split(',')]
        d = math.sqrt(pow(perfectX - int(result[0]), 2) + pow(perfectY - int(result[1]), 2))

        if d >= (0.875 * INTEGERS):
            fourth_group.insert(i, [int(result[0]), int(result[1])])
        elif (0.875 * INTEGERS) > d >= (0.5 * INTEGERS):
            third_group.insert(i, [int(result[0]), int(result[1])])
        elif (0.5 * INTEGERS) > d >= (0.125 * INTEGERS):
            second_group.insert(i, [int(result[0]), int(result[1])])
        elif (0.125 * INTEGERS) > d:
            first_group.insert(i, [int(result[0]), int(result[1])])

    scanner.close()

    # toString
    toString = "The most suitable group: " + str(first_group)

    return toString

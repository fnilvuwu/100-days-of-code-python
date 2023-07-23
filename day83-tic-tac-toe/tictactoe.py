array_x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
def displayTable(array_x):
    for i in range(3):
        for j in range(3):
            print(f"| {array_x[i][j]} |", end="")
            if j == 2:
                print("\n---------------")

def changeElementX(array_x, x, y):
    array_x[x][y] = "x"
    return array_x

def changeElementO(array_x, x, y):
    array_x[x][y] = "o"
    return array_x

def checkValidBox(array_x, x, y):
    if array_x[x][y] != "x" and array_x[x][y] != "o":
        return True
    return False

        

def checkWinX(array_x):
    if array_x[0][0] == "x" and array_x[0][1] == "x" and array_x[0][2] == "x":
        print("x win")
        return True
    elif array_x[1][0] == "x" and array_x[1][1] == "x" and array_x[1][2] == "x":
        print("x win")
        return True
    elif array_x[2][0] == "x" and array_x[2][1] == "x" and array_x[2][2] == "x":
        print("x win")
        return True
    elif array_x[0][0] == "x" and array_x[1][1] == "x" and array_x[2][2] == "x":
        print("x win")
        return True
    elif array_x[0][2] == "x" and array_x[1][1] == "x" and array_x[2][0] == "x":
        print("x win")
        return True
    elif array_x[0][2] == "x" and array_x[1][2] == "x" and array_x[2][2] == "x":
        print("x win")
        return True
    elif array_x[0][1] == "x" and array_x[1][1] == "x" and array_x[2][1] == "x":
        print("x win")
        return True
    elif array_x[0][0] == "x" and array_x[1][0] == "x" and array_x[2][0] == "x":
        print("x win")
        return True

def checkWinY(array_x):
    if array_x[0][0] == "o" and array_x[0][1] == "o" and array_x[0][2] == "o":
        print("o win")
        return True
    elif array_x[1][0] == "o" and array_x[1][1] == "o" and array_x[1][2] == "o":
        print("o win")
        return True
    elif array_x[2][0] == "o" and array_x[2][1] == "o" and array_x[2][2] == "o":
        print("o win")
        return True
    elif array_x[0][0] == "o" and array_x[1][1] == "o" and array_x[2][2] == "o":
        print("o win")
        return True
    elif array_x[0][2] == "o" and array_x[1][1] == "o" and array_x[2][0] == "o":
        print("o win")
        return True
    elif array_x[0][2] == "o" and array_x[1][2] == "o" and array_x[2][2] == "o":
        print("o win")
        return True
    elif array_x[0][1] == "o" and array_x[1][1] == "o" and array_x[2][1] == "o":
        print("o win")
        return True
    elif array_x[0][0] == "o" and array_x[1][0] == "o" and array_x[2][0] == "o":
        print("o win")
        return True

gameOver = False
while not gameOver:
    displayTable(array_x)
    print("X-Turn")
    x, y = input("Enter x-and-y-coord: ").split()
    x = int(x)
    y = int(y)
    while not checkValidBox(array_x, x, y):
        displayTable(array_x)
        print("X-Turn")
        print("Coordinate not valid")
        x, y = input("Enter x-and-y-coord: ").split()
        x = int(x)
        y = int(y)

    array_x = changeElementX(array_x, x, y)
    if checkWinX(array_x) or checkWinY(array_x):
        gameOver = True
    displayTable(array_x)

    print("O-Turn")
    x, y = input("Enter x-and-y-coord: ").split()
    x = int(x)
    y = int(y)

    while not checkValidBox(array_x, x, y):
        displayTable(array_x)
        print("O-Turn")
        print("Coordinate not valid")
        x, y = input("Enter x-and-y-coord: ").split()
        x = int(x)
        y = int(y)

    array_x = changeElementO(array_x, x, y)

    if checkWinX(array_x) or checkWinY(array_x):
        gameOver = True
model = \
    [
        ["-", "-", "-"],
        ["-", "-", "-"],
        ["-", "-", "-"],
    ]

model2 = \
    [
        [model[0][0], model[1][0], model[2][0]],
        [model[0][1], model[1][1], model[2][1]],
        [model[0][2], model[1][2], model[2][2]]
    ]


def checkRowsX():
    global win
    count1 = model[0].count("x")
    count2 = model[1].count("x")
    count3 = model[2].count("x")

    if count1 == 3:
        print("X vann på rad 1!")
        win = True
    if count2 == 3:
        print("X vann på rad 2!")
        win = True
    if count3 == 3:
        print("X vann på rad 3!")
        win = True


def checkRowsO():
    global win
    count1 = model[0].count("o")
    count2 = model[1].count("o")
    count3 = model[2].count("o")

    if count1 == 3:
        print("O vann på rad 1!")
        win = True
    if count2 == 3:
        print("O vann på rad 2!")
        win = True
    if count3 == 3:
        print("O vann på rad 3!")
        win = True


def checkColumns():
    global win
    if model[0][0] == model[1][0] and model[1][0] == model[2][0] and model[0][0] != "-":
        if model[0][0] == "x":
            print("X vann på kolumn 1!")
            win = True
        elif model[0][0] == "o":
            print("O vann på kolumn 1!")
            win = True
    elif model[0][1] == model[1][1] and model[1][1] == model[2][1] and model[0][1] != "-":
        if model[0][1] == "x":
            print("X vann på kolumn 2!")
            win = True
        elif model[0][1] == "o":
            print("O vann på kolumn 2!")
            win = True
    elif model[0][2] == model[1][2] and model[1][2] == model[2][2] and model[0][2] != "-":
        if model[0][2] == "x":
            print("X vann på kolumn 3!")
            win = True
        elif model[0][2] == "o":
            print("O vann på kolumn 3!")
            win = True


def checkersModel():
    print("    1  ", "2", "  3")
    print("1", chr(124), model[0][0], chr(124), model[0][1], chr(124), model[0][2], chr(124))  # Rad 1
    print(" ", chr(45), chr(45), chr(45), chr(45), chr(45), chr(45), chr(45))
    print("2", chr(124), model[1][0], chr(124), model[1][1], chr(124), model[1][2], chr(124))  # Rad 2
    print(" ", chr(45), chr(45), chr(45), chr(45), chr(45), chr(45), chr(45))
    print("3", chr(124), model[2][0], chr(124), model[2][1], chr(124), model[2][2], chr(124))  # Rad 3


checkersModel()

win = False
playerX = True
playerO = False
while not win:
    while playerX:
        ###Spelare X
        xkoord = int(input("\nSpelare X: Skriv in X-koordinaten: "))
        ykoord = int(input("Spelare X: Skriv in Y-koordinaten: "))

        model[xkoord - 1][ykoord - 1] = "x"

        checkersModel()

        if "x" in model[0][0] and "x" in model[1][1] and "x" in model[2][2]:
            print("X vann diagonalt höger!")
            win = True
        if "x" in model[0][2] and "x" in model[1][1] and "x" in model[2][0]:
            print("X vann diagonalt vänster!")
            win = True

        checkRowsX()
        checkColumns()
        playerX = False
        playerO = True

        if win == True:
            playerO = False

    while playerO:
        ###Spelare O
        xkoord = int(input("\nSpelare O: Skriv in X-koordinaten: "))
        ykoord = int(input("Spelare O: Skriv in Y-koordinaten: "))

        model[xkoord - 1][ykoord - 1] = "o"

        checkersModel()

        if "o" in model[0][0] and "o" in model[1][1] and "o" in model[2][2]:
            print("O vann diagonalt höger!")
            win = True
        elif "o" in model[0][2] and "o" in model[1][1] and "o" in model[2][0]:
            print("O vann diagonalt vänster!")
            win = True

        checkRowsO()
        checkColumns()

        playerO = False
        playerX = True

        if win == True:
            playerX = False

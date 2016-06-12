def main():
    """TODO: Docstring for main.
    :returns: TODO

    """

    gameMap = {}

    fp = open("initial", "r")
    for i, each in enumerate(fp):
        each = each[:-1]
        line = each.split(" ")
        print "line: ", line
        for j, ch in enumerate(line):
            if ch == "1":
                gameMap[(i, j)] = 1
    fp.close()

    maxLifeNum = len(gameMap)
    maxTurnNum = 0

    for item in range(10000):
        newGameMap = {}
        for each in gameMap:
            if next(each[0]-1, each[1]-1, gameMap):
                newGameMap[each[0]-1, each[1]-1] = 1
            if next(each[0]-1, each[1], gameMap):
                newGameMap[each[0]-1, each[1]] = 1
            if next(each[0]-1, each[1]+1, gameMap):
                newGameMap[each[0]-1, each[1]+1] = 1
            if next(each[0], each[1]-1, gameMap):
                newGameMap[each[0], each[1]-1] = 1
            if next(each[0], each[1], gameMap):
                newGameMap[each[0], each[1]] = 1
            if next(each[0], each[1]+1, gameMap):
                newGameMap[each[0], each[1]+1] = 1
            if next(each[0]+1, each[1]-1, gameMap):
                newGameMap[each[0]+1, each[1]-1] = 1
            if next(each[0]+1, each[1], gameMap):
                newGameMap[each[0]+1, each[1]] = 1
            if next(each[0]+1, each[1]+1, gameMap):
                newGameMap[each[0]+1, each[1]+1] = 1
        gameMap = newGameMap

        if len(newGameMap)>maxLifeNum:
            maxLifeNum = len(newGameMap)
            maxTurnNum = item+1
            print "now max life number is ", maxLifeNum, " in turn ", maxTurnNum



def next(i, j, gameMap):
    """TODO: Docstring for next.
    :returns: TODO

    """
    try:
        flag = gameMap[(i,j)]
    except KeyError as e:
        flag = 0

    sum = 0

    for x in range(i-1, i+2):
        for y in range(j-1, j+2):
            if x==i and y == j:
                continue

            try:
                sum += gameMap[(x,y)]
            except KeyError as e:
                continue

    #print "x: ", x, "y: " , y, "sum: ", sum
    if flag == 0:
        if sum ==3:
            return 1
    else:
        if sum <2:
            return 0
        elif sum > 3:
            return 0
        else:
            return 1


if __name__ == "__main__":
    main()

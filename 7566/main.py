def main():
    """TODO: Docstring for main.

    :returns: void

    """
    weight = [509,838,924,650,604,793,564,651,697,649,747,787,701,605,644]
    weight.sort()
    weight.reverse()

    print weight
    max = 0
    maxPath = ''

    for i in range(32767):
        item = bin(i)
        item = item[2:]
        item = item.zfill(15)

        sum = 0
        for indexNum, j in enumerate(item):

            if j == '1':
                if sum+weight[indexNum] >= 5000:
                    if sum > max:
                        max = sum
                        maxPath = item[:indexNum]
                        break
                else:
                    sum += weight[indexNum]
        if sum > max:
            max = sum
            maxPath = item
        '''
        if i == 30:
            while(1):
                pass

            '''
    print "max = ", max
    print "path = ", maxPath

if __name__ == "__main__":
    main()

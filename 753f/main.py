from string import atoi


class Cloth():

    """Docstring for Cloth. """

    def __init__(self, price, number):
        """TODO: to be defined1. """
        self.number = number
        self.price = price

    def plus(self, amount):
        self.number += amount

    def rm(self, amount):
        self.number -= amount


def main():
    """TODO: Docstring for main.
    :returns: query sum

    """
    filename = '144043123647536.txt'
    querySum = 0
    clothList = []

    fp = open(filename, 'r')

    for each in fp:
        querySum = queryProcess(each, clothList, querySum)

    print querySum

def queryProcess(query, clothList, querySum):
    """TODO: Docstring for queryProcess.
    :returns: TODO

    """

    query = query.split(" ")

    if query[0][0] == 'q':
        lowBound = atoi(query[1])
        highBound = atoi(query[2])

        for each in clothList:
            if each.price >= lowBound and each.price <= highBound:
                querySum += each.number

        return querySum

    else:
        number = atoi(query[1])
        price = atoi(query[2])
        for i, each in enumerate(clothList):
            if each.price == price:
                if query[0][0] == 'u':
                    clothList[i].plus(number)
                elif query[0][0] == 'd':
                    clothList[i].rm(number)
                else:
                    print "wrong"
                    while(1):pass
                return querySum

        cloth = Cloth(price,number)
        clothList.append(cloth)
        return querySum


if __name__ == "__main__":
    main()

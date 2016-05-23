def main():
    """TODO: Docstring for main.
    :returns: TODO

    """

    maxVisitId = 0;
    maxVisit = 0;

    for i in range(500):
        filename = str(i)
        idTable = {}
        file_obj = open(filename, 'r')

        for idNumber in file_obj:
            try:
                idTable[idNumber]
            except Exception as e:
                idTable[idNumber] = 0
            finally:
                idTable[idNumber] = idTable[idNumber]+1

        for idNumber in idTable:
            if idTable[idNumber] > maxVisit:
                maxVisit = idTable[idNumber]
                maxVisitId = idNumber

    print "max visit: ", maxVisit
    print "id: ", maxVisitId


if __name__ == "__main__":
    main()

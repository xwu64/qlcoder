def main():
    """TODO: Docstring for main.
    :returns: TODO

    """
    filename = 'uv.txt'
    fileObj = open(filename, 'r')

    userList = set()

    for eachline in fileObj:
        eachline = eachline.split(' ')
        userList.add(eachline[1])

    print len(userList)
    pass

if __name__ == "__main__":
    main()
    pass

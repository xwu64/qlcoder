from struct import *

def main(filename):
    """TODO: Docstring for main.
    :returns: TODO

    """
    fHandle = open(filename, 'r')
    counter = 0
    while(1):
        counter +=1
        flag = fHandle.read(1)
        flag = unpack('>b', flag)
        flag = flag[0]
        if flag == 0:
            length = fHandle.read(4)
            length = unpack('>i', length)
            length = length[0]
            fwHandle = open(str(counter)+'jpg', 'w')
            fwHandle.write(fHandle.read(length))
            fwHandle.close()

        elif flag == 1:
            pass
        elif flag ==2:
            break
        else:
            print "error flag = ", flag




if __name__ == "__main__":
    filename = 'rf.data'
    main(filename)

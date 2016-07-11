s1 = ''

class node(object):

    """Docstring for node. """

    def __init__(self, symbol, frequency, leaf):
        """TODO: to be defined1. """
        self.symbol = symbol
        self.frequency = frequency
        self.leaf = leaf
        self.id = id

    def addChildren(self, leftChild, rightChild):
        """TODO: Docstring for addChildren.
        :returns: TODO

        """
        print "left F: ", leftChild.frequency, " S ", leftChild.symbol
        print "right F: ", rightChild.frequency, " S ", rightChild.symbol
        self.leftChild = leftChild
        self.rightChild = rightChild

    def setID(self,id):
        """TODO: Docstring for setID.
        :returns: TODO

        """
        self.id = id


def readFrequency(filename):
    """TODO: Docstring for readFrequency.
    :returns: TODO

    """
    fHandle = open(filename, "r")
    leave = []
    for each in fHandle:
        frequency = each.split(" ")
        frequency = frequency[-1]
        frequency = int(frequency[:-2])
        newNode = node(each[2], (frequency), True)
        leave.append(newNode)
    return leave

def printHuffTree(node):
    """TODO: Docstring for printHuffTree.

    :arg1: TODO
    :returns: TODO

    """
    if node.leaf == True:
        print node.symbol, " ", node.frequency
        return 0
    else:
        print node.frequency, "0"
        printHuffTree(node.leftChild)
        print node.frequency, "1"
        printHuffTree(node.rightChild)
        return 0


def readCode(filename):
    """TODO: Docstring for readCode.
    :returns: TODO

    """
    fHandle = open(filename, 'r')

    code = fHandle.read()
    fHandle.close()

    return code


def translator(node, code):
    """TODO: Docstring for translator.
    :returns: TODO

    """
    if code == '0':
        print "0"
        return node.leftChild
    else:
        print "1"
        return node.rightChild


def main():
    """TODO: Docstring for main.

    :arg1: TODO
    :returns: TODO

    """
    leave = readFrequency("Frequency")

    leave = sorted(leave, key = lambda node:node.frequency)
    for i, leaf in enumerate(leave):
        leaf.setID(i)

    while(1):
        if len(leave) == 1:
            break

        leave = sorted(leave, key = lambda node:node.frequency)

        '''
        for each in leave:
            print each.id, " ", each.symbol
        '''
        newNode = node(None, leave[0].frequency+leave[1].frequency, False)
        if leave[0].id < leave[1].id:
            newNode.addChildren(leave[0], leave[1])
        else:
            newNode.addChildren(leave[1], leave[0])
        newNode.setID(leave[1].id)

        leave.append(newNode)
        leave = leave[2:]

    #printHuffTree(leave[0])
    code = readCode("Code")

    nextNode = leave[0]
    global s1
    for each in code:
        #print each
    #    print nextNode.frequency
    #    print nextNode.symbol
        nextNode = translator(nextNode, each)
        if nextNode.leaf == True:
            s1+=nextNode.symbol
            nextNode = leave[0]
    print s1


if __name__ == "__main__":
    main()

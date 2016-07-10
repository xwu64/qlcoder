import math
import random


baseS = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
base = []

for each in baseS:
    base.append(each)


def encode(num):
    """TODO: Docstring for encode.
    :returns: TODO

    """
    if num / 10 ==0:
        return str(num)

    if num / 100 == 0:
        if num < 72:
            return 'A'+base[num-10]
        else:
            return 'Az'+base[num-72]

    digitNum = int(math.log10(num))
    str1 = ''
    num = num - 10**digitNum
    for each in range(digitNum):
        str1 += base[(num%62)]
        num = num/62
    return base[9+digitNum]+str1[::-1]


def decode(str1):
    """TODO: Docstring for decode.
    :returns: TODO

    """
    if len(str1) == 1:
        return int(str1)

    if str1[0] == 'A':
        if len(str1) == 2:
            return base.index(str1[1])+10
        else:
            return base.index(str1[2])+72

    digitNum = base.index(str1[0]) - 9
    num = 10 ** digitNum
    negStr1 = str1[::-1]
    negStr1 = negStr1[:-1]
    for i, each in enumerate(negStr1):
        num += base.index(each)*(62**i)
    return num


if __name__ == "__main__":
    for each in range(100):
        num = random.randint(0,10**40)
        str1 = encode(num)
        print "encode \n num=", num, "str=", str1
        num = decode(str1)
        print "decode \n str=", str1, "num=", num



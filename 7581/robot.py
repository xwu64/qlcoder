import urllib2
import md5
from datetime import date

def main(voteNum, userName):
    """TODO: Docstring for main.
    :returns: X number

    """
    today = date.today()
    year = str(today.year)
    month = str(today.month).zfill(2)
    day = str(today.day).zfill(2)


    voteNum = str(voteNum)

    print year+month+day+userName+voteNum
    item = 100000
    while 1:
        x = str(item)

        md5Value = md5.new(year+month+day+userName+voteNum+x).hexdigest()
        if md5Value[:6] == '000000':
            """
            print year+month+day+userName+voteNum+x
            print md5Value
            """
            return x
        item +=1



if __name__ == "__main__":
    xList = [None]*1000
    userName = raw_input("Username: ")
    today = date.today()
    year = str(today.year)
    month = str(today.month).zfill(2)
    day = str(today.day).zfill(2)
    filename = userName+year+month+day
    try:
        fHandle = open(filename, "r")
        for each in fHandle:
            each = each.split(" ")
            x = each[1]
            xList[int(each[0])] = x[:-1]
        fHandle.close()
        print xList
    except IOError, e:
        print "no record"

    for each in range(0,1000): # vote number range
        if xList[each] == None:
            x = main(each+1, userName)
            xList[each] = x
            indexNum = str(each+1)
            x = indexNum + x
            xList[int(x[:2])-1] = x[2:]
            xList[int(x[:3])-1] = x[3:]
            fHandle = open(filename, "w")
            for i, x in enumerate(xList):
                if x is not None:
                    fHandle.write(str(i)+" "+x+"\n")
            fHandle.close()
            url = "http://www.qlcoder.com/train/handsomerank?user="+userName+"&checkcode="+xList[each]
            uHandle = urllib2.urlopen(url)
        else:
            url = "http://www.qlcoder.com/train/handsomerank?user="+userName+"&checkcode="+xList[each]
            uHandle = urllib2.urlopen(url)
            continue




import threading
import urllib2
import time

def main(item):
    """TODO: Docstring for main.
    :returns: TODO

    """
    url = "http://www.qlcoder.com/train/spider3/{i}".format(i = item)
    previousHtml = ''
    previousGap = 0
    gap = 10.0
    maxGap = 0
    print url
    for each in range(20):
        uHandle = urllib2.urlopen(url)
        html = uHandle.read()
        '''
        print "1: ", previousHtml
        print "2: ", html
        print "gap:", gap
        '''
        if cmp(html, previousHtml): # not same return 1
            gap = gap*0.8
            previousHtml = html
        else:
            if gap>400:
                maxGap = maxGap + 60
                time.sleep(60)
                continue

            previousGap = gap
            gap = gap*2
            if gap>maxGap:
                maxGap = gap
        time.sleep(gap)
    print item, " ", maxGap


if __name__ == "__main__":
    threads = []
    print "create thread"
    for item in range(1,11):
        '''
        if item in [1,2,10,9]:
            continue
        '''
        t = threading.Thread(target=main, args= (item,))
        threads.append(t)

    print "start thread"
    for each in threads:
        each.start()

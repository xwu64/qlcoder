import urllib2
import re
from bs4 import BeautifulSoup

def main():
    """TODO: Docstring for main.
    :returns: TODO

    """

    sum = 0
    i = 0

    for item in range(0,175, 25):
        url = 'https://movie.douban.com/top250?start={num}&filter='.format(num = item)
        print url
        uHandle = urllib2.urlopen(url)
        rawHtml = uHandle.read()
        soup = BeautifulSoup(rawHtml)
        for each in soup.find_all('span', class_='rating_num'):
            sum += float(each.string)
            i+=1
            if i>165:
                print "166, ", sum
                print each.string
                break
        if i > 165:
            break




if __name__ == "__main__":
    main()

#!/usr/bin/python
# coding: utf-8
import os
import sys
import requests
import re
import urllib


def getUrl(name):
    r = requests.get("http://www.songtaste.com/music.php?tag=chart&dt=2016-03-28")
    print r
    # name = name.replace('/', '_')
    # print name
    if os.path.isdir("%s" % name):
        print 'The path is exist !'
    else: 
        os.mkdir("%s" % name)
        print 'creat over'
    reg = r'WL\("(.+?.),"(.+?.)"'
    gre = re.compile(reg)
    number = re.findall(gre,r.text)
    # arr = number[0][1].split(',')
    # print arr[1].replace('\"', '')
    x = 0
    for dd in number:
        print dd[1]
        url = 'http://www.songtaste.com/song/'
        url += dd[1]
        print url
        songurl = requests.get(url)
        reg = r'var strURL = \"(.+?.)\"'
        gre = re.compile(reg)
        number = re.findall(gre,songurl.text)
        if number:
            x+=1
            print x
            print name + '_'+ '%d' % x
            finalUrl = 'http://www.songtaste.com/time.php?str='
            finalUrl += number[0]
            finalUrl += '&sid='
            finalUrl += dd[1]
            print finalUrl
            try:
                urllib.urlretrieve(requests.get(finalUrl).text, './%s/%d.mp3' % (name, x))
            except UnicodeError,e:
                pass
            except UnboundLocalError,e:
                pass
            except Exception,e:
                pass
    print name + ' over'

if __name__ == "__main__":
    getUrl('2016-04-04')
    getUrl('2016-03-28')
    getUrl('2016-03-21')
    getUrl('2016-03-14')
    getUrl('2016-03-07')
    getUrl('2016-02-29')
    getUrl('2016-02-22')
    getUrl('2016-02-15')
    getUrl('2016-02-08')
    getUrl('2016-02-01')
    getUrl('2016-01-25')
    getUrl('2016-01-18')
    getUrl('2016-01-11')
    getUrl('2016-01-04')
    getUrl('2015-12-28')
    getUrl('2015-12-21')
    getUrl('2015-12-14')
    getUrl('2015-12-07')
    getUrl('2015-11-30')
    getUrl('2015-11-23')
    getUrl('2015-11-16')
    getUrl('2015-11-09')
    getUrl('2015-11-02')
    getUrl('2015-10-26')
    getUrl('2015-10-19')
    getUrl('2015-10-12')
    getUrl('2015-10-05')
    getUrl('2015-09-28')
    getUrl('2015-09-21')
    getUrl('2015-09-14')
    getUrl('2015-09-07')
    getUrl('2015-08-31')
    getUrl('2015-08-24')
    getUrl('2015-08-17')
    getUrl('2015-08-10')
    getUrl('2015-08-03')
    getUrl('2015-07-27')
    getUrl('2015-07-20')
    getUrl('2015-07-13')
    getUrl('2015-07-06')
    getUrl('2015-06-29')
    getUrl('2015-06-22')
    getUrl('2015-06-15')
    getUrl('2015-06-08')
    getUrl('2015-06-01')
    getUrl('2015-05-25')
    getUrl('2015-05-18')
    getUrl('2015-05-11')
    getUrl('2015-05-04')
    getUrl('2015-04-27')
    getUrl('2015-04-20')
    getUrl('2015-04-13')
    getUrl('2015-04-06')
    getUrl('2015-03-30')
    getUrl('2015-03-23')
    getUrl('2015-03-16')
    getUrl('2015-03-09')
    getUrl('2015-03-02')
    getUrl('2015-02-23')
    getUrl('2015-02-16')
    getUrl('2015-02-09')
    getUrl('2015-02-02')
    getUrl('2015-01-26')
    getUrl('2015-01-19')
    getUrl('2015-01-12')
    getUrl('2015-01-05')
    getUrl('2014-12-29')
    getUrl('2014-12-22')
    getUrl('2014-12-15')
    getUrl('2014-12-08')
    getUrl('2014-12-01')
    getUrl('2014-11-24')
    getUrl('2014-11-17')
    getUrl('2014-11-10')
    getUrl('2014-11-03')
    getUrl('2014-10-27')
    getUrl('2014-10-20')
    getUrl('2014-10-13')
    getUrl('2014-10-06')
    getUrl('2014-09-29')
    getUrl('2014-09-22')
    getUrl('2014-09-15')
    getUrl('2014-09-08')
    getUrl('2014-09-01')
    getUrl('2014-08-25')
    getUrl('2014-08-18')
    getUrl('2014-08-11')
    getUrl('2014-08-04')
    getUrl('2014-07-28')
    getUrl('2014-07-21')
    getUrl('2014-07-14')
    getUrl('2014-07-07')
    getUrl('2014-06-30')
    getUrl('2014-06-23')
    getUrl('2014-06-16')
    getUrl('2014-06-09')
    getUrl('2014-06-02')
    getUrl('2014-05-26')
    getUrl('2014-05-19')
    getUrl('2014-05-12')
    getUrl('2014-05-05')
    getUrl('2014-04-28')
    getUrl('2014-04-21')
    getUrl('2014-04-14')
    getUrl('2014-04-07')
    getUrl('2014-03-31')
    getUrl('2014-03-24')
    getUrl('2014-03-17')
    getUrl('2014-03-10')
    getUrl('2014-03-03')
    getUrl('2014-02-24')
    getUrl('2014-02-17')
    getUrl('2014-02-10')
    getUrl('2014-02-03')
    getUrl('2014-01-27')
    getUrl('2014-01-20')
    getUrl('2014-01-13')
    getUrl('2014-01-06')
    getUrl('2013-12-30')
    getUrl('2013-12-23')
    getUrl('2013-12-16')
    getUrl('2013-12-09')
    getUrl('2013-12-02')
    getUrl('2013-11-25')
    getUrl('2013-11-18')
    getUrl('2013-11-11')
    getUrl('2013-11-04')
    getUrl('2013-10-28')
    getUrl('2013-10-21')
    getUrl('2013-10-14')
    getUrl('2013-10-07')
    getUrl('2013-09-30')
    getUrl('2013-09-23')
    getUrl('2013-09-16')
    getUrl('2013-09-09')
    getUrl('2013-09-02')
    getUrl('2013-08-26')
    getUrl('2013-08-19')
    getUrl('2013-08-12')
    getUrl('2013-08-05')
    getUrl('2013-07-29')
    getUrl('2013-07-22')
    getUrl('2013-07-15')
    getUrl('2013-07-08')
    getUrl('2013-07-01')
    getUrl('2013-06-24')
    getUrl('2013-06-17')
    getUrl('2013-06-10')
    getUrl('2013-06-03')
    getUrl('2013-05-27')
    getUrl('2013-05-20')
    getUrl('2013-05-13')
    getUrl('2013-05-06')
    getUrl('2013-04-29')
    getUrl('2013-04-22')
    getUrl('2013-04-15')
    getUrl('2013-04-08')
    getUrl('2013-04-01')
    getUrl('2013-03-25')
    getUrl('2013-03-18')
    getUrl('2013-03-11')
    getUrl('2013-03-04')
    getUrl('2013-02-25')
    getUrl('2013-02-18')
    getUrl('2013-02-11')
    getUrl('2013-02-04')
    getUrl('2013-01-28')
    getUrl('2013-01-21')
    getUrl('2013-01-14')
    getUrl('2013-01-07')
    getUrl('2012-12-31')
    getUrl('2012-12-24')
    getUrl('2012-12-17')
    getUrl('2012-12-10')
    getUrl('2012-12-03')
    getUrl('2012-11-26')
    getUrl('2012-11-19')
    getUrl('2012-11-12')
    getUrl('2012-11-05')
    getUrl('2012-10-29')
    getUrl('2012-10-22')
    getUrl('2012-10-15')
    getUrl('2012-10-08')
    getUrl('2012-10-01')
    getUrl('2012-09-24')
    getUrl('2012-09-17')
    getUrl('2012-09-10')
    getUrl('2012-09-03')
    getUrl('2012-08-27')
    getUrl('2012-08-20')
    getUrl('2012-08-13')
    getUrl('2012-08-06')
    getUrl('2012-07-30')
    getUrl('2012-07-23')
    getUrl('2012-07-16')
    getUrl('2012-07-09')
    getUrl('2012-07-02')
    getUrl('2012-06-25')
    getUrl('2012-06-18')
    getUrl('2012-06-11')
    getUrl('2012-06-04')
    getUrl('2012-05-28')
    getUrl('2012-05-21')
    getUrl('2012-05-14')
    getUrl('2012-05-07')
    getUrl('2012-04-30')
    getUrl('2012-04-23')
    getUrl('2012-04-16')
    getUrl('2012-04-09')
    getUrl('2012-04-02')
    getUrl('2012-03-26')
    getUrl('2012-03-19')
    getUrl('2012-03-12')
    getUrl('2012-03-05')
    getUrl('2012-02-27')
    getUrl('2012-02-20')
    getUrl('2012-02-13')
    getUrl('2012-02-06')
    getUrl('2012-01-30')
    getUrl('2012-01-23')
    getUrl('2012-01-16')
    getUrl('2012-01-09')
    getUrl('2012-01-02')
    getUrl('2011-12-26')
    getUrl('2011-12-19')
    getUrl('2011-12-12')
    getUrl('2011-12-05')
    getUrl('2011-11-28')
    getUrl('2011-11-21')
    getUrl('2011-11-14')
    getUrl('2011-11-07')
    getUrl('2011-10-31')
    getUrl('2011-10-24')
    getUrl('2011-10-17')
    getUrl('2011-10-10')
    getUrl('2011-10-03')
    getUrl('2011-09-26')
    getUrl('2011-09-19')
    getUrl('2011-09-12')
    getUrl('2011-09-05')
    getUrl('2011-08-29')
    getUrl('2011-08-22')
    getUrl('2011-08-15')
    getUrl('2011-08-08')
    getUrl('2011-08-01')
    getUrl('2011-07-25')
    getUrl('2011-07-18')
    getUrl('2011-07-11')
    getUrl('2011-07-04')
    getUrl('2011-06-27')
    getUrl('2011-06-20')
    getUrl('2011-06-13')
    getUrl('2011-06-06')
    getUrl('2011-05-30')
    getUrl('2011-05-23')
    getUrl('2011-05-16')
    getUrl('2011-05-09')
    getUrl('2011-05-02')
    getUrl('2011-04-25')
    getUrl('2011-04-18')
    getUrl('2011-04-11')
    getUrl('2011-04-04')
    getUrl('2011-03-28')
    getUrl('2011-03-21')
    getUrl('2011-03-14')
    getUrl('2011-03-07')
    getUrl('2011-02-28')
    getUrl('2011-02-21')
    getUrl('2011-02-14')
    getUrl('2011-02-07')
    getUrl('2011-01-31')
    getUrl('2011-01-24')
    getUrl('2011-01-17')
    getUrl('2011-01-10')
    getUrl('2011-01-03')
    getUrl('2010-12-27')
    getUrl('2010-12-20')
    getUrl('2010-12-13')
    getUrl('2010-12-06')
    getUrl('2010-11-29')
    getUrl('2010-11-22')
    getUrl('2010-11-15')
    getUrl('2010-11-08')
    getUrl('2010-11-01')
    getUrl('2010-10-25')
    getUrl('2010-10-18')
    getUrl('2010-10-11')
    getUrl('2010-10-04')
    getUrl('2010-09-27')
    getUrl('2010-09-20')
    getUrl('2010-09-13')
    getUrl('2010-09-06')
    getUrl('2010-08-30')
    getUrl('2010-08-23')
    getUrl('2010-08-16')
    getUrl('2010-08-09')
    getUrl('2010-08-02')
    getUrl('2010-07-26')
    getUrl('2010-07-19')
    getUrl('2010-07-12')
    getUrl('2010-07-05')
    getUrl('2010-06-28')
    getUrl('2010-06-21')
    getUrl('2010-06-14')
    getUrl('2010-06-07')
    getUrl('2010-05-31')
    getUrl('2010-05-24')
    getUrl('2010-05-17')
    getUrl('2010-05-10')
    getUrl('2010-05-03')
    getUrl('2010-04-26')
    getUrl('2010-04-19')
    getUrl('2010-04-12')
    getUrl('2010-04-05')
    getUrl('2010-03-29')
    getUrl('2010-03-22')
    getUrl('2010-03-15')
    getUrl('2010-03-08')
    getUrl('2010-03-01')
    getUrl('2010-02-22')
    getUrl('2010-02-15')
    getUrl('2010-02-08')
    getUrl('2010-02-01')
    getUrl('2010-01-25')
    getUrl('2010-01-18')
    getUrl('2010-01-11')
    getUrl('2010-01-04')
    getUrl('2009-12-28')
    getUrl('2009-12-21')
    getUrl('2009-12-14')
    getUrl('2009-12-07')
    getUrl('2009-11-30')
    getUrl('2009-11-23')
    getUrl('2009-11-16')
    getUrl('2009-11-09')
    getUrl('2009-11-02')
    getUrl('2009-10-26')
    getUrl('2009-10-19')
    getUrl('2009-10-12')
    getUrl('2009-10-05')
    getUrl('2009-09-28')
    getUrl('2009-09-21')
    getUrl('2009-09-14')
    getUrl('2009-09-07')
    getUrl('2009-08-31')
    getUrl('2009-08-24')
    getUrl('2009-08-17')
    getUrl('2009-08-10')
    getUrl('2009-08-03')
    getUrl('2009-07-27')
    getUrl('2009-07-20')
    getUrl('2009-07-13')
    getUrl('2009-07-06')
    getUrl('2009-06-29')
    getUrl('2009-06-22')
    getUrl('2009-06-15')
    getUrl('2009-06-08')
    getUrl('2009-06-01')
    getUrl('2009-05-25')
    getUrl('2009-05-18')
    getUrl('2009-05-11')
    getUrl('2009-05-04')
    getUrl('2009-04-27')
    getUrl('2009-04-20')
    getUrl('2009-04-13')
    getUrl('2009-04-06')
    getUrl('2009-03-30')
    getUrl('2009-03-23')
    getUrl('2009-03-16')
    getUrl('2009-03-09')
    getUrl('2009-03-02')
    getUrl('2009-02-23')
    getUrl('2009-02-16')
    getUrl('2009-02-09')
    getUrl('2009-02-02')
    getUrl('2009-01-26')
    getUrl('2009-01-19')
    getUrl('2009-01-12')
    getUrl('2009-01-05')
    getUrl('2008-12-29')
    getUrl('2008-12-22')
    getUrl('2008-12-15')
    getUrl('2008-12-08')
    getUrl('2008-12-01')
    getUrl('2008-11-24')
    getUrl('2008-11-17')
    getUrl('2008-11-10')
    getUrl('2008-11-03')
    getUrl('2008-10-27')
    getUrl('2008-10-20')
    getUrl('2008-10-13')
    getUrl('2008-10-06')
    getUrl('2008-09-29')
    getUrl('2008-09-22')
    getUrl('2008-09-15')
    getUrl('2008-09-08')
    getUrl('2008-09-01')
    getUrl('2008-08-25')
    getUrl('2008-08-18')
    getUrl('2008-08-11')
    getUrl('2008-08-04')
    getUrl('2008-07-28')
    getUrl('2008-07-21')
    getUrl('2008-07-14')
    getUrl('2008-07-07')
    getUrl('2008-06-30')
    getUrl('2008-06-23')
    getUrl('2008-06-16')
    getUrl('2008-06-09')
    getUrl('2008-06-02')
    getUrl('2008-05-26')
    getUrl('2008-05-19')
    getUrl('2008-05-12')
    getUrl('2008-05-05')
    getUrl('2008-04-28')
    getUrl('2008-04-21')
    getUrl('2008-04-14')
    getUrl('2008-04-07')
    getUrl('2008-03-31')
    getUrl('2008-03-24')
    getUrl('2008-03-17')
    getUrl('2008-03-10')
    getUrl('2008-03-03')
    getUrl('2008-02-25')
    getUrl('2008-02-18')
    getUrl('2008-02-11')
    getUrl('2008-02-04')
    getUrl('2008-01-28')
    getUrl('2008-01-21')
    getUrl('2008-01-14')
    getUrl('2008-01-07')
    getUrl('2007-12-31')
    getUrl('2007-12-24')
    getUrl('2007-12-17')
    getUrl('2007-12-10')
    getUrl('2007-12-03')
    getUrl('2007-11-26')
    getUrl('2007-11-19')
    getUrl('2007-11-12')
    getUrl('2007-11-05')
    getUrl('2007-10-29')
    getUrl('2007-10-22')
    getUrl('2007-10-15')
    getUrl('2007-10-08')
    getUrl('2007-10-01')
    getUrl('2007-09-24')
    getUrl('2007-09-17')
    getUrl('2007-09-10')
    getUrl('2007-09-03')
    getUrl('2007-08-27')
    getUrl('2007-08-20')
    getUrl('2007-08-13')
    getUrl('2007-08-06')
    getUrl('2007-07-30')
    getUrl('2007-07-23')
    getUrl('2007-07-16')
    getUrl('2007-07-09')
    getUrl('2007-07-02')
    getUrl('2007-06-25')
    getUrl('2007-06-18')
    getUrl('2007-06-11')
    getUrl('2007-06-04')
    getUrl('2007-05-28')
    getUrl('2007-05-21')
    getUrl('2007-05-14')
    getUrl('2007-05-07')
    getUrl('2007-04-30')
    getUrl('2007-04-23')
    getUrl('2007-04-16')
    getUrl('2007-04-09')
    getUrl('2007-04-02')
    getUrl('2007-03-26')
    getUrl('2007-03-19')
    getUrl('2007-03-12')
    getUrl('2007-03-05')
    getUrl('2007-02-26')
    getUrl('2007-02-19')
    getUrl('2007-02-12')







#!/usr/bin/python
# coding: utf-8
import os
import sys
import requests
import re
import urllib

def getUrl(name):
	r = requests.get("http://www.songtaste.com/music/catsong/%s" % name)
	name = name.replace('/', '_')
	print name
	if os.path.isdir("%s" % name):
		print 'The path is exist !'
	else: 
		os.mkdir("%s" % name)
		print 'creat over'
	# print r.text
	reg = r'<td class="singer"><a href="/song/(.+?.)/">'
	gre = re.compile(reg)
	number = re.findall(gre,r.text)
	x = 0
	for dd in number:
		url = 'http://www.songtaste.com/song/'
		url += dd
		songurl = requests.get(url)
		reg = r'var strURL = \"(.+?.)\"'
		gre = re.compile(reg)
		number = re.findall(gre,songurl.text)
		if number:
			x+=1
			print x
			print name + '%d' % x
			finalUrl = 'http://www.songtaste.com/time.php?str='
			finalUrl += number[0]
			finalUrl += '&sid='
			finalUrl += dd
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
	for x in xrange(1,100):
#		if x<=38: 
#		    continue
		getUrl('cat15/%d' % x)







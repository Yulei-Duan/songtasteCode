#!/usr/bin/python
# coding: utf-8
import os
import json
import sys
import requests
import re
import urllib

  # <td class="singer"><a href="/song/1587079/">木偶的死亡舞步 - 钢琴曲</a> </td>

def getUrl():
	r = requests.get("http://www.songtaste.com/music/catsong/cat9/2")
	# print r.text
	reg = r'<td class="singer"><a href="/song/(.+?.)/">'
	gre = re.compile(reg)
	number = re.findall(gre,r.text)
	sum = ''
	for dd in number:
		sum += dd
		sum = sum + ','
	sum = sum[:-1]
	url = 'http://www.songtaste.com/playmusic.php?song_id='
	url = url + sum

	playerUrl = requests.get(url)
	# print playerUrl.text

	reg = r'(http://.+?.mp3|http://.+?.wma)'
	gre = re.compile(reg)
	mp3URL = re.findall(gre,playerUrl.text)
	x = 50
	for dd in mp3URL:
		print dd
		urllib.urlretrieve(dd, '%s.mp3' %x)
		# urllib.urlretrieve(dd)
		x+=1







if __name__ == "__main__":
	getUrl()





'''
	This script extracts text from .memo files created by the default
	Memo app on Samsung (and possibly other) phones. No root access
	required. Share a memo via Bluetooth to your PC and run this script
	against the file.

	Version 0.2 Updated on: 9 May 2016 Domenic Brosh 

	This program is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

	WARNING: This script relies on Python's XML Processing Modules and
	is therefore not secure against maliciously constructed data. ONLY
	USE THIS SCRIPT TO PARSE MEMOS THAT YOU HAVE CREATED ON YOUR OWN
	DEVICE. For more information see:
	https://docs.python.org/2/library/xml.html#xml-vulnerabilities
	https://docs.python.org/3/library/xml.html
'''
import re, sys, os, zipfile, time, xml.etree.ElementTree as eltree

def memoContent(memoFile):
	archive = zipfile.ZipFile(memoFile, 'r')
	return archive.open('memo_content.xml')

def parseMemo(memoFile):

	inputFile = memoContent(memoFile)
	tree = eltree.parse(inputFile)
	root = tree.getroot()

	titleElement = root.find('.//meta[@title]')
	memoTitle = titleElement.attrib.get('title')

	timeElement = root.find('.//meta[@createdTime]')
	timeStamp = timeElement.attrib.get('createdTime')
	memoTime = time.strftime('%x %X', time.localtime(float(timeStamp)/1000))

	contentElement = (root[1][0].text)
	parsedList = (re.split('</p>|<p value="memo2" >', contentElement))
	# <p> tags mark new lines. Remove them from the output
	parsedList = [symbol.replace('<p>', '') for symbol in parsedList]
	parsedList = [symbol.replace('&nbsp;', ' ') for symbol in parsedList]

	print ('Title: ' + memoTitle)
	print ('Created: ' + memoTime)

	for element in parsedList:
		print(element)

if len(sys.argv) < 2:
	scriptName = ("".join(sys.argv[0].rsplit("/", 1)[-1:]))

	# This script requires an input directory and optional file
	print ("USEAGE: python %s /path/to/somedirectory[/file.memo]") % scriptName

else:
	if sys.argv[1].endswith(".memo"):
		parseMemo(sys.argv[1])
	else:
		for memoFiles in os.listdir(sys.argv[1]):
		    if memoFiles.endswith('.memo'):
		    	parseMemo(sys.argv[1] + "/" + memoFiles)
		    	print('########## END OF MEMO ##########')

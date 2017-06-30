import json
import re

mainFile = "data-gen/tweets.txt"

def cleanText(str):
	containsUnicode = False

	try:
		# remove unicode
		line = str.decode('unicode_escape')
	except:
		line = str.encode('utf-8')
		line = line.decode('unicode_escape').encode('ascii', 'ignore')
		containsUnicode = True

	line = line.strip()
	return (line, containsUnicode)

def parseTweets(fileName):
	linesWithUnicode = 0

	ft1File = "ft1.txt"
	outFile = open(ft1File, "wb")

	with open(fileName) as f:
	    for line in f:
	    	parsed_json = json.loads(line)
	    	if 'created_at' in parsed_json and 'text' in parsed_json:
	    		timeStamp = parsed_json['created_at']
	    		cleanedText = cleanText(parsed_json['text'])
	    		text = cleanedText[0]
	    		if cleanedText[-1]: linesWithUnicode += 1

	    		finalLine = "{} (timestamp: {})\n".format(text, timeStamp)
	    		outFile.write(finalLine)

	numUnicodeLines = "\n{} tweets contained unicode.".format(linesWithUnicode)
	outFile.write(numUnicodeLines)
	outFile.close()

parseTweets(mainFile)

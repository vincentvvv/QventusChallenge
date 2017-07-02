#!/usr/bin/env python
import sys
import json

tweetFile  = sys.argv[1]

# Given a string, check if it has unicode
# Remove all unicode and escape characters
# return a tuple(str, bool)
#	str  - cleaned line
# 	bool - TRUE if it contains Unicode	
def cleanText(str):
	containsUnicode = False
	# remove unicode
	try:
		line = str.decode('unicode_escape')
	except:
		line = str.encode('utf-8')
		line = line.decode('unicode_escape').encode('ascii', 'ignore')
		containsUnicode = True
	# remove escape
	line = line.replace("\n", "")
	line = line.replace("\r", "")
	return (line, containsUnicode)

# Loop through each line in tweets
# cleans up the data and write the cleaned format into the output file
# writes the total number of tweets with unicode
def parseTweets(fileName):
	linesWithUnicode = 0

	outputDir = sys.argv[2]
	outFile = open(outputDir, "wb")

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

parseTweets(tweetFile)
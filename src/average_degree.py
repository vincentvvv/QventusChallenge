#!/usr/bin/env python
import sys
import time
from datetime import datetime

tweetFile = sys.argv[1]

# DegreeGraph
# stores the graph structure, and does the average degree calculations
class DegreeGraph(object):
	def __init__(self):
		self.graph = {}
		self.totalNodes = 0
		self.totalEdges = 0
		self.queueOfTweets = []
		self.numOfTweets = 0

	# Takes in a time object and a list of hashtags
	# adds to the queueOfTweets and updates the graph with the new tweet
	def addTweet(self, time, hashtags):
		self.queueOfTweets.append((time, hashtags))
		self.numOfTweets += 1
		self.updateGraph(time, hashtags)

	# Takes a list of hashtags and adds edges and nodes to the graph
	def addHashtags(self, hashtags):
		if len(hashtags) > 1:
			for tag1 in hashtags:
				for tag2 in hashtags:
					if tag1 != tag2:
						if tag1 in self.graph:
							if tag2 not in self.graph[tag1]: 
								self.graph[tag1].append(tag2)
								self.totalEdges += 1
						else:
							# new node
							self.totalNodes += 1
							self.graph[tag1] = [tag2]
							# add a edge
							self.totalEdges += 1

	# remove all tweets that are not in the 60 sec time fame of the given time
	def evictTweets(self, timeData):
		while self.numOfTweets > 1:
			oldestTweet = self.queueOfTweets[0]
			timeDiff = (timeData - oldestTweet[0]).total_seconds()
			# not in time 60 sec frame
			if timeDiff > 60:
			# remove the tweet and remove the nodes and edges
				tags = oldestTweet[-1]
				# remove edges
				for tag1 in tags:
					if tag1 in self.graph:
						for tag2 in tags:
							# delete edge
							if tag2 in self.graph[tag1]:
								self.graph[tag1].remove(tag2)
								self.totalEdges -= 1
						# delete node
						if len(self.graph[tag1]) == 0:
							self.graph.pop(tag1, None)
							self.totalNodes -= 1

				self.numOfTweets -= 1
				self.queueOfTweets.pop(0)

			# it is in the range, so we are done
			else: break

	# Update the graph with the given tweet time and hashtags
	def updateGraph(self, timeData, hashtags):
		self.evictTweets(timeData)
		self.addHashtags(hashtags)

	def getAvgDegree(self):
		if self.totalNodes > 0: return self.totalEdges / float(self.totalNodes)
		return 0

# Given a tweet: Str
# return a list of hashtags: [Str]
def getHashTags(line):
	resultTags = []
	for item in line.split():
		# everything that has a # in front
		if item.startswith("#"):
			tags = item.split("#")
			# go through all hashtag
			for tag in tags:
				if tag != "":
					# convert to lowercase
					tag = tag.lower()
					if tag not in resultTags: resultTags.append(tag)

	return resultTags

# Run through the cleaned tweets in file ft1.txt
# Write to file ft2.txt with the average degree for each text
def parseLines(fileName):

	outputDir = sys.argv[2]
	outFile = open(outputDir, "wb")

	degreeGraph = DegreeGraph()
	with open(fileName) as f:
	    for line in f:
	    	if line == '\n': break
	    	# get timestamp
	    	timestamp = [p.split(')')[0] for p in line.split('(') if ')' in p][-1]
	    	timestamp = timestamp[11::]
	    	timeString = time.strptime(timestamp, '%a %b %d %H:%M:%S +0000 %Y')
        	timeDate = datetime.fromtimestamp(time.mktime(timeString))
        	# get hashes
        	hashtags = getHashTags(line)
        	# add tweet with hashtags to queue
        	degreeGraph.addTweet(timeDate, hashtags)
        	avgDegree = degreeGraph.getAvgDegree()
        	# write to file
        	outFile.write("%.2f\n" % avgDegree)

        outFile.close()

parseLines(tweetFile)
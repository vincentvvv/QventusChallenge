#!/bin/bash
/usr/bin/python src/tweets_cleaned.py tweet_input/tweets.txt tweet_output/ft1.txt
/usr/bin/python src/average_degree.py tweet_output/ft1.txt tweet_output/ft2.txt
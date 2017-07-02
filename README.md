# [Qventus Challenge](https://github.com/yuguang/coding-challenge)
---
### Submission by: Vincent Vuong
### File Structure:
```
├── README.md  
├── run.sh  
├── src  
│   ├── average_degree.py  
│   └── tweets_cleaned.py  
├── tweet_input  
│   └── tweets.txt  
└── tweet_output  
    ├── ft1.txt  
    └── ft2.txt  
```
### Extra Imports
---
- `import json` for parsing json
- `import time` for parsing the timestamp
- `from datetime import datetime` for calculating the time difference between 2 timestamps

### Instructions
---
- Run the `run.sh` script with `./run.sh` (may need to run `chmod +x run.sh`)
- Results will appear in `tweet_output` directory
- `ft1.txt` is part 1, cleaned tweets
- `ft2.txt` is part 2, average degree calculations for the tweets

### To Run Each Script Individually
----
| Arguments   | Description |
| ----------- | ----------- |
| `input file`   | The location of the input file. |
| `output file`  | The location of the output file. |

- Part 1: `python tweets_cleaned.py <input file> <output file>`
- Part 2: `python average_degree.py <input file> <output file>`
##### Example 
`python src/tweets_cleaned.py tweet_input/tweets.txt tweet_output/ft1.txt`

### Strategy
---
##### Part 1
- Go through all the tweets in `tweet_input/tweets.txt`
- parse the json for `text` and `created_at`
- clean the unicode and remove `\n` and `\r`
- for each tweet with a unicode, increment the counter
- write the cleaned tweet with timestamp in format `tweet (timestamp)\n` into file `tweet_output/ft1.txt`
- at the end write `X tweets contained unicode.`, where `X` is the number of tweets that contains unicode
---
##### Part 2
- Use the file `tweet_output/ft1.txt` created from part 1 to calculate the average degree
- Go through each tweet, and parse the hashtags and the timestamp
- insert into the `DegreeGraph` Class, which handles the insertion of hashtags, evicting hashtags that are not in the 60 second window, and also does the average degree calculations for each tweet added
- write the average degree for each tweet to the file `tweet_output/ft2.txt`
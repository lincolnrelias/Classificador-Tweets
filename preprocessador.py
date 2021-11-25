import re
file = open("saData.csv","r",encoding="utf8")
dataset = list()
for line in file:
    lineSplit = line.split(",")
    tweetContentClean = re.sub(r'http\S+', '', lineSplit[3].lower())
    tweetContentClean = re.sub('\W+',' ', tweetContentClean)
    lineRefactored = lineSplit[1]+","+tweetContentClean
    dataset.append(lineRefactored)
dataset.pop(0)
open("saDataProcessed.csv","w").writelines([x+"\n" for x in dataset])
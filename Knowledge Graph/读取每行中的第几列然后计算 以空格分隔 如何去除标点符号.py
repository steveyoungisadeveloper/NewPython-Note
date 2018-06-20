# coding: UTF-8

#Python read 和 write 这里有写 http://www.cnblogs.com/feeland/p/4477535.html
#string 里有 digits whitesapce punctuation 单独区分出来 这里边就是 利用了punctuation去split掉<>符号的
#用for word in wordList 不会改变 list里边的值 要用这种方法
import string

strip = string.punctuation
wordList = []

amieData = open("amieData.txt", "r")
scaleKBData = open("scaleKBData.csv", "w")
lines = amieData.readlines()

#以行的形式读取全部内容
for line in lines:
    wordList = line.split()
#用for word in wordList 不会改变 list里边的值 要用这种方法
    for i in range(len(wordList)):
        wordList[i] = wordList[i].strip(strip)

    subject = wordList[0]
    predicate = wordList[1]
    object = wordList[2]
    newEntry = predicate + " " + subject + " " + object

    scaleKBData.writelines(newEntry + "\n")

amieData.close()
scaleKBData.close()

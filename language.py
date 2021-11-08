"""
Language Modeling Project
Name:
Roll No:
"""

import language_tests as test

project = "Language" # don't edit this

### WEEK 1 ###

'''
loadBook(filename)
#1 [Check6-1]
Parameters: str
Returns: 2D list of strs
'''
def loadBook(filename):
    f=open(filename)
    book=[]
    x=f.read().splitlines()
    for each in x:
        if len(each)>0:
            eachword=each.split()
            book.append(eachword)
    #print(book)
    return book


'''
getCorpusLength(corpus)
#2 [Check6-1]
Parameters: 2D list of strs
Returns: int
'''
def getCorpusLength(corpus):
    length=0
    for row in corpus:
        for col in row:
            length=length+1
    #print(length)
    return length


'''
buildVocabulary(corpus)
#3 [Check6-1]
Parameters: 2D list of strs
Returns: list of strs
'''
def buildVocabulary(corpus):
    newlist=[]
    for row in corpus:
        for col in row:
            if col not in newlist:
                newlist.append(col)
    #print(newlist)
    return newlist


'''
countUnigrams(corpus)
#4 [Check6-1]
Parameters: 2D list of strs
Returns: dict mapping strs to ints
'''
def countUnigrams(corpus):
    dictionary={}
    for row in corpus:
        for col in row:
            if col not in dictionary:
                dictionary[col]=1
            else:
                dictionary[col]+=1
    #print(dictionary)
    return dictionary


'''
getStartWords(corpus)
#5 [Check6-1]
Parameters: 2D list of strs
Returns: list of strs
'''
def getStartWords(corpus):
    list=[]
    for i in corpus:
        if i[0] not in list:
            list.append(i[0])
    #print(list)
    return list


'''
countStartWords(corpus)
#5 [Check6-1]
Parameters: 2D list of strs
Returns: dict mapping strs to ints
'''
def countStartWords(corpus):
    dictionary={}
    for i in corpus:
        if i[0] not in dictionary:
            dictionary[i[0]]=1
        else:
            dictionary[i[0]]+=1
    #print(dictionary)
    return dictionary


'''
countBigrams(corpus)
#6 [Check6-1]
Parameters: 2D list of strs
Returns: dict mapping strs to (dicts mapping strs to ints)
'''
def countBigrams(corpus):
    dictionary={}
    for row in corpus:
        for col in range(len(row)-1):
            if row[col] not in dictionary:
                dictionary[row[col]]={}
            if row[col+1] in dictionary[row[col]]:
                dictionary[row[col]][row[col+1]]+=1
            else:
                dictionary[row[col]][row[col+1]]=1
    return dictionary


### WEEK 2 ###

'''
buildUniformProbs(unigrams)
#1 [Check6-2]
Parameters: list of strs
Returns: list of floats
'''
def buildUniformProbs(unigrams):
    uniformprob=[]
    for eachword in unigrams:
        prob=1/len(unigrams)
        uniformprob.append(prob)
    #print(uniformprob)
    return uniformprob


'''
buildUnigramProbs(unigrams, unigramCounts, totalCount)
#2 [Check6-2]
Parameters: list of strs ; dict mapping strs to ints ; int
Returns: list of floats
'''
def buildUnigramProbs(unigrams, unigramCounts, totalCount):
    unigram_prob=[]
    for i in unigrams:
        countofword=unigramCounts[i]
        prob=countofword/totalCount
        #print(totalCount)
        unigram_prob.append(prob)
    return unigram_prob


'''
buildBigramProbs(unigramCounts, bigramCounts)
#3 [Check6-2]
Parameters: dict mapping strs to ints ; dict mapping strs to (dicts mapping strs to ints)
Returns: dict mapping strs to (dicts mapping strs to (lists of values))
'''
def buildBigramProbs(unigramCounts, bigramCounts):
    dictionary={}
    for prevWord in bigramCounts:
        words=[]
        probsoflist=[]
        for keys,values in bigramCounts[prevWord].items():
            #print(bigramCounts)
            words.append(keys)
            probsoflist.append(values/unigramCounts[prevWord])
            tempdict={}
            tempdict["words"]=words
            #print(words)
            #print(tempdict)
            tempdict["probs"]=probsoflist
        dictionary[prevWord]=tempdict
        #print(dictionary)
    return dictionary


'''
getTopWords(count, words, probs, ignoreList)
#4 [Check6-2]
Parameters: int ; list of strs ; list of floats ; list of strs
Returns: dict mapping strs to floats
'''
def getTopWords(count, words, probs, ignoreList):
    highwordProb= { }
    Top_words = { }
    for i in range(len(words)):
        if words[i] not in ignoreList:
           highwordProb[words[i]] = probs[i]
    sorted_list = sorted(highwordProb, key=highwordProb.get, reverse=True)
    for sort_words in sorted_list:
        if len(Top_words)<count:
           Top_words[sort_words]= highwordProb[sort_words]
    return Top_words





'''
generateTextFromUnigrams(count, words, probs)
#5 [Check6-2]
Parameters: int ; list of strs ; list of floats
Returns: str
'''
from random import choices
def generateTextFromUnigrams(count, words, probs):
    sentence=""
    for i in range(count):
        #print(count)
        randomList = choices(words,weights=probs)
        #print("The random list is  :  ", randomList)
        sentence= sentence + randomList[0]+" "
    #print("sen is :::::",len(sentence))
    #print(sentence)
    return sentence


'''
generateTextFromBigrams(count, startWords, startWordProbs, bigramProbs)
#6 [Check6-2]
Parameters: int ; list of strs ; list of floats ; dict mapping strs to (dicts mapping strs to (lists of values))
Returns: str
'''
def generateTextFromBigrams(count, startWords, startWordProbs, bigramProbs):
    sentence=""
    z= choices(startWords,weights=startWordProbs)[0]
    sentence = sentence + z
    for i in range(count-1):
        if (z!="."):
                x=bigramProbs[z]['words']
                y=bigramProbs[z]['probs']
                z = choices(x,weights=y)[0]  
                sentence+=" " +z
                #print("random choices    :::: ",z)
                #print("sentence ::::::::::::", sentence)
        else:
            z= choices(startWords,weights=startWordProbs)[0]
            sentence = sentence + " " + z
            #print("sentence  ::::::::::::" sentence)
    return sentence



### WEEK 3 ###

ignore = [ ",", ".", "?", "'", '"', "-", "!", ":", ";", "by", "around", "over",
           "a", "on", "be", "in", "the", "is", "on", "and", "to", "of", "it",
           "as", "an", "but", "at", "if", "so", "was", "were", "for", "this",
           "that", "onto", "from", "not", "into" ]

'''
graphTop50Words(corpus)
#3 [Hw6]
Parameters: 2D list of strs
Returns: None
'''
def graphTop50Words(corpus):
    words = buildVocabulary(corpus)
    count = getCorpusLength(corpus)
    unigramcount = countUnigrams(corpus)
    unigramprobs = buildUnigramProbs(words, unigramcount, totalCount=count)
    topwords = getTopWords(50,words,unigramprobs,ignore)
    plot = barPlot(topwords, "Top 50 Words")
    return plot
    


'''
graphTopStartWords(corpus)
#4 [Hw6]
Parameters: 2D list of strs
Returns: None
'''
def graphTopStartWords(corpus):
    startwords=getStartWords(corpus)
    startwordcounts=countStartWords(corpus)

    startWordProbs=buildUnigramProbs(startwords,startwordcounts,len(corpus))
    count=getTopWords(50,startwords,startWordProbs,ignore)
    plot=barPlot(count,"Top state words")
    return plot
 


'''
graphTopNextWords(corpus, word)
#5 [Hw6]
Parameters: 2D list of strs ; str
Returns: None
'''
def graphTopNextWords(corpus, word):
    return


'''
setupChartData(corpus1, corpus2, topWordCount)
#6 [Hw6]
Parameters: 2D list of strs ; 2D list of strs ; int
Returns: dict mapping strs to (lists of values)
'''
def setupChartData(corpus1, corpus2, topWordCount):
    return


'''
graphTopWordsSideBySide(corpus1, name1, corpus2, name2, numWords, title)
#6 [Hw6]
Parameters: 2D list of strs ; str ; 2D list of strs ; str ; int ; str
Returns: None
'''
def graphTopWordsSideBySide(corpus1, name1, corpus2, name2, numWords, title):
    return


'''
graphTopWordsInScatterplot(corpus1, corpus2, numWords, title)
#6 [Hw6]
Parameters: 2D list of strs ; 2D list of strs ; int ; str
Returns: None
'''
def graphTopWordsInScatterplot(corpus1, corpus2, numWords, title):
    return


### WEEK 3 PROVIDED CODE ###

"""
Expects a dictionary of words as keys with probabilities as values, and a title
Plots the words on the x axis, probabilities as the y axis and puts a title on top.
"""
def barPlot(dict, title):
    import matplotlib.pyplot as plt

    names = []
    values = []
    for k in dict:
        names.append(k)
        values.append(dict[k])

    plt.bar(names, values)

    plt.xticks(rotation='vertical')
    plt.title(title)

    plt.show()

"""
Expects 3 lists - one of x values, and two of values such that the index of a name
corresponds to a value at the same index in both lists. Category1 and Category2
are the labels for the different colors in the graph. For example, you may use
it to graph two categories of probabilities side by side to look at the differences.
"""
def sideBySideBarPlots(xValues, values1, values2, category1, category2, title):
    import matplotlib.pyplot as plt

    w = 0.35  # the width of the bars

    plt.bar(xValues, values1, width=-w, align='edge', label=category1)
    plt.bar(xValues, values2, width= w, align='edge', label=category2)

    plt.xticks(rotation="vertical")
    plt.legend()
    plt.title(title)

    plt.show()

"""
Expects two lists of probabilities and a list of labels (words) all the same length
and plots the probabilities of x and y, labels each point, and puts a title on top.
Note that this limits the graph to go from 0x0 to 0.02 x 0.02.
"""
def scatterPlot(xs, ys, labels, title):
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()

    plt.scatter(xs, ys)

    # make labels for the points
    for i in range(len(labels)):
        plt.annotate(labels[i], # this is the text
                    (xs[i], ys[i]), # this is the point to label
                    textcoords="offset points", # how to position the text
                    xytext=(0, 10), # distance from text to points (x,y)
                    ha='center') # horizontal alignment can be left, right or center

    plt.title(title)
    plt.xlim(0, 0.02)
    plt.ylim(0, 0.02)

    # a bit of advanced code to draw a y=x line
    ax.plot([0, 1], [0, 1], color='black', transform=ax.transAxes)

    plt.show()


### RUN CODE ###

# This code runs the test cases to check your work
if __name__ == "__main__":
    # print("\n" + "#"*15 + " WEEK 1 TESTS " +  "#" * 16 + "\n")
    # test.week1Tests()
    # print("\n" + "#"*15 + " WEEK 1 OUTPUT " + "#" * 15 + "\n")
    # test.runWeek1()
    #test.testLoadBook()
    #test.testGetCorpusLength()
    #test.testBuildVocabulary()
    #test.testCountUnigrams()
    #test.testGetStartWords()
    #test. testCountStartWords()
    #test.testCountBigrams()
    #test.testBuildUniformProbs()

    ## Uncomment these for Week 2 ##

    #print("\n" + "#"*15 + " WEEK 2 TESTS " +  "#" * 16 + "\n")
    #test.week2Tests()
    #print("\n" + "#"*15 + " WEEK 2 OUTPUT " + "#" * 15 + "\n")
    #test.runWeek2()
    #test.testBuildUnigramProbs()
    #test.testBuildBigramProbs()
    #test.testGetTopWords()
    #test.testGenerateTextFromUnigrams()
    #test.testGenerateTextFromBigrams()


    ## Uncomment these for Week 3 ##

    print("\n" + "#"*15 + " WEEK 3 OUTPUT " + "#" * 15 + "\n")
    test.runWeek3()

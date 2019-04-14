from collections import OrderedDict
mapDict = OrderedDict()			# declaring an empty ordered dictionary to store words as key and its value as a the sum


def arangeSortedSentence():  # function to arange the sentence in ordered format
    aValNS = mapDict.values()  # creating array of sums as per the order of sentence
    aValS = mapDict.values()
    aValS.sort()  # sorted array to make new sentence
    print "converted Sum: ", aValNS
    sortedSent = ""  # empty string to concate the words
    for i in aValS:  # loop that runs on sorted array and finds the key from the dictionary to make the output sentence
        index = aValNS.index(i)
        sortedSent += str([k for k, v in mapDict.iteritems() if v == i][0])  # scans the dictionary and returns all the words in a list hence using '[0]' to get the first occurence
        sortedSent += " "
        mapDict[mapDict.keys()[index]] = -1  # updating the sum in dictionary to -1 as it is alrealy used and will not be required again.

    print sortedSent


def WordToSum(word):		# function to convert words to sum and storing it in a dictionary
    aWord = list(word)
    aValue = map(lambda x: ord(x) - 96, aWord)
    #mapDict[word] = sum(aValue)
    mapDict[word] = sum(aValue)


def main():
    #sentence = "a cat runs faster than the tortoise"
    sentence = "dot the enemy is rooting for a ball"
    print sentence
    sentence = sentence.split(" ")
    for i in sentence:
        WordToSum(i)


main()
print mapDict
arangeSortedSentence()
print mapDict

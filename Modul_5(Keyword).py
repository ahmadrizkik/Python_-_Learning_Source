paragraph = open('test3.txt', 'r')
parReader = paragraph.read()
def word_search(data, keyword):
    kwCount = 0
    dataBeingSplit = data.split()
    allWord = []
    for wordToList in dataBeingSplit:
        allWord.append(wordToList.rstrip('.,?()\"\'').lower())
        if keyword.lower() in allWord:
            kwCount = kwCount + 1
            return kwCount
print (word_search(parReader, 'and'))
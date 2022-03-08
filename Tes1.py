exampleText = 'to. Test back. in, back for\' the test in back.'

splitToWord = exampleText.split()
normalizedWord = []
for x in splitToWord:
    normalizedWord.append(x.rstrip('.,\'').lower())
print (normalizedWord)
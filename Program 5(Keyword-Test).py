# Check Keyword

exampleText = 'to. Test back. in, back. for\' the test in back.'
keywordText = 'back'

def keywordCounter(doc, keyword):
    print ('isi teksnya\n'+'"'+doc+'"')
    print ('keywordnya = '+keywordText)

    totalKeywoard = 0

    splittoword = doc.rstrip('.,?()\"\'').lower()

    if keyword in splittoword:
        print (True)

    print ('total keyword = ', totalKeywoard)

keywordCounter(exampleText, keywordText)
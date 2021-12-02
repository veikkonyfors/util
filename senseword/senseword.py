class SenseWord():
    '''
    VN/ViWare 20211201
    
    SenseWord, class to sense differences in two given words.
    
    Entails command line interface
    Usage: senseword word1 word2
    :param word1: First word to compare
    :type word1: string  
    :param word2: Second word to compare
    :type word2: string
    
    :remarks: Handy e.g. with comparing rsa256 hashes
    '''

    def sense(self,word1,word2):
        return(word1==word2)

import sys, getopt
from senseword import SenseWord

def main(argv):
    '''
    VN/ViWare 20211201
    
    senseword, command to sense differences in two given words.
    
    Usage: senseword [-h] | word1 word2
    
    :option h: print out Usage
    :param word1: First word to compare
    :type word1: string  
    :param word2: Second word to compare
    :type word2: string
    
    :returns: 0 if words are the same, nonzero otherwise
    
    :remarks: Handy e.g. with comparing rsa256 hashes
    '''
    try:
        opts, args = getopt.getopt(argv,"h")
    except getopt.GetoptError:
        print(usage(argv))
        sys.exit(2)
    
    if len(opts)==0 and len(args)==0: print(usage(argv)); sys.exit(1)
    
    for opt, arg in opts:
        if opt == '-h':
           print(usage(argv))
           if (len(args)==0 and len(opts)==1): sys.exit(0)
           else: sys.exit(1)
        else:
            if(len(args)!=2):
                print(usage(argv)); sys.exit(1)

    sense_word=SenseWord()
    print(sense_word.sense(argv[0],argv[1]))
    print("same" if sense_word.sense(argv[0],argv[1]) else "different")
    sys.exit(not sense_word.sense(argv[0],argv[1]))

def usage(argv):
    return 'Usage: senseword.py -h | word1 word2\nWas senseword.py '+' '.join([str(arg) for arg in argv])


if __name__ == "__main__":
    main(sys.argv[1:])
   

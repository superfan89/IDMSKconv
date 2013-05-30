import os,re,sys
import decomposeTDAs
def printInfo():
    print '*'*30
    print 'IDM Sk Data Extractor'
    print 'Built data:Dec 6,2009'
    print 'Author    :Superfan'
    print 'Intro     :This script will extract original data from dictionaries built with IDM Sk'
    print '           Tested with LDOCE5 and OALD7'
    print 'Usage     :\'python IDMSKconv.py [output path] [dictionary path]\''
    print 'Example   :\'python IDMSKconv.py C:\\Output C:\\Dict\''
    print '           If no path is specified,it will be defaulted to the current path.'
    print '*'*30
if __name__=='__main__':
    #check if options are valid
    opt = sys.argv[1:]
    printInfo()
    if len(opt)>=1:
        if not os.path.isabs(opt[0]):
            print '\''+opt[0]+'\''+' is not a valid directory name!'
            sys.exit()
        else:outDir=re.match(r'(.*?)\\*$',opt[0]).group(1)
    else:outDir=os.getcwd()
    if len(opt)>=2:
        if not os.path.exists(opt[1]):
            print '\''+opt[1]+'\''+' doesn\'t exsists!'
            sys.exit()
        else:dictDir=re.match(r'(.*?)\\*$',opt[1]).group(1)
    else:dictDir=os.getcwd()
    print 'Dictionary dir:',dictDir
    print 'Output     dir:',outDir
    print 'Type any key to begin...'
    raw_input()
    #begin to parse dictionary data
    for root,dirs,files in os.walk(dictDir):
        if('CONTENT.tda'.lower() in [file.lower() for file in files]):
            currentOutdir=outDir+re.match(dictDir.replace('\\','\\\\')+r'(.*)',root).group(1)
            print 'Find target files in:'+'\"'+root+'\"'
            print 'Current output path:'+currentOutdir
            if not os.path.exists(currentOutdir):
                os.makedirs(currentOutdir)
            decps=decomposeTDAs.decompose(root,currentOutdir)
            decps.inflateTDA()
            decps.writeFiles()
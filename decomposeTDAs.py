import zlib,struct,re
typeIndex={'ULONG':4,
	   'U24':3,
	   'USHORT':2,
	   'UBYTE':1,
	   'LINK':0,
	   'DATA':0}
class decompose:
    def parseFormat(self):
	select=0
        fconfig=open(self.dir+'\\config.cft','rb')
	for line in fconfig:
	    result = re.match(r'\$(\S+)\s*=\s*(\S+)',line)
	    if result:
		if result.group(1)=='CONTENT,OFFSET':
                    self.formatStr[1]=typeIndex[result.group(2)]
                    select=2
		else:
		    self.formatStr[select]+=typeIndex[result.group(2)]
    def writeOffsetIndex(self):
	self.offsets=[]
	i=0
	fdata=open(self.dir+'\\files.dat','rb')
	while True:
	    i+=1
	    if(len(fdata.read(self.formatStr[0]))==0):break
	    self.offsets.append(struct.unpack('L',str(fdata.read(self.formatStr[1])+(4-self.formatStr[1])*'\x00'))[0])
	    fdata.read(self.formatStr[2])
    def inflateTDA(self):
        fin=open(self.dir+'\\CONTENT.tda', 'rb')
        fdst=open(self.outdir+'\\output', 'wb')
        findex=open(self.dir+'\\CONTENT.tda.tdz','rb')
        byte=[]
        while True:
            bin=findex.read(8)
            if len(bin)==0:break
            byte.append(struct.unpack('ii',str(bin)))
        i=0
        print 'Now decompressing...'
        for xi,bytei in byte:
            i+=1
            dedata=zlib.decompress(fin.read(bytei))
            fdst.write(dedata) 
        print 'Done!Total %d entries.' %i
    def writeFiles(self):
        fin=open(self.dir+'\\NAME.tda','rb')
        raw=fin.read()
        name=raw.split('\x00')
        import os
        fin=open(self.outdir+'\\output','rb')
        for i in range(len(self.offsets)):
            fout=open(self.outdir+'\\'+name[i],'wb')
            if(i==len(self.offsets)-1):
                fout.write(fin.read()[:-1])
            else:
                fout.write(fin.read(self.offsets[i+1]-self.offsets[i])[:-1])
            print 'Now writing separate files:'+str(i+1)+'\r',
        print '\nDone!'
    def __init__(self,dir,outdir):
	self.dir=dir
        self.outdir=outdir
	self.formatStr=[0,0,0]
	self.parseFormat()
        self.writeOffsetIndex()
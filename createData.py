
foos=set()

for line in open("oxymoronlist.txt"):
    words=line.split()
    words=[word.lower() for word in words]
    fooString=" ".join(words)
    foos.add(fooString)

print len(foos)

outFile1=open("foo_1.txt","w")
outFile2=open("foo_2.txt","w")
outFileMulti=open("fooMulti.txt","w")

for foo in foos:
    words=foo.split()
    if len(words)==1:
        outFile1.write(foo+"\n")
    if len(words)==2:
        outFile2.write(foo+"\n")
    else:
        outFileMulti.write(foo+"\n")

outFile1.close()
outFile2.close()
outFileMulti.close()

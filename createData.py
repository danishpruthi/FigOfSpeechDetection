
oxymorons=set()

for line in open("oxymoronlist.txt"):
    words=line.split()
    words=[word.lower() for word in words]
    oxymoronString=" ".join(words)
    oxymorons.add(oxymoronString)

print len(oxymorons)

outFile1=open("oxy_1.txt","w")
outFile2=open("oxy_2.txt","w")
outFileMulti=open("oxyMulti.txt","w")

for oxymoron in oxymorons:
    words=oxymoron.split()
    if len(words)==1:
        outFile1.write(oxymoron+"\n")
    if len(words)==2:
        outFile2.write(oxymoron+"\n")
    else:
        outFileMulti.write(oxymoron+"\n")

outFile1.close()
outFile2.close()
outFileMulti.close()

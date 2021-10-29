import sys
def qcreat(item):
    query=""
    for i in range(1,len(item)-1):
        query+="INSERT INTO "+ sys.argv[3]+"("+(',').join(item[0])+") VALUES (\'"+'\',\''.join(item[i])+"\');\n"
    print(query)
    return query
    
f=open(sys.argv[1],"r",encoding='utf-8')
lines=f.readlines()
f.close()
i=0
item=""
separ=list()
for line in lines:

    item=line.split('\t')
    if '\n' in item[len(item)-1]:
        item[len(item)-1]=item[len(item)-1].replace('\n',"")
    # print(item)
    separ.append(item)
    i+=1
print(qcreat(separ))

fout=open(sys.argv[2],"w",encoding='utf-8')
fout.write(qcreat(separ))
fout.close()
fhand=open('mbox-short.txt')
counts=dict()
timelist=list()
for line in fhand:
    line=line.rstrip()
    if not line.startswith('From') or line.startswith('From:'):
        continue
    
    words=line.split()
    time=words[5]
    Hrs=time[0:2]
    timelist.append(Hrs)


for hr in timelist:
    counts[hr]=counts.get(hr,0)+1




lst=list()

for key,value in counts.items():
    newtup=(key,value)
    lst.append(newtup)
lst=sorted(lst)

for key,value in lst:
    print(key,value)
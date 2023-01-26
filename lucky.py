import sys
count=0
with open(sys.argv[1],'r') as f:
        for line in f:
            for word in line.split():
                if word not in count:
                    count[word]=1
                else:
                    count[word]+=1
print(count)
f.close()

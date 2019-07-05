fname = input("Enter file name: ")
fh = open(fname)
#for lst in fh:
lst = list()
#print(lst)

for line in fh:
    #line = line.rstrip()
    wrds = line.split()
    for word in wrds:
        if word not in lst:
            lst.append(word)
lst.sort()
print(lst)

fname = input("Enter file name: ")


fh = open(fname)
count = 0

for line in fh:
    wrds = line.split()
    #print( "Debug:" , wrds)
    if len(wrds) == 0 : continue
    if wrds[0] != 'From' : continue
    count = count + 1
    print(wrds[1])
print('There were', count, 'lines in the file with From as the first word')

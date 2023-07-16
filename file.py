f=open("d:\\amit.txt","r")
line=''
size=0
while line:
    line=f.readline()
    l=len(line)
    size=size+l
    print(line)
print("Total size of file is :", size)
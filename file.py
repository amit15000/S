f=open("d:\\amit.txt","r")
line=' '
size=0
size_after_strip=0
while line:
    line=f.readline()
    l=len(line)
    size=size+l
    size_after_strip=size_after_strip+len(line.strip())
    print(line)
print("Total size of file is :", size)
print("Total size after removing leading and trailing spaces :", size_after_strip)
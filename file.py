# f=open("d:\\students.txt","w+")
# for i in range(5):
#     name=input("Enter the name of student")
#     f.write(name)
# lines=f.readlines()
# print(lines)
# f.close()

fout=open("d:\\students.txt","w")
list=[]
for i in range(5):
 name=input("enter the name of student")
 list.append(name+'\n')
 
fout.writelines(list)
fout.close()
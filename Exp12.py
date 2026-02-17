print("UIN:251A029")
print("DATE:17-02-26")

file=open("file.txt","r")
content=file.read().split()
print(content)
n=int(input("ENTER THEWRLD LENGTH:"))
for i in content:
    if len(i)==n:
        print(i)
file.close()

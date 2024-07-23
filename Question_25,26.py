'''for i in range(0,128):
    print(chr(i),end=" ")'''

''' i/p-->hello-----world
o/p-->-----hello world
print("-"*30)   #-->hint'''



n=input()
count=0
ans=""
for i in n:
    if(i=="-"):
        count+=1
    else:
        ans=ans+i
print("-"*count+ans)
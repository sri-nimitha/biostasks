a = []*1000
a = input()
b = 0
j = 0
p = 0
for i in range(len(a)):
    if(a[i]=='.'):
        if(a[i+1]=='p'):
            p+=1
        elif(a[i+1]=='b'):
            b+=1
        elif(a[i+1]=='j'):
            j+=1
print(p,b,j)

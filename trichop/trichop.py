a,b,r = list(map(int,input().split()))
n = int(input())
x=[]
i = 0
x = [int(i) for i in input().split()]
count = 0
for i in range(len(x)):
    if(a+b>x[i] and a+x[i]>b and b+x[i]>a):
        count+=1
print(count)
if(count>=r):
    print("Natsu")
else:
    print("Grey")

str1,str2 = str(input()).split()
x = sum(ord(ch) for ch in str1)
y = sum(ord(ch) for ch in str2)
if(x == y):
    print(True)
else:
    print(False)

a = input()
def number(i):
    if i.isdigit():
        if int(i)%2 ==0:
            return True
        else: return False
    else: return True
print (*sorted(a,key = lambda i:(i.isdigit(),number(i),i.isupper(),i)),sep='')

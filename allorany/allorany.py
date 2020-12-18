numbers = input('');
palindrom = 0
positive=0
for a in numbers.split():
  #conditin one
  temp=int(a)
  rev=0
  num=int(a)
  while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
  if(temp == rev):
    palindrom=palindrom+1
  #condit two
  if(int(a)<=0):
      positive=positive+1
      break
if(palindrom>0 and positive==0):
    print(True)
else:
    print(False)

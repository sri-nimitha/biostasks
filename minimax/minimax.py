n = input().strip().split()
for i in range(0, len(n)):
    n[i] = int(n[i])
    
s = sum(n)
print(str(s - max(n)) + " " + str(s - min(n)))
    


    

   

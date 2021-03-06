Coding:
  
x=int(input())
sum=0
y=x
while y>=10:
 sum=0
 while x!=0:
   sum=sum+(x%10)
   x=int(x/10)
 y=sum
 x=sum
print(y)

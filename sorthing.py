n= int(input("Enter number of elements: "))
print("Enter the elements:")
l = []
for i in range(n):
    l.append(int(input()))
for i in range(0,n-1):
    min = i
    for j in range(i+1,n):
      if (l[j]<l[min]):
         min = j
    l[min],l[i] = l[i],l[min]
print (l)  
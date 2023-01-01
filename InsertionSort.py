a=[15,2,3,6,9]
for i in range(len(a)):
    t=a[i]
    j=i-1
    while j>=0 and t<a[j]:
        a[j+1]=a[j]
        j-=1
    a[j+1]=t
print(a)
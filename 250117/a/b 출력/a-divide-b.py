a, b = map(int, input().split())

arr = []

for i in range(20):
    a *= 10
    arr.append(a // b)
    a = (a%b)

print(a//b,end="")
print(".",end="")

if(a//b < 10):
    for i in range(20):
        print(arr[i],end="")
elif(a//b <100):
    for i in range(19):
        print(arr[i],end="")
else:
    for i in range(18):
        print(arr[i],end="")
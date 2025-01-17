a, b = map(int, input().split())

arr = []

for i in range(20):
    a *= 10
    arr.append(a // b)
    a = (a%b)

print("0.",end="")
for i in range(20):
    print(arr[i],end="")
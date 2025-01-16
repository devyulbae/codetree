b, a = int(input().split())

if b%2==1:
    b -= 1

while(b>=a):
    print(b)
    b -= 2
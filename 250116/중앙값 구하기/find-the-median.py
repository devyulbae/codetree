a, b, c = map(int, input().split())

if(a>=b>=c) or (a<=b<=c):
    print(b)
elif(a>=c>=b) or (a<=c<=b):
    print(c)
else:
    print(a) 
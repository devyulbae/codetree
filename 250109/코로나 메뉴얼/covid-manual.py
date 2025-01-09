p = []

for i in range(3):
    p.append(list(input().split()))

count = 0

for i in range(3):
    if int(p[i][1]) >= 37 and p[i][0] == 'Y':
        count += 1
    
if count>=2:
    print("E")
else:
    print("N")
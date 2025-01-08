x_age, x_sex = map(int, input().split())
y_age, y_sex = map(int, input().split())

if(x_age>=19 and x_sex=="M") or (y_age>=19 and y_sex=="M"):
    print(1)
else:
    print(0)
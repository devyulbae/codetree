x_age, x_sex = input().split()
y_age, y_sex = input().split()

print(1) if ((int(x_age)>=19 and x_sex=="M") or (int(y_age)>=19 and y_sex=="M")) else print(0)

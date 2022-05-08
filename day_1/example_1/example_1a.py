from math import sqrt
a = [1.000000,8.00,1]
b = [[0,0.00000,0.000],[1.000,1.0,1],[1,1.00,0.0]]
k = 0
for i in range(len(b)):
    if i+1 < len(b):
        k = k+ a[i]*a[i+1]/sqrt((b[i][0]-b[i+1][0])**2+(b[i][1] -b[i + 1][1])**2+(b[i][2]- b[i + 1][2])**2)
    else:
        k=k+a[i]*a[0]/sqrt((b[i][0]-b[0][0])**2+(b[i][1]- b[0][1])**2 + (b[i][2] -b[0][2])**2)
print(k)

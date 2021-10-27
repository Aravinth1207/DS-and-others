arr = []
C = 6
R = 6
for i in range(6):
    arr.append(list(map(int,input().split())))
sumArray = [] 
for i in range(0, R-2):
    for j in range(0, C-2):
        SUM = (arr[i][j] + arr[i][j + 1] + arr[i][j + 2]) + (arr[i + 1][j + 1]) + (arr[i + 2][j] +  arr[i + 2][j + 1] + arr[i + 2][j + 2])
        sumArray.append(SUM)

print(sumArray)
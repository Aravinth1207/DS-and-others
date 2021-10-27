arr = []

for i in range(6):
    arr.append(list(map(int,input().split())))
MAX = -9999
for i in range(0, 4):
    for j in range(0, 4):
        
        SUM = (arr[i][j] + arr[i][j + 1] + arr[i][j + 2]) + (arr[i + 1][j + 1]) + (arr[i + 2][j] +  arr[i + 2][j + 1] + arr[i + 2][j + 2])
        if MAX <= SUM:
            MAX = SUM

print(MAX)
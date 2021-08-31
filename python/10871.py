
n, x = map(int, input().split())
num_list = list(map(int, input().split()))

for i in range(n):
    if num_list[i] < x:
        print(num_list[i], end=" ")   #출력 사이에 공백을 넣어주기


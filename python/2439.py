n = int(input())

for i in range(1, (n+1)):   # 0부터 시작하는 for문을 1부터 시작
    print(' '*(n-i) + '*'*i)  # 사이를 ,가 아닌 +로 해야 불필요한 공백이 사라짐

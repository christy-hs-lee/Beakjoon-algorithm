num = int(input())
sum = 0
sums = []

for i in range(num):
    a,b = map(int, input().split())
    sum = a + b
    sums.append(sum)   # 값을 리스트에 추가
    
for x in range(num):   # 출력용 반복문
    print('Case #%d:' %(x+1), sums[x])  # 출력 시 사이 공백을 띄우기 위한 방법
num = int(input())
sum = 0
sums = []
a_list = []
b_list = []

for i in range(num):
    a,b = map(int, input().split())
    a_list.append(a)
    b_list.append(b)
    sum = a + b
    sums.append(sum)   # 값을 리스트에 추가
    
for x in range(num):   # 출력용 반복문
    print('Case #%d:' %(x+1), a_list[x], '+', b_list[x], '=', sums[x])  # 출력 시 사이 공백을 띄우기 위한 방법
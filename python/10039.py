sum = 0

for i in range(5):
    score = int(input())
    if score < 40:
        sum = sum + 40
    else:
        sum = sum + score
        
evg = int(sum/5)
print(evg)

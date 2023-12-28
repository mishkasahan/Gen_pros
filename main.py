def prost(n):
    for i in range(n):
        count_dil = 0
        for j in range(1,i):
            if i % j == 0:
                count_dil +=1
        if count_dil == 1:
            yield i


r = prost(150)

for h in r:
    print(h)

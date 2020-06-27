n,k = map(int,input().split())
m = 1
maxl = 0
s = list()
for i in range(n):
    s.append(int(input()))

if 0 in s:
    maxl = n

elif k == 0:
    maxl = 0
else:
    u = 0
    l = 0
    while True:
        m *= s[u]
        if m <= k:
            maxl = max([u-l+1,maxl])#maxを更新
        else:
            while m>k:
                m /= s[l]
                l += 1

        u += 1
        if n == u :
            break
print(maxl)

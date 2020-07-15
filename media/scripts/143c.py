n = int(input())
S = input()
ans = S[0]
count = 1
for i in range(1,n):
    if S[i] != ans[-1]:
        ans += S[i]
        count += 1
print(count)
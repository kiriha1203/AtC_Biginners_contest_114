s = input()
ans = 9999999999
for i in range(len(s) - 2):
    ans = min(ans, abs(int(s[i:i+3])-753))
print(ans)

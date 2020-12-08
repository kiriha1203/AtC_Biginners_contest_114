import itertools

n = input()
length = int(len(n))

nums = ['3', '5', '7', '0']

count = 0
for t in itertools.product(nums, repeat=length):
    nums_str = ''.join(t)
    if ('3' not in nums_str) or ('5' not in nums_str) or ('7' not in nums_str):
        continue
    num_str = str(int(nums_str))
    if '0' in num_str:
        continue
    if int(num_str) <= int(n):
        count += 1
print(count)

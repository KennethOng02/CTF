import string

alpha = "0ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"

flag = []
with open("message.txt") as f:
    nums_str = f.read()
    nums = [int(x) for x in nums_str.split()]
    for num in nums:
        ind = pow(num, -1, 41)
        flag.append(alpha[ind])

print(f'picoCTF{{{"".join(flag)}}}')

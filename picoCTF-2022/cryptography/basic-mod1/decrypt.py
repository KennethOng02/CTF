alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"

flag = []
with open("message.txt") as f:
    num_str = f.read()
    nums = [int(x) for x in num_str.split()]
    for num in nums:
        flag.append(alpha[num % 37])

print(f'picoCTF{{{"".join(flag)}}}')

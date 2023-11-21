import re

# c_obj = re.compile("[a-z]+")
# match_iter = c_obj.finditer("파이th0n")

match_iter = re.finditer("[a-z]+", "파이th0n")

print(match_iter)

for i in match_iter:
    print(i.group())
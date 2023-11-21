import re

# c_obj = re.compile('[a-z]+')
# match_list = c_obj.findall("파이th0n")

match_list = re.findall("[a-z]+", "파이th0n")

print(match_list)

for i in match_list:
    print(i)
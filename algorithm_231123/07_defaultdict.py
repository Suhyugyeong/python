from collections import defaultdict

my_dict = defaultdict(int)

my_dict['first'] = 5
my_dict['second'] = 4
print(my_dict['first'])
print(my_dict['second'])
print(my_dict['third'])
my_dict['third'] += 1
print(my_dict['third'])
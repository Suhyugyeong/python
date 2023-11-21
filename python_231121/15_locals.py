import sys # 시간초과 이슈가 있어요!!!

s = set()
calc_count = 5
cmd = ["add 1", "check 1", "check 2", "all", "toggle 1"]
for i in cmd:
    command = i.split()
    if command[0] == 'add':
        num = int(command[1])
        s.add(num)
    elif command[0] == 'remove':
        num = int(command[1])
        s.discard(num)
    elif command[0] == 'check':
        num = int(command[1])
        if num in s:
            print(1)
        else:
            print(0)
    elif command[0] == 'toggle':
        num = int(command[1])
        if num in s:
            s.remove(num)
        else:
            s.add(num)
    elif command[0] == 'all':
        s = set([i for i in range(1, 20 + 1)])
    elif command[0] == 'empty':
        s = set()

print(locals())

from pprint import pprint
pprint(locals())
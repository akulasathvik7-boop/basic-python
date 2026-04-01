from collections import deque
 
d=deque()
print(d)
d.appendleft(1)
d.extendleft([2,3,4,5])
print(d)

for i in d:
    print(i*i)

if 6 in d:
    print('yes')
else:
    print('false')
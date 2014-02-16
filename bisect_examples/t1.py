import bisect
import random

print('New  Pos  Contents')
print('---  ---  --------')

l = []
for i in 'asdqweqfssdfplsfjoibuhcbmn':
    position = bisect.bisect_left(l, i)
    bisect.insort(l, i)
    print('%s  %3d' %(i, position), l)


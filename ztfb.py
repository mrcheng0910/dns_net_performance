import numpy as np
fp = open('test.txt','r')
rrt = fp.readlines()
rrt_v = []
for i in rrt:
    rrt_v.append(float(i.strip()))
x = np.array(rrt_v)

from scipy import stats

rrt_zscore =  stats.zscore(rrt_v)

for i in rrt_zscore:
    if i<0:
        print -i
    else:
        print i

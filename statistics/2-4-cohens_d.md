[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

>> 
```
import thinkstats2
import nsfg
import numpy as np

def CohenEffectSize(group1, group2):
    diff = group1.mean()-group2.mean()
    var1 = group1.var()
    var2 = group2.var()
    n1, n2 = len(group1), len(group2)

    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
    d = diff / np.sqrt(pooled_var)
    return d

preg = nsfg.ReadFemPreg()
live = preg[preg.outcome == 1]

firsts = live[live.birthord == 1]
others = live[live.birthord != 1]

d1=CohenEffectSize(firsts.prglngth, others.prglngth)
d2 = CohenEffectSize(firsts.totalwgt_lb, others.totalwgt_lb)
print('The Cohen Effect Size in pregnancy length is %f.' %(d1))
print('The Cohen Effect Size in total weight is %f.' %(d2))
print('The difference between Cohens of pregancy length and total weight is %f.' %(d1-d2))
```
The Cohen Effect Size in pregnancy length is 0.028879.
The Cohen Effect Size in total weight is -0.088673.
The difference between Cohens of pregancy length and total weight is 0.117552.

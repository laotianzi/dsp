[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

>> 
```
import numpy as np
import thinkstats2
import thinkplot

%matplotlib inline

t = np.random.random(1000)

thinkplot.PrePlot(cols=2)

pmf = thinkstats2.Pmf(t)
thinkplot.SubPlot(1)
thinkplot.Pmf(pmf,linewidth=0.05)
thinkplot.Config(xlabel ='random value', ylabel='PMF')

cdf = thinkstats2.Cdf(t)
thinkplot.SubPlot(2)
thinkplot.Cdf(cdf)
thinkplot.Config(xlabel = 'random value', ylabel='CDF')
```
print('Yes, the distribution is uniform.')

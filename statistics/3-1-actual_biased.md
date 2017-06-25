[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

>> 
```python
import thinkstats2
import thinkplot
import nsfg

%matplotlib inline

def BiasPmf(pmf, label):
    new_pmf = pmf.Copy(label = label)
    for x,p in pmf.Items():
        new_pmf.Mult(x,x)
    new_pmf.Normalize()
    return new_pmf

resp = nsfg.ReadFemResp()
pmf = thinkstats2.Pmf(resp.numkdhh, label='numkdhh')

biasedPmf = BiasPmf(pmf, label = 'Biased')

thinkplot.PrePlot(cols=2)

thinkplot.SubPlot(1)
thinkplot.Pmf(pmf)
thinkplot.Config(xlabel='Number of children', ylabel='PMF')

thinkplot.SubPlot(2)
thinkplot.Pmfs([pmf, biased])
thinkplot.Config(xlabel='Number of Children', ylabel='PMF')

print('The actual means is %f.' %(pmf.Mean()))
print('The biased means is %f.' %(biasedPmf.Mean()))
print('The difference between actual mean and biased mean is %f.' %(pmf.Mean()-biasedPmf.Mean()))
```

The actual means is 1.024205.
The biased means is 2.403679.
The difference between actual mean and biased mean is -1.379474.

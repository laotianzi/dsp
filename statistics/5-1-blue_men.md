[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

>> 
```
import scipy.stats
mu = 178
sigma = 7.7
dist = scipy.stats.norm(loc=mu, scale=sigma)

dist.mean(), dist.std()
dist.cdf(mu-sigma)

low = dist.cdf(177.8)    
high = dist.cdf(185.4)   
high-low
```
A: 34.2% of the U.S. male population is in the range of 5'10" and 6'1".

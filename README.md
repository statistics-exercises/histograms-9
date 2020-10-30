# Histogram for negative binomial random variable

We are going to complete one final exercise to consolidate this business of estimating the histogram.  I would like you to calculate an estimate for the probability mass function for a negative binomial random variable with parameters `kparam` and `prob` by repeatedly sampling from this distribution and by constructing a histogram.  

The code that you need to write here is very similar to the code that you wrote when you were generating the histogram for the binomial random variable.  There are a couple of subtle differences, however.  The first one of these is that the random variable cannot be less than `kparam` as we are measuring the number of trials we have to perform in order to observe exactly `kparam` successes.  We must therefore perform at least `kparam` trials.  The consequence of this for the computing of the  histogram is that the 0th element of the list counts measures the number of times that the random was equal to `kparam` and not 0.  We thus cannot write:

````
myvar = negative_binomial( kparam, prob ) 
counts[int(myvar)] = counts[int(myvar)] + 1
````
 
We instead need to write:

````
myvar = negative_binomial( kparam, prob ) 
counts[int(myvar-kparam)] = counts[int(myvar-kparam)] + 1 
````

The second subtlety is the fact that the the random variable can take any integer value greater than or equal to `kparam`.  In other words, the sample space for this random variable is infinite.  This second problem is easily resolved, however, as the probability that the random variable is very large is very small.  We can thus truncate the `counts` list and only estimate the first `noutcomes` elements of the probability mass function.  You will need to experiment a little with how large noutcomes needs to be in practise.  If you observe problems with the indices being beyond the length of the list you will need to increase this quantity.

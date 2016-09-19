# Authors: Anand Jetha, Dylan Delaney, Kuong Tran, Rachel Cheng
# uniqnames: ajetha dylmdel kuong racheng
# Date: December 16, 2014
# Purpose: Used to find the RV that produces a certain probability.
# Description: Compares CDF of looped RV to their probability

import sys
import random
import math

"""
Requires: nothing
Modifies: nothing
Effects: generates numbers randomly from a Uniform(0,1) distribution

This function is implemented for you.
"""
def uniformGen():
	return random.random()


"""
Requires: seed is a value generated from a Uniform(0,1) distribution
		  p is the probability of success
Modifies: nothing
Effects: returns a randomly generated value from a Bernoulli(p) distribution,
	using the inverse method described in the spec
"""
def generateFromBernoulli(seed, p):
	notP = 1.0 - p
	if (notP >= seed):
		return 0
	else:
		return 1

"""
Requires: seed is a value generated from a Uniform(0,1) distribution
		  p is the probability of success
		  n is the number of trials
Modifies: nothing
Effects: returns a randomly generated value from a Binomial(n,p) distribution,
	using the inverse method described in the spec
"""
def generateFromBinomial(seed, n, p):
	notP = 1 - p #the complement
	stepInt = 0 #the current RV k being tested
	#calculates the n choose k part of the formula
	nChoose = math.factorial(n) / (
		math.factorial(n - stepInt) * math.factorial(stepInt))
	#calculates the number of success part of formula
	pRaised = p ** stepInt
	#calculated the number of failures part of formula
	notpRaised = (notP) ** (n - stepInt)
	#calculated the pdf at RV = 0 and starts cdf
	cdf = nChoose * pRaised * notpRaised
	while seed > cdf:
		stepInt += 1
		nChoose = math.factorial(n) / (
			math.factorial(n - stepInt) * math.factorial(stepInt))
		pRaised = p ** stepInt
		notpRaised = (notP) ** (n - stepInt)
		cdf += nChoose * pRaised * notpRaised
	return stepInt

"""
Requires: seed is a value generated from a Uniform(0,1) distribution
		  p is the probability of success
Modifies: nothing
Effects: returns a randomly generated value from a Geometric(p) distribution,
	using the inverse method described in the spec
"""
def generateFromGeometric(seed, p):
	notP = 1 - p #the complement
	stepRV = 0 #the current RV k being tested
	cdf = 1 - (notP ** (stepRV + 1))
	while seed > cdf:
		stepRV += 1
		cdf = 1 - (notP ** (stepRV + 1))
	return stepRV

"""
NOTE FOR THE FOLLOWING TWO FUNCTIONS: You WILL lose points on the bare-bones
	portion of the project if you simply make a call to the corresponding
	function in the random library. The idea is that everyone gains an
	understanding of how to write code to analyze data, and these distributions
	are the easiest implementations of the inverse method for continuous random
	variables.
"""

"""
Requires: seed is a value generated from a Uniform(0,1) distribution
		  a is the beginning of the interval
		  b is the end of the interval
Effects: returns a randomly generated value from a Uniform(a,b) distribution,
	using the inverse method described in the spec
"""
def generateFromUniform(seed, a, b):
	rv = (seed * (b - a)) + a
	return rv

"""
Requires: seed is a value generated from a Uniform(0,1) distribution
		  ld (lambda) is the rate at which the distribution decays
Modifies: nothing
Effects: returns a randomly generated value from a Exponential(ld) distribution,
	using the inverse method described in the spec
"""
def generateFromExponential(seed, ld):
	rv = -1 * math.log(1 - seed) / ld
	return rv


"""
Generating from a normal distribution in a non-hacky way is nearly impossible,
so we provide you with a function that calls the library for you.

Requires: mu is the mean of the distribution
		  sigma is the standard deviation of the distribution
Effects: Returns a randomly generated sample from a Normal(mu, sigma)
	distribution
"""
def generateFromNormal(mu, sigma):
	return random.gauss(mu, sigma)


"""
The following function is not required, but your dataset may need you to
implement it. If you would like to implement it, remove the "pass" statement
and implement your function as normal.
"""

"""
Requires: seed is a value generated from a Uniform(0,1) distribution
		  ld (lambda) is the approximation of n*p from the Binomial(n,p)
			distribution
Modifies: nothing
Effects: returns a randomly generated value from a Poisson(ld) distribution,
	using the inverse method described in the spec
"""
def generateFromPoisson(seed, ld):
	rv = 0
	cdf = (ld ** rv) * math.exp(-1 * ld)
	while seed > cdf:
		rv += 1
		cdf += (ld ** rv) * math.exp(-1 * ld) / math.factorial(rv)
	return rv


# DO NOT modify these 2 lines of code or you will be very sad
# Similarly, do not place any code below them
if __name__ == "__generation__":
	main(sys.argv)


'''
    Integration with Monte Carlo technique 


'''


import random 
import math
#use monte carlo technique to compute integrals with different dimensions


from testIntegrals import *

#1 dimension integral 
def monte_carlo1 (fonc, n , a, b):
    sumG = 0
    for i in range(n):
        xi = random.uniform(a,b)
        sumG += fonc(xi)

    #domain area
    dArea = (b-a)

   #return the integral
    return dArea * (1/n) * sumG


print("integral function1 = " + str(monte_carlo1(fun1,100, 0,1)))

print("integral function2 = "+ str(monte_carlo1(fun2,100, 0, math.sqrt(3))))


#2 dimension integral
def monte_carlo2 (fonc, n , a, b , c ,d):
    sumG = 0
    for i in range(n):
        xi = random.uniform(a,b)
        yi = random.uniform(c,d)
        sumG += fonc(xi,yi)

    #domain area
    dArea = (b-a) * (d-c)

   #return the integral
    return dArea * (1/n) * sumG




print("integral function3 = "+ str(monte_carlo2(fun3,100, 2, 4, 3,4 )))


#3 dimension integral 
def monte_carlo3 (fonc, n, a, b, c, d , e, f):
    sumG = 0
    for i in range(n):
        xi = random.uniform(a,b)
        yi = random.uniform(c,d)
        zi = random.uniform(e,f)
        sumG += fonc(xi,yi,zi)

    #domain area
    dArea = (b-a) * (d-c) * (f-e)

   #return the integral
    return dArea * (1/n) * sumG



print("integral function4 = "+ str(monte_carlo3(fun4,100,-3, 0, 2, 5,2,3 )))












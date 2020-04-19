#!/usr/bin/env python3

import numpy as np

s0=0
s1=540000
s2=1210000
s3=2420000
s4=4530000



def paytax(salary):
    if (salary <= s1) & (salary>=s0):
        tax=salary*0.05-0
        level=1
    elif (salary <= s2) & (salary>s1):
        tax=salary*0.12-37800
        level=2
    elif (salary <= s3) & (salary>s2):
        tax=salary*0.2-134600
        level=3
    elif (salary <= s4) & (salary>s3):
        tax=salary*0.3-376600
        level=4
    else:
        tax=salary*0.4-829600
        level=5
    net=salary-tax
    print("salary = ", salary/10000, "(w) | tax = ", tax/10000, "(w) | net income = ", net/10000, "(w) | level = ", level)
    

ex0=paytax(400000)
ex1=paytax(1200000)
ex11=paytax(1210000)
ex12=paytax(1220000)

ex2=paytax(1300000)
ex3=paytax(1400000)
ex4=paytax(2400000)
ex5=paytax(3400000)
ex6=paytax(4600000)
   

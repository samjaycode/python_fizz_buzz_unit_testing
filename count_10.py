# -*- coding: utf-8 -*-
#created by Sam Ryan
#on 8/19/16

#fizzbuzz test
number = 0
v3 = "fizz"
v5 = "buzz"
l = []
while number < 101:
    if number % 3 == 0 and number % 5 == 0:
        l.append(v3+' '+v5) 
    elif number % 3 == 0: 
        l.append(v3)
    elif number % 5 == 0: 
        l.append(v5)
    else:
        l.append(number)
    
    number += 1


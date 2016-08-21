# -*- coding: utf-8 -*-
#created by Sam Ryan
#on 8/19/16

#fizzbuzz test

def fizzbuzz(number) :
    v3 = "fizz"
    v5 = "buzz"
    if number % 3 == 0 and number % 5 == 0:
        return v3+' '+v5
    elif number % 3 == 0: 
        return v3
    elif number % 7 == 0: 
        return v5
    else:
        return number



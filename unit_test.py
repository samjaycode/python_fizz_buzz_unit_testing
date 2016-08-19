# -*- coding: utf-8 -*-
#created by Sam Ryan
#on 8/19/16
#unit testing

from count_10 import fizzbuzz
#unit testing return values from function

assert fizzbuzz(5) == 'buzz'

assert fizzbuzz(3) == 'fizz'

assert fizzbuzz(15) == 'fizz buzz'

assert fizzbuzz(1) == 1

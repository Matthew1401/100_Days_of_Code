# -*- coding: utf-8 -*-
# Day 4 Project: random

import random
import my_module
print(my_module.pi)

random_integer = random.randint(1, 10) # 1 - 9
print(random_integer)

random_float = random.random() # 0.000000 - 0.9999999999
print(random_float)

random_float_5 = random.random() * 5 # 0.0000 - 0.999999 * 5 == 0.00000 - 4.99999
print(random_float_5)
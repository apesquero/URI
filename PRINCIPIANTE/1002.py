# -*- coding: utf-8 -*-

import math

area = None
pi = None
radio = None

def read_numeric():
  try:
    # read for Python 2.x
    return float(raw_input())
  except NameError:
    # read for Python 3.x
    return float(input())


radio = read_numeric()
pi = 3.14159
area = pi * (math.pow(radio, 2))
print(str("A=") + "{0:.4f}".format(area))

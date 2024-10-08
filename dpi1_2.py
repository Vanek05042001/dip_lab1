# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 17:47:24 2024

@author: Vanya
"""
import numpy as np

rnd = np.random.default_rng()
b = rnd.integers(0, 4, (5,5), endpoint=True)
print(b)
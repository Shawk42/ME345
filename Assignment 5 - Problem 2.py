"""Assignment 5 - Problem 2"""
import numpy as np
import matplotlib.pyplot as plt

"""Givens"""
T = 293    #Temperature for everything else
T_m = 298    #Temperature for mecury
p = 1
R_cr = 5*(10**5)
V = 3.5

"""Table Values"""
print("Key","[Air,Water,Mercury]")
nu_air = 15*(10**-6)            #nu for air from table @300K
nu_water = (959*(10**-6))/(998) #nu for water from table @265K
nu_mercury = .1125              #nu for mercury from table @300K

nu = np.array([nu_air,nu_water,nu_mercury])

L = (nu*R_cr)/V
print(L,"meters")




"""Assignment 5 - Problem 1"""
import numpy as np
import matplotlib.pyplot as plt

"""Givens"""
p = 1              #given pressure in [atm]
T = 25+273.15             #given temperature in [K]
V = 25             #given velocity in m/s
Re_cr = 5*(10**5)  #Critical reynolds number

"""Linear Interpolation - From Table in textbook"""
print("Interpolation for Density")
x_1 = float(input("What is the low temperature"))
x_2 = T
x_3 = float(input("What is the high temperature"))
y_1 = float(input("What is the low density"))
y_3 = float(input("What is the high density"))
y_2 = (((x_2-x_1)*(y_3-y_1))/(x_3-x_1))+y_1
rho = y_2

print("Interpolation for v - At same temperature")
y_1 = float(input("What is the low v"))
y_3 = float(input("What is the high v"))
y_2 = (((x_2-x_1)*(y_3-y_1))/(x_3-x_1))+y_1
v = y_2

print(rho,"rho")
print(v,"v")

"""Calculations"""
L = (v*Re_cr)/V
print(L,"Length in meters")

"""Plotting"""
L_g = np.linspace(0,.5,num=500)
Re = (V*L_g)/v
plt.plot(L_g,Re)
plt.show()

#ineresting linear relationship that confirms the answer

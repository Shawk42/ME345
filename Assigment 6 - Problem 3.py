"""Heat Transfer - Assignment 6 Problem 2"""
print("Assignemt 6 problem 2")
import numpy as np

"""Givens"""
Klv = 273.15       #Conversion from C to K
D = .01            #Outer Diameter
T_sphere = 90+Klv  #Tempearature of spehere in Kelvin
vel = 2              #Velocity of water stream
T_water = 12+Klv   #Temperature of water in Kelvin

"""Water properties at 285K [from book]"""
mu = 1225*(10**-6)
vol_spec = 1*(10**-3)
rho = 1/vol_spec
Pr = 8.81

"""Interpolation X=temp, Y=property"""
x_1 = 360
x_2 = T_sphere
x_3 = 365

"""mu_water interpolation"""
y_1 = 324*(10**-6)
y_3 = 306*(10**-6)

y_2 = (((x_2-x_1)*(y_3-y_1))/(x_3-x_1))+y_1
mu_s = y_2
#print(mu_s, "mu_s") #Logical value

"""Intermediate calulcations"""
Re = (rho*vel*D)/mu
#print(int(Re), "Re")

Nuss = 2+(.4*(Re**.5)+0.06*(Re**(2/3)))*(Pr**.4)*((mu/mu_s)**.25)
#print(Nuss, "Nusselt number")

K = 590*(10**-3)     #K for water infinite
h = (Nuss*K)/D
print(h, "h")

"""Answer"""
A = 4*np.pi*(D/2)**2
Delta_T = T_sphere-T_water
q = h*A*Delta_T
print(q)
"""Verification Logic"""
print("-" *50)
print("Verification Logic results")
print("-" *50)
#ensures correct temperature inputs for interpolation
if x_2 > x_1 and x_3 > x_2:
    print("Interpolation temperatures are correct")
else:
    print("Interpolation temperatures are incorrect")
#ensures conditions are met for equation (Reynolds)
if Re <= 3.5*(10**4) and Re <= 7.6*(10**4):
    print("Equation is valid")
else:
    print("Equation is invalid")
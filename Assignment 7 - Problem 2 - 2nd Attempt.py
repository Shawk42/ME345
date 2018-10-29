'''Assignment 7 - Problem 2 - Second Attempt'''
print("Assignment 7 - Problem 2 - Second Attempt")
print(" "*50)

import numpy as np
import matplotlib.pyplot as plt

"""GIVENS"""
Kelvin = 273.15       #Conversion from C to K
m_dot = .5            #mass flow rate through the pipe     [kg/s]
D = .05               #diameter of pipe                    [m]
T_i = 20+Kelvin       #Tempearture of oil coming into pipe [K]
T_s = 150+Kelvin      #Constant surface temp of pipe       [K]
L = 25                #Length of pipe                      [m]

pi = np.pi

fact = float(input("How much larger is the outlet temperature expected to be"))


"""Assumptions"""
T_o_a = fact*T_i          #Assumed outlet temp of pipe         [m]
T_mean_a =(T_o_a+T_i)/2  #Assumed average temp of fluid       [m]

"""
FLUID PROPERTIES from
http://cecs.wright.edu/people/faculty/sthomas/htappendix01.pdf
"""
#Table import
T_tab = [0+Kelvin,20+Kelvin,40+Kelvin,60+Kelvin,80+Kelvin,100+Kelvin,120+Kelvin,140+Kelvin,150+Kelvin]
mu_tab = [3.814,0.8374,0.2177,0.07399,0.03232,0.01718,0.01029,0.006558,0.005344 ]
Pr_tab = [46639,10863,2962,1080,499.3,279.1,176.3,118.1,98.31]
K_tab = [0.1469,0.1450,0.1444,0.1404,0.1380,0.1367,0.1347,0.1330,0.1327]
Cp_tab = [1797,1881,1964,2048,2131,2220,2308,2395,2441]

#Interpolaions
mu = np.interp(T_mean_a,T_tab,mu_tab)        #Interpolating mu
Pr = np.interp(T_mean_a,T_tab,Pr_tab)        #Interpolating Pr
K = np.interp(T_mean_a,T_tab,K_tab)          #Interpolating K
Cp = np.interp(T_mean_a,T_tab,Cp_tab)         #Interpolating Cp

"""FLOW TYPE CALCULATIONS"""
#Reynolds number
Re = (4*m_dot)/(pi*D*mu)

if Re < 2300:
    print("Flow is Laminar - Re is =",int(Re))
if Re > 2300:
    print("The flow is turbulent - Re is =",int(Re))
if Re > 2300 and Re <3000:
    print("Flow is in transition region")
#Hydrdulic Developing Length
x_hyd = 0.05*Re*D

if x_hyd < L:
    print("Hydraulic flow is FULLY DEVELOPED - Develops at",x_hyd)
else:
    print("Hydraulic flow is UNDEVELOPED- Develops at",x_hyd)

#Thermal Developing Length
x_thr = 0.05*Re*Pr*D

if x_thr < L:
    print("Thermal BL is FULLY DEVELOPED - Develops at",x_thr)
else:
    print("Thermal BL is UNDEVELOPED- Develops at",x_thr)

"""h CALCULATIONS"""
Gz = (D/L*.5)*Re*Pr
num = 0.0668*Gz
dem = 1+(0.04*Gz**(2/3))
Nu_d = 3.66+(num/dem)

h = (K/D)*Nu_d

"""TEMP OUT CALCULATIONS"""
P = pi*D                      #Perimter length out [m]
beta = ((-P*L)/(m_dot*Cp))*h  #Intermediate term
alpha = np.e**beta            #Intermeidat term
T_o = -alpha*T_s+alpha*T_i+T_s

alpha_check = (T_s-T_o)/(T_s-T_i)
dev = np.absolute(alpha-alpha_check)

if dev <= .00000001:
    print("Surface temp verified by alpha")
    print("Alpha Deviation",dev)
else:
    print("Suface temp INVALID by alpha check"," Alpha Deviation", dev)

if T_o < T_i:
    print("INVALID solution the temperature is dropping along the pipe")

"""q CALCULATION [HEAT RATE]"""
delta_T = T_o-T_i
q = m_dot*Cp*delta_T
error = T_o-T_o_a

if error > 0:
    print("Above the assumed value")
else:
    print("Below the assumed value")

"""PRINTING"""

print(" "*50)
print("RESULTS AND TROUBLESHOOTING")
print("-"*50)
print("Inlet temp",T_i,"[K]")
print("Assumed outlet temp",T_o_a,"[K]")
print("Assumed average temp",T_mean_a,"[K]")
print("Outlet temp",T_o,"[K]")
print("Heat Rate",q*.001,"[kW]")
print("Error",error)

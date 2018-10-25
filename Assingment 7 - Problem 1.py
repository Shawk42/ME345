"""Assignment 7 - Problem 1"""
print("Assignment 7 - Problem 1")

import numpy as np

"""Givens"""
D = .025        #Diameter of pipe in meters [m]
L = 15          #Length of pipe in meters [m]
m_dot = .001    #Mass flow rate in [kg/s]
Ti = 325        #Entrance temperature [K]
To = 425        #Exit temperature [K]

"""AVG TEMP CALCS"""
Tavg = (Ti+To)/2

"""FLUID PROPS"""
#[water, engine oil,mercury]
nu = np.array([(274*(10**-6)), (1.635*(10**-2)), (0.124*(10**-2))])  #nu from table at 375K [N-s/m^2]
Re = ((4*m_dot)/(np.pi*D*nu))   #Reynolds number
Pr = np.array([1.70, (300+233)/2, (0.0196+0.0163)/2 ])      #Pr from table using avg. as interpolations

"""INTERMEDIATE CALCULATIONS"""
x_f = .05*Re        #Fluid flow developed length
x_t = x_f*Pr        #Thermal BL developed length


"""Logic and Verifications"""
print("-"*50)
print("VERIFICATION AND LOGIC")
print("-"*50)

Re_wa = Re.item(0)            #pullling values from Re array
Re_eo = Re.item(1)            #pullling values from Re array
Re_mer = Re.item(2)            #pullling values from Re array

#Checking if flow is turblent or laminar
if Re_wa <= 2300:
    print("Water flow is Laminar - Re is", int(Re_wa))
else:
    print("Water flow is turbulent - Re is", int(Re_wa))
if Re_eo <= 2300:
    print("Engine Oil flow is Laminar - Re is", int(Re_eo))
else:
    print("Engine Oil flow is turbulent - Re is", int(Re_eo))
if Re_eo <= 2300:
    print("Mercury flow is Laminar - Re is", int(Re_mer))
else:
    print("Mercury Oil flow is turbulent - Re is", int(Re_mer))

#checking fluid developing length
print(L, "The length of the pipe is")
print(x_f, "Fluid flow fully develops at")
print(x_t, "Thermal boundry latyer fully develops at")

print(Pr, "Pr")
print(Re, "Re")


"""Result Printing"""
print("-"*50)
print("RESULTS")
print("-"*50)
print(Tavg, "Average Temperature in Kelvin")




"""Assigment 7 - Problem 2"""
print("Assigment 7 - Problem 2")
import numpy as np

'''GIVENS'''
Kelvin = 273.15
m_dot = 0.5     #mass flow flow rate [kg/s]
T_i = 20+Kelvin #Inlet tempearture [Kelvin]
T_i_c = 20      #Inlet temperature [C]
T_s = 150+Kelvin #Surface temperature [Kelvin]
D = 0.05         #Diamter of pipe [meters]
L = 25           #Length of pipe [meters]

'''ASSUMPTIONS'''
#T_o_a = (2*T_i_c)+Kelvin   # Initiial Outlet temperature assumption
T_o_a = 420                 #Iteration 1 average
T_avg_a = (T_i+T_o_a)/2

'''FLUID PROPERTIES'''
"""Interpolation X=temp, Y=property"""
x_1 = 350
x_2 = T_avg_a
x_3 = 360
"""Cp interpolation"""
y_1 = 2.118
y_3 = 2.161
y_2 = (((x_2-x_1)*(y_3-y_1))/(x_3-x_1))+y_1
Cp = y_2
"""Pr interpolation"""
y_1 = 546
y_3 = 395
y_2 = (((x_2-x_1)*(y_3-y_1))/(x_3-x_1))+y_1
Pr = y_2
"""Mu interpolation"""
y_1 = 3.56*(10**-2)
y_3 = 2.52*(10**-2)
y_2 = (((x_2-x_1)*(y_3-y_1))/(x_3-x_1))+y_1
mu = y_2

#"""Values at T = 430K"""
#Cp = 2.471
#Pr = 88
#mu = 0.470*(10**-2)
K = 138*(10**-3)            #Thermal Conductivity [constant value in range]
Re = (4*m_dot)/(np.pi*D*mu) #Reynolds number calcations
x_f = 0.05*Re*D             #Distance to fully developed flow
x_t = 0.05*Re*Pr*D          #Distance to fully developed thermal BL

'''INTERMEDIATE CALCULATIONS'''
G_zd = (D/L)*Re*Pr
a = 0.0668*G_zd
b = 1+0.04*G_zd**(2/3)
Nu_d = 3.66+(a/b)
h = (K*Nu_d)/D

'''OUTLET TEMP CALCULATION'''
P = np.pi*D               #Perimeter length of pipe
d = (-(P*L)/(m_dot*Cp))
c = T_s-T_i
T_o = (-np.e**d)*c+T_s
T_avg = (T_i+T_o)/2

'''q calculations'''
area = np.pi*(D/2)**2*L
q = h*area*(T_s-T_o)

'''LOGIC'''
#Flow type
if Re < 2300:
    print("Flow is laminar - ",Re)
else:
    print("Flow is turbulent - ",Re)

#Boundry layer forming
if Pr > 1 and x_f < x_t:
    print("BL formed correctly")
elif Pr < 1 and x_f > x_t:
    print("BL formed correctly")
else:
    print("BL forming conditions INVALID")

#Pr check for equations
if Pr >= 5:
    print("Nu_d equation is valid")
else:
    print("Nu_d equation is INVALID")

'''Printing'''
print("-"*50)
print("INTERMEDIATE VALUES")
print("-"*50)
print("Assumed outlet temp = ",T_o_a)
print("Assumed mean temp = ", T_avg_a )
print("Distance to fully developed flow =",x_f)
print("Distance to thermal BL devloped =", x_t)
print("Nu_d =",Nu_d)
print("h =",h)
print("Outlet Temperature =",T_o)
print("Heat transfer rate =", q)
print("Actual minus estimate of outlet temp =", T_o-T_o_a)

'''PROCESS PRINTING'''
print("-"*50)
print("PROCESS PRINTING")
print("-"*50)
print("The fluid enters the pipe at",T_i)
print("The pipe is surrounded by a constant temperature of",T_s)
print("It was assumed that the fluid exits the pipe at",T_o_a)
print("The fluid was then caclulated to exit the pipe at ",T_o)
print("The fluid was transfering heat out the pipe into the surface at a rate of",q)
print("The fluid is at an average tempearture of",T_avg)
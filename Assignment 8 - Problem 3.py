'''ASSIGNEMNT 8 - PROBLEM 3'''
print("ASSIGNMENT 8 - PROBLEM 3")
import numpy as np
import scipy.constants as cst

"""GIVENS"""
m2 = 1/10000                  #Converion from cm^2 to m^2
A_1 = 5*m2                    #Area 1 [m^2]
A_2 = 9*m2                    #Area 2 [m^2]
theta_1 = np.radians(45)      #Theta_1 [radians]
theta_2 = np.radians(70)      #Theta_2 [radians]
r = 1.3                       #Distance between plates
q = 625*(10**-5)              #Wattage coming from the first plate
sigma = cst.Stefan_Boltzmann  #Importing the Boltzman constant


"""NORMAL AREA"""
An_1 = A_1*np.cos(theta_1)  #Normal area of area_1
An_2 = A_2*np.cos(theta_2)  #Normal area of area_2

"""OMEGA CALCULATIONS"""
w_1 = An_1/(r**2)         #omega calculations
w_2 = An_2/(r**2)

"""INTENSITY CALCULATIONS"""
I_1 = q/(An_1*w_1)       #Intensity of plate 1

"""TEMPERATURE CALCULATIONS"""
pi = np.pi
T_s = ((pi*I_1)/sigma)**0.25


"""ANSWER VALIDATION AND SOLUTION PRINTING"""
print(""*50)
print("-"*20,"ANSWER VALIDATION","-"*20)

#Checking omega
w_max = .1
if w_1 <= w_max and w_2 <= w_max:
    print("Curvature can be ignored")
else:
    print("ERROR - Curvature cannot be ignored")
    print("Omega 1",w_1)
    print("Omega 2",w_2)
#Boltzman printing
print("The boltzman constant used was ",sigma)

print(""*50)
print("-"*20,"SOLUTION","-"*20)
print("Intensity of radiation from area_1 ",I_1)
print("The temperature at the surface of area 1 is",T_s)

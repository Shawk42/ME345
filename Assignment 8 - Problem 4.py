'''ASSIGNEMNT 8 - PROBLEM 4'''
print("ASSIGNMENT 8 - PROBLEM 4")
import numpy as np
import scipy.constants as cst

"""GIVENS"""
T_inf = 290                   #Temperature of air      [K]
h = 25                        #Convection coeff of air [W/(m^2-K)]
J = 3500                      #Radiosity               [W/m^2]
rho = 0.4                     #Reflectivity            [dim]
sigma = cst.Stefan_Boltzmann  #Importing the Boltzman constant
T_s = 425                     #Temperature of surface  [K]

"""PART A [IRRADIATION ON SURFACE]"""
E = sigma*(T_s**4)            #Blackbody radiation from the cube
G = (J-E)/rho                 #Irradiation on the surface [ANSWER]

"""PART B [ABSORPTIVITY OF SURFACE]"""
alpha = 1-rho                #Absorptivity of surface

"""PART C [EMISSIVE POWER OF THE SURFACE]"""
q_conv = h*(T_s-T_inf)
q_rad = E-(alpha*G)
q_tot = q_conv+q_rad

"""PART D [EMMISIVITY OF SURFACE]"""



"""SOLUTION AND SOLUTION VALIDATION"""
print(""*50)
print("-"*20,"ANSWER VALIDATION","-"*20)
print("The boltzman constant used was ",sigma)

print(""*50)
print("-"*20,"SOLUTION","-"*20)
print("Part A - Irradiation on the surface =",int(G),"[W/m^2]")
print("Part B - Absorptivity of surface = ",alpha,"[dim]")
print("Part C - Emissive power of the surface",int(E),"[W/m^2]")


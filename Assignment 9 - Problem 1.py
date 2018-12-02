'''ASSIGNMENT 9 - PROBLEM 1'''
print("Assignment 8 - Problem 1")
import numpy as np
import scipy.constants as cst

sigma = cst.Stefan_Boltzmann    #Importing the Boltzman constant

"""PART A"""
T_s = 800    #Given surface tempearture in K

Tlamnda4 = T_s*4    #Finding lamnda T at each integration point
Tlamnda6 = T_s*6
Tlamnda8 = T_s*8

print("Lamnda T at 4 um =",Tlamnda4)
print("Lamnda T at 6 um =",Tlamnda6)
print("Lamnda T at 8 um =",Tlamnda8)
#F4 = float(input("What is the F value at 4 um = "))  #0.318102 [old inputs]
#F6 = float(input("What is the F value at 6 um = "))  #0.607559 [old inputs]
#F8 = float(input("What is the F value at 8 um = "))  #0.769234 [old inputs]
F4 = 0.318102
F6 = 0.607559
F8 = 0.769234

frac1 = F4     #Fraction emmitted {results of integrals}
frac2 = F6-F4
frac3 = F8-F6

epsilon = 0.4*frac1+0.8*frac2+0.2*frac3  #Finding epsilon value

#print(epsilon,"PART A SOLTUION")

print(""*50)
print("PART B")
T_surr = 1500   #Given irradiation temperature of surroundings
Tlamnda4_surr = T_surr*4    #Finding lamnda T at each integration point
Tlamnda6_surr = T_surr*6
Tlamnda8_surr = T_surr*8

print("Lamnda T at 4 um =",Tlamnda4_surr)
print("Lamnda T at 6 um =",Tlamnda6_surr)
print("Lamnda T at 8 um =",Tlamnda8_surr)
#F4_surr = float(input("What is the F value at 4 um = "))  #0.480877 [old inputs]
#F6_surr = float(input("What is the F value at 6 um = "))  #0.737818 [old inputs]
#F8_surr = float(input("What is the F value at 8 um = "))  #0.856288 [old inputs]
F4_surr = 0.480877
F6_surr = 0.737818
F8_surr = 0.856288

frac1_surr = F4_surr         #Fraction emmitted {results of integrals}
frac2_surr = F6_surr-F4_surr
frac3_surr = F8_surr-F6_surr

alpha = 0.4*frac1_surr+0.8*frac2_surr+0.2*frac3_surr  #Finding epsilon value

#print(alpha,"PART B SOLTUION")

print(""*50)
print("PART C")
E = epsilon*sigma*(T_s**4)   #Energy from surface temp
rho = 1-alpha
G = sigma*(T_surr**4)        #Energy from blackbody surroundings
J = E+rho*G
#print(J,"PART C SOLUTION")

print(""*50)
print("PART D")
q_rad = J-G
#print(q_rad,"PART D SOLUTION")

print(""*50)
print("SOLUTIONS")
print("-"*50)
print("Part A (Emissivity) = ",epsilon,"[dim]")
print("Part B (Absorptivity) = ", alpha,"[dim]")
print("Part C (Radiosity) =",J,"[W/m^2]")
print("Part D (Heat Flux)",abs(q_rad)*0.001,"[kW/m^2] into the surface")



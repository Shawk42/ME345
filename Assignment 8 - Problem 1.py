'''ASSIGNEMNT 8 - PROBLEM 1'''
print("ASSIGNMENT 8 - PROBLEM 1")
import numpy as np
import scipy.constants as cst

"""GIVENS AND VARIABLE CONDITIONING"""
T_1 = 2000  #[K]
T_2 = 3300  #[K]
lam_low = .4    #[um]
lam_high = .7   #[um]

lam = np.array([lam_low,lam_high])
low = 0
high = 1


"""CONSTANTS"""
sigma = cst.Stefan_Boltzmann      #Importing the Boltzman constant


"""LAMNDA T VALUES"""
lam_T1 = T_1*lam
lam_T2 = T_2*lam
print(""*50)
print("--" * 10, "LamndaT values", "--" * 10)
print("Lamnda T1 [low,high]",lam_T1)
print(""*50)
print("Lamnda T2 [low,high]",lam_T2)
print(""*50)

"""F(0 to lamnda) input and conditioing"""
print("F inputs for ",T_1)
F_11 = float(input("Input the lower F value for 2000K "))
F_12 = float(input("Input the upper F value for 2000K "))
print("F inputs for ",T_2)
F_21 = float(input("Input the lower F value for 3300K "))
F_22 = float(input("Input the upper F value for 3300K "))

F_2000 = F_12-F_11  #Finding the percentage for each temp
F_3000 = F_22-F_21


"PRINTING"
print(""*50)
print("--"*10,"CONSTANTS USED","--"*10)
print("Boltzman Constant ",sigma)



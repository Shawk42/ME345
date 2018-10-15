"""Heat Transfer - Assignment 6 Problem 2"""
print("Assignemt 6 problem 2")
import numpy as np
import matplotlib.pyplot as plt

"""Givens"""
Klv = 273.15      #Conversion from C to K
L = 4             #Length in meters
D_in = .07        #Inner diameter in meters
D_out = .08       #Outer diameter in meters
T_steam = 150+Klv #Temperature of steam in Kelvin
T_inf = 25+Klv    #Temperature of air in Kelvin
V_inf = 5         #Velocity of air in m/s

"""Assumed Values"""
T_f = np.linspace(T_steam-200,450)         #Temperature of air "film"
#print(T_f, "Temperature of film in Kelvin [initial guess]")

"""Interpolation X=temp, Y=property"""
x_1 = 400
x_2 = T_f
x_3 = 450

"""nu interpolation"""
y_1 = 26.41*(10**-6)
y_3 = 32.39*(10**-6)

y_2 = (((x_2-x_1)*(y_3-y_1))/(x_3-x_1))+y_1
nu = y_2
#print(nu,"nu") #Logical result
"""Pr interpolation"""
y_1 = .690
y_3 = .686

y_2 = (((x_2-x_1)*(y_3-y_1))/(x_3-x_1))+y_1
Pr = y_2
#print(Pr, "Pr") #Logical result

"""K interpolation"""
y_1 = 33.8*(10**-3)
y_3 = 37.3*(10**-3)

y_2 = (((x_2-x_1)*(y_3-y_1))/(x_3-x_1))+y_1
K = y_2
#print(int(K), "K") #Logical result

"""Intermediate Calculations"""
Delta_T = T_f-T_inf

Re = (V_inf*D_out)/nu
#print(int(Re), "Reynolds number")

check = Re*Pr                         #check for equation
#print(int(check), "x should be greater than .2")

x = .62*(Re**.5)*(Pr**(1/3))
#print(x, "x") #correct output
y = (1+((.4/(Pr))**(2/3)))**(-.25)
#print(y, "y")  #correct output
z = (1+((Re/282000)**(5/8)))**(4/5)
#print(z, "z") #correct output
Nu_d = .3+x+y+z                       #caclulating Average Nu_d

h = (Nu_d*K)/D_out                    #calculating average h value

rad = D_out/2
area = 2*np.pi*rad*L               #surface area of outside of the cylinder

"""Solution Calculation [ANSWER]"""

q = h*area*Delta_T

print("-" *50)
print("Answer")
print("-" *50)
#print(int(q),"q")
#print((q*.001),"q in kW")
print("q at 420K was 3.601 kW")

"""Troubleshooting"""
print("-" *50)
print("Troubleshooting")
print("-" *50)

#print(rad, "radius")                #correct
#print(area, "surface area of pipe") #correct
#print(Delta_T, "Delta_T")             #correct
#print(x, "x")                       #correct
#print(y, "y")                       #correct
#print(z, "z")                       #correct
#print(Nu_d, "Nu_d")                 #correct
#print(K, "K")
#print(D_out,"D_out")
#print(h,"h")
#print(T_steam, "T of steam")
#print(T_f, "T of film")
#print(K, "K")


"""Verification Logic"""
print("-" *50)
print("Verification Logic results - removed for graphing")
print("-" *50)

"""
#ensures correct temperature inputs for interpolation
if x_2 > x_1 and x_3 > x_2:
    print("Interpolation temperatures are correct")
else:
    print("Interpolation temperatures are incorrect")

#ensures correct variable reassignment
if nu != Pr and nu != K and K != Pr:
    print("Variables reassigned correctly")
else:
    print("Variables reassigned incorrectly")

#ensures equation is valid
if check >= .2:
    print("Equation is valid")
else:
    print("Equation is invalid")
"""
plt.plot(q*.001,T_f, 'g')
plt.plot(3.601,420,'r*')
plt.xlabel("q")
plt.ylabel("T_film")
plt.axvline(x = 3.601)    #line at point
plt.hlines(420,-3,4,'b')
plt.title("Graphical Interation")
plt.grid()
plt.show()
"""Assignment 7 - Problem 1"""
print("Assignment 7 - Problem 1")

import numpy as np

"""Givens"""
D = .025        #Diameter of pipe in meters [m]
L = 15          #Length of pipe in meters [m]
m_dot = .01    #Mass flow rate in [kg/s]
Ti = 325        #Entrance temperature [K]
To = 425        #Exit temperature [K]

"""AVG TEMP CALCS"""
Tavg = (Ti+To)/2

"""FLUID PROPS"""
#[water, engine oil,mercury]
nu = np.array([(274*(10**-6)), (1.635*(10**-2)), (0.124*(10**-2))])  #nu from table at 375K [N-s/m^2]
Re = ((4*m_dot)/(np.pi*D*nu))   #Reynolds number
Pr = np.array([1.70, (300+233)/2, (0.0196+0.0163)/2 ])      #Pr from table using avg. as interpolations
K = np.array([(681*(10**-3)), (.137+.136)/2, (9180000+9800000)/2])   #K from table using avg. as interpolations

water = 0
engine_oil = 1
mercury = 2

"""INTERMEDIATE CALCULATIONS"""
x_f = .05*Re*D        #Fluid flow developed length
x_t_a = np.multiply(Re,Pr)        #Thermal BL developed length intermediate
x_t = .05*x_t_a*D      #Thermal boundry layer developing length

Nu_d = 4.36             #Flow is fully developed, as well as thermal boundry layer

Re_wa = Re.item(water)            #pullling values from Re array
Re_eo = Re.item(engine_oil)            #pullling values from Re array
Re_mer = Re.item(mercury)            #pullling values from Re array

"""ANSWER CALCULATION"""
h = (K*Nu_d)/D    #h for water


"""LOGIC AND VERIFICATION"""
print("-"*50)
print("VERIFICATION AND LOGIC")
print("-"*50)



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
#water verification
x_f_w = x_f.item(water)
x_t_w = x_t.item(water)
Pr_w = Pr.item(water)
if Pr_w > 1:
    if x_f_w < x_t_w:
        print("Water boundry layers forming correctly")
    else:
        print("Water boundry layers formed incorrectly")
if Pr_w < 1:
    if x_f_w > x_t_w:
        print("Water boundry layers forming correctly")
    else:
        print("Water boundry layers formed incorrectly")
#Engine oil verification
x_f_eo = x_f.item(engine_oil)
x_t_eo = x_t.item(engine_oil)
Pr_eo = Pr.item(engine_oil)
if Pr_eo > 1:
    if x_f_eo < x_t_eo:
        print("Engine Oil boundry layers forming correctly")
    else:
        print("Engine Oil layers formed incorrectly")
if Pr_eo < 1:
    if x_f_eo > x_t_eo:
        print("Engine Oil layers forming correctly")
    else:
        print("Engine Oil layers formed incorrectly")
#Mercury verification
x_f_m = x_f.item(mercury)
x_t_m = x_t.item(mercury)
Pr_m = Pr.item(mercury)
if Pr_m > 1:
    if x_f_m < x_t_m:
        print("Mercury boundry layers forming correctly")
    else:
        print("Mercury boundry layers formed incorrectly")
if Pr_m < 1:
    if x_f_m > x_t_m:
        print("Mercury boundry layers forming correctly")
    else:
        print("Mercury boundry layers formed incorrectly")

#simple case identificatoin
if x_f_w < L and x_t_w < L:
    print("Water flow developed by outlet - Simple Case Valid")
if x_f_eo < L and x_t_eo < L:
    print("Engine Oil flow developed by outlet - Simple Case Valid")
if x_f_m < L and x_t_m < L:
    print("Mercury flow developed by outlet - Simple Case Valid")

"""Intermdiate Values Printing"""
print("-"*50)
print("INTERMEDIATE VALUES PRINTING")
print("-"*50)
print(Tavg, "Average Temperature in Kelvin")
print(x_f_w, "Hydrodynamic distance - Water")
print(x_t_w, "Thermal Distance - Water")
print(x_f_eo, "Hydrodynamic distance - Engine Oil")
print(x_t_eo, "Thermal Distance - Engine Oil")
print(x_f_m, "Hydrodynamic distance - Mercury")
print(x_t_m, "Thermal Distance - Mercury")

"""SOLUTION PRINTING"""
print("-"*50)
print("SOLUTION")
print("-"*50)
print("h_water = ",h.item(water))
print("h_engine oil = ",h.item(engine_oil))
print("h_mercury = ",h.item(mercury))
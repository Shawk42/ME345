"""Assignment 5 - Problem 1"""

"""Givens"""
p = 1              #given pressure in [atm]
T = 25+273.15             #given temperature in [K]
V = 25             #given velocity in m/s
Re_cr = 5*(10**5)  #Critical reynolds number
L = .5

"""Table Inputs @300K """
nu = 15.89*(10**-6)      #nu of air at 300K

"""Calculations"""
Re = (V*L)/nu         #reynolds number
p = int((Re/Re_cr)*100)    # % calculation

"""Answer Logic"""
if Re < Re_cr:
    print("Flow is Laminar Re is less than Re_cr")
    print("Re is",p,"% of R_cr")
else:
    print("Flow is turbulent as Re is greater than Re_cr")
    print("Re is", p, "% of R_cr")
import math

rho = 1.225
g = 9.81

def lift(v, S, Cl):
    return 0.5 * rho * v**2 * S * Cl

def drag(v, S, Cd):
    return 0.5 * rho * v**2 * S * Cd

def weight(m):
    return m * g

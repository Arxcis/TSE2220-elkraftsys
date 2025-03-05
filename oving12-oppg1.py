"""
Øving 12 oppgave 1
"""
from math import acos, sqrt, pi
from cmath import polar
from jonas import printPolar, fromPolar, plotPolar

# 
# Innstillinger 
#
P3 = 2e6
cosfi3 = 0.85
fi3 = acos(cosfi3)
V3LL = 20e3

def r(km):
    return 0.3*km
def x(km):
    return 0.4j*km

L1km = 30
L2km = 15
ZL1 = r(L1km) + x(L1km)
ZL2 = r(L2km) + x(L2km)

#
# Beregninger
#

# I3
I3 = P3/(sqrt(3)*V3LL*cosfi3)
I3 *= fromPolar(1, 180*(-fi3/pi))

# I2
P2 = 3e6
cosfi2 = 0.9
fi2 = acos(cosfi2)
IL2 = I3
VL2 = IL2 * ZL2
VL2LL = VL2*sqrt(3)
V2LL = V3LL + VL2LL

V2LLmagnitude, vfi = polar(V2LL)
I2 = P2 / (sqrt(3)*V2LLmagnitude*cosfi2)
I2 *= fromPolar(1, 180*((-fi2 + vfi)/pi))

# I1
I1 = I2 + I3

# V1
VL1 = I1 * ZL1
VL1LL = sqrt(3) * VL1
V1LL = VL1LL + V2LL

#
# Presenter
#
printPolar(I3)
printPolar(ZL1, ZL2)
printPolar(V3LL, VL2LL, V2LL, I2)
plotPolar(I1, I2, I3)
printPolar(I1)
plotPolar(V1LL, V2LL, V3LL, VL1LL, VL2LL)


"""
Øving 12 oppgave 1
"""
from math import acos, sqrt, pi
from cmath import polar
from jonas import printPolar, fromPolar, plotPolar

# 
# Innstillinger 
#
P3_fff = 2e6
cosfi3 = 0.85
fi3 = acos(cosfi3)
V3_ff = 20e3

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
I3 = P3_fff/(sqrt(3)*V3_ff*cosfi3)
I3 *= fromPolar(1, 180*(-fi3/pi))

# I2
P2_fff = 3e6
cosfi2 = 0.9
fi2 = acos(cosfi2)
IL2 = I3
VL2_f = IL2 * ZL2
VL2_ff = VL2_f*sqrt(3)
V2_ff = V3_ff + VL2_ff

V2abs_ff, V2fi = polar(V2_ff)
I2 = P2_fff / (sqrt(3)*V2abs_ff*cosfi2)
I2 *= fromPolar(1, 180*((-fi2 + V2fi)/pi))

# I1
I1 = I2 + I3

# V1
VL1_f = I1 * ZL1
VL1_ff = sqrt(3) * VL1_f
V1_ff = V2_ff + VL1_ff

#
# Presenter
#
printPolar(ZL1, ZL2)
plotPolar(I1, I2, I3)
printPolar(I1, I2, I3)
printPolar(V1_ff, V2_ff, V3_ff, VL1_ff, VL2_ff)
plotPolar(V1_ff, V2_ff, V3_ff, VL1_ff, VL2_ff)


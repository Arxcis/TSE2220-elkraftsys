"""
Øving 12 oppgave 1
"""
from math import acos, sqrt, pi
from cmath import polar
from jonas import printPolar, fromPolar, plotPolar

# 
# Innstillinger 
#
P3fff = 2e6
cosfi3 = 0.85
fi3 = acos(cosfi3)
V3ff = 20e3

def r(km):
    return 0.3*km
def x(km):
    return 0.4j*km

L1km = 30
L2km = 15
Zlinje1 = r(L1km) + x(L1km)
ZL2 = r(L2km) + x(L2km)

#
# Beregninger
#

# I3
I3 = P3fff/(sqrt(3)*V3ff*cosfi3)
I3 *= fromPolar(1, 180*(-fi3/pi))

# I2
P2fff = 3e6
cosfi2 = 0.9
fi2 = acos(cosfi2)
IL2 = I3
Vlinje2f = IL2 * ZL2
Vlinje2ff = Vlinje2f*sqrt(3)
V2ff = V3ff + Vlinje2ff

V2absff, V2fi = polar(V2ff)
I2 = P2fff / (sqrt(3)*V2absff*cosfi2)
I2 *= fromPolar(1, 180*((-fi2 + V2fi)/pi))

# I1
I1 = I2 + I3

# V1
Vlinje1f = I1 * Zlinje1
Vlinje1ff = sqrt(3) * Vlinje1f
V1ff = V2ff + Vlinje1ff

#
# Presenter
#
printPolar(Zlinje1, ZL2)
plotPolar(I1, I2, I3)
printPolar(I1, I2, I3)
printPolar(V1ff, V2ff, V3ff, Vlinje1ff, Vlinje2ff)
plotPolar(V1ff, V2ff, V3ff, Vlinje1ff, Vlinje2ff)


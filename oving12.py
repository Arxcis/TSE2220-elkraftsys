from math import acos, sqrt

# Øving 12 oppgave 1
# 
# Prep
#
P3 = 2e6
cosfi3 = 0.85
fi3 = acos(cosfi3)
V3LL = 20e3


def r(km):
    return 0.3*km
def x(km):
    return 0.4j*km

L1 = 30
L2 = 15
RL1 = r(L1)
RL2 = r(L2)
XL1 = x(L1)
XL2 = x(L2)

ZL1 = RL1 + XL1
ZL2 = RL2 + XL2

from jonas import printPolar, fromPolar
printPolar(ZL1, ZL2)

#
# Beregninger
#
from math import pi
# I3
I3 = P3/(sqrt(3)*V3LL*cosfi3)
I3 *= fromPolar(1, 180*(-fi3/pi))
printPolar(I3)

# I2
P2 = 3e6
cosfi2 = 0.9
fi2 = acos(cosfi2)
IL2 = I3
VL2 = IL2 * ZL2
VL2LL = VL2*sqrt(3)
V2LL = V3LL + VL2LL

from cmath import polar
from math import pi

V2LLmagnitude, vfi = polar(V2LL)
I2 = P2 / (sqrt(3)*V2LLmagnitude*cosfi2)
I2 *= fromPolar(1, 180*((-fi2 + vfi)/pi))
printPolar(V3LL, VL2LL, V2LL, I2)


from jonas import plotPolar

# I1
I1 = I2 + I3
plotPolar(I1, I2, I3)
printPolar(I1)

# V1
VL1 = I1 * ZL1
VL1LL = sqrt(3) * VL1


V1LL = VL1LL + V2LL

plotPolar(V1LL, V2LL, V3LL, VL1LL, VL2LL)


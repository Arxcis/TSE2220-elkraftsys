"""
Øving 12 oppgave 2
"""

from jonas import fromPolar
from math import acos, pi

#
# Innstillinger
#

Linje = 90 # km
P2total = 5e6
cosfi2 = 0.88 # induktiv
fi2 = 180 * acos(cosfi2)/pi
V2ff = 66e3 # 66kV
V2f0 = V2ff/3**0.5
R = 0.1 * Linje
X = 0.5j * Linje
Cd = 8e-9 * Linje
fhz = 50
omega = 2*pi*fhz
ZC = fromPolar((Cd/2*omega)**-1, -90)

#
# Beregninger
#
I2f0 = P2total / (3**0.5 * cosfi2 * V2ff) * fromPolar(1, -fi2)

from jonas import printPolar, plotPolar

Z2 = V2f0 / I2f0

IC2f0 = V2f0 / ZC
Ilinje = I2f0 + IC2f0
Zlinje = R + X
Vlinjef0 = Ilinje*Zlinje

V1f0 = Vlinjef0 + V2f0
V1ff = V1f0 * 3**0.5

IC1f0 = V1f0 / ZC
I1f0 = Ilinje + IC1f0

#
# Presenter
#
printPolar(Z2, Zlinje, ZC)

printPolar(I2f0, IC2f0, Ilinje, IC1f0, I1f0)
plotPolar(I2f0, IC2f0, Ilinje, IC1f0, I1f0)
plotPolar(V1f0, V2f0, Vlinjef0)
printPolar(V2f0, Vlinjef0, V1f0)

printPolar(V2ff, V1ff)

"""
Øving 12 oppgave 2
"""

from jonas import fromPolar
from math import acos, pi, sqrt

#
# Innstillinger
#
linjekilometer = 90             # km
P2total = 5e6                   # 5MW
cosfi2 = 0.88                   # induktiv
fi2 = 180 * acos(cosfi2)/pi
V2ff = 66e3                     # 66kV
V2f0 = V2ff/sqrt(3)
Rlinje = 0.1 * linjekilometer   # r=0.1 ohm / km
XLlinje = 0.5j * linjekilometer # x=0.5 ohm / km
Zlinje = Rlinje + XLlinje
Cdrift = 8e-9 * linjekilometer  # Cd=8nF / km
fhz = 50                        # f=50hz
XClinje = (1j*Cdrift*2*pi*fhz)**-1

#
# Beregninger
#

# Ved punkt 2:
I2 = P2total / (sqrt(3) * cosfi2 * V2ff) * fromPolar(1, -fi2)
Z2 = V2f0 / I2

# På linje:
IC2 = V2f0 / XClinje / 2
Ilinje = I2 + IC2
Vlinjef0 = Ilinje*Zlinje

# Ved punkt 1:
V1f0 = Vlinjef0 + V2f0
V1ff = V1f0 * sqrt(3)
IC1 = V1f0 / XClinje / 2
I1 = Ilinje + IC1

#
# Presenter
#
from jonas import printPolar, plotPolar
printPolar(Z2, Zlinje, XClinje)
printPolar(I2, IC2, Ilinje, IC1, I1)
plotPolar(I2, IC2, Ilinje, IC1, I1)
plotPolar(V1f0, V2f0, Vlinjef0)
printPolar(V2f0, Vlinjef0, V1f0)
printPolar(V2ff, V1ff)

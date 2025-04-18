"""
Øving 12 oppgave 2
"""

from jonas import fromPolar
from math import acos, pi, sqrt

#
# Innstillinger
#
linjekm = 90                    # km
P2fff = 5e6                     # 5MW
cosfi2 = 0.88                   # induktiv
fi2 = 180 * acos(cosfi2)/pi
V2ff = 66e3                    # 66kV
V2f = V2ff/sqrt(3)
Rlinje = 0.1 * linjekm          # r=0.1 ohm / km
XLlinje = 0.5j * linjekm        # x=0.5 ohm / km
Zlinje = Rlinje + XLlinje
Cdrift = 8e-9 * linjekm         # Cd=8nF / km
fhz = 50                        # f=50hz
XClinje = (1j*Cdrift*2*pi*fhz)**-1

#
# Beregninger
#

# Ved punkt 2:
I2 = P2fff / (sqrt(3) * cosfi2 * V2ff) * fromPolar(1, -fi2)
Z2 = V2f / I2

# På linje:
IC2 = V2f / (XClinje / 2)
Ilinje = I2 + IC2
Vlinjef = Ilinje*Zlinje

# Ved punkt 1:
V1f = Vlinjef + V2f
V1ff = V1f * sqrt(3)
IC1 = V1f / (XClinje / 2)
I1 = Ilinje + IC1

#
# Presenter
#
from jonas import printPolar, plotPolar
printPolar(Z2, Zlinje, XClinje)
printPolar(I2, IC2, Ilinje, IC1, I1)
plotPolar(I2, IC2, Ilinje, IC1, I1)
printPolar(V2f, Vlinjef, V1f)
printPolar(V2ff, V1ff)
plotPolar(V2f, Vlinjef, V1f, V2ff, V1ff)

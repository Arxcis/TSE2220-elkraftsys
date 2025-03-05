"""
Øving 12 oppgave 2
"""

from jonas import fromPolar
from math import acos, pi

#
# Innstillinger
#
linjekilometer = 90 # km
P2total = 5e6
cosfi2 = 0.88 # induktiv
fi2 = 180 * acos(cosfi2)/pi
V2ff = 66e3 # 66kV
V2f0 = V2ff/3**0.5
Rlinje = 0.1 * linjekilometer   # r=0.1 ohm / km
XLlinje = 0.5j * linjekilometer # x=0.5 ohm / km
Zlinje = Rlinje + XLlinje
Cdrift = 8e-9 * linjekilometer  # Cd=8nF / km
fhz = 50                        # f=50hz
XClinje = (1j*Cdrift*2*pi*fhz)**-1

print(XClinje)
#
# Beregninger
#
I2 = P2total / (3**0.5 * cosfi2 * V2ff) * fromPolar(1, -fi2)

from jonas import printPolar, plotPolar

Z2 = V2f0 / I2

IC2 = V2f0 / XClinje / 2
Ilinje = I2 + IC2
Vlinjef0 = Ilinje*Zlinje

V1f0 = Vlinjef0 + V2f0
V1ff = V1f0 * 3**0.5

IC1 = V1f0 / XClinje / 2
I1 = Ilinje + IC1

#
# Presenter
#
printPolar(Z2, Zlinje, XClinje)

printPolar(I2, IC2, Ilinje, IC1, I1)
plotPolar(I2, IC2, Ilinje, IC1, I1)
plotPolar(V1f0, V2f0, Vlinjef0)
printPolar(V2f0, Vlinjef0, V1f0)

printPolar(V2ff, V1ff)

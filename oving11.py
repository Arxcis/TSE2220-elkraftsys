from jonas import fromPolar, printPolar
from math import acos, sin, pi, sqrt, tan

#
# Innstillinger 
#
V2ff = 66e3
cosfi = 0.8 # induktiv
fi = acos(cosfi)
sinfi = sin(fi)
tanfi = tan(fi)
fhz = 50

def r(km):
    return 0.25*km
def x(km):
    return 2*pi*fhz*(1.27e-3)*km

km = 60 
R = r(km)
X = x(km)
P2fff = 6e6

print("Prep:")
print("R: ", R)
print("X: ", X)
print("fi: ", (fi/pi)*180)
print("V2ff:", V2ff)
print(f"P2fff: {P2fff:.3g} [W]")

#
# Projeksjonsmetoden
#
print()
print("Projeksjonsmetoden:")
Zlinje = R + X

I2 = P2fff/(cosfi*V2ff) / sqrt(3)
Vlinjeff = sqrt(3) * I2*(R*cosfi + X*sinfi)
V1ff = V2ff + Vlinjeff

print(f"I2: {I2:.3g} [A]")
print(f"V2ff: {V2ff:.3g} [V]")
print(f"Vlinjeff: {Vlinjeff:.3g} [V]")
print(f"V1ff: {V1ff:.3g} [V]")

#
# Effektmetoden
#
print()
print("Effektmetoden:")

I2 = P2fff / (cosfi*V2ff) / sqrt(3)
P2f  = P2fff / 3
Q2f = P2f * tan(fi)
S2f = sqrt(P2f*P2f + Q2f*Q2f)
V2f = S2f / I2
V2ff = V2f * sqrt(3)

Plinjef = I2*I2*R
Qlinjef = I2*I2*X
Slinjef = sqrt(Plinjef**2 + Qlinjef**2)

Vlinjef = Slinjef / I2
Vlinjeff = sqrt(3) * Vlinjef

V1ff = V2ff + Vlinjeff

print()
print(f"V2ff: {V2ff:.3g} [V]")
print(f"Vlinjeff: {Vlinjeff:.3g} [V]")
print(f"V1ff: {V1ff:.3g} [V]")

#
# Kompleksmetoden
#
print()
print("Kompleksmetoden")

I2 = P2fff / (cosfi*V2ff) / sqrt(3)
VRlinjef = fromPolar(R*I2, -180*fi/pi)
VXlinjef = fromPolar(X*I2, -180*fi/pi + 90)
VZlinjef = VRlinjef + VXlinjef
VZlinjeff = sqrt(3) * VZlinjef

V1ff = V2ff + VZlinjeff
printPolar(V2ff, VRlinjef, VXlinjef, VZlinjef, VZlinjeff, V1ff)



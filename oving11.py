from jonas import fromPolar, printPolar
from math import acos, sin, pi, sqrt, tan
from cmath import polar

#
# Innstillinger 
#
V2 = 66e3
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
Ptotal = 6e6

print("Prep:")
print("R: ", R)
print("X: ", X)
print("fi: ", (fi/pi)*180)
print("V2:", V2)
print(f"P: {Ptotal:.3g} [W]")

#
# Projeksjonsmetoden
#
print()
print("Projeksjonsmetoden:")
Vlinje_linje,_ = polar(V2)
Zlinje = R + X

ILL = Ptotal/(cosfi*Vlinje_linje)
deltaVLL = ILL*(R*cosfi + X*sinfi)
V1LL = V2 + deltaVLL

print(f"ILL: {ILL:.3g} [A]")
print(f"V2LLL: {V2:.3g} [V]")
print(f"deltaVLL: {deltaVLL:.3g} [V]")
print(f"V1LL: {V1LL:.3g} [V]")

#
# Effektmetoden
#
print()
print("Effektmetoden:")

IL = ILL / sqrt(3)
P2 = Ptotal / 3
Q2 = P2 * tan(fi)
S2 = sqrt(P2*P2 + Q2*Q2)
V2 = S2 / IL
V2LL = V2 * sqrt(3)

deltaP = IL*IL*R
deltaQ = IL*IL*X
deltaS = sqrt(deltaP**2 + deltaQ**2)

deltaV = deltaS / IL
deltaVLL = sqrt(3) * deltaV

V1LL = V2LL + deltaVLL

print()
print(f"V2LL: {V2LL:.3g} [V]")
print(f"deltaVLL: {deltaVLL:.3g} [V]")
print(f"V1LL: {V1LL:.3g} [V]")

#
# Kompleksmetoden
#
print()
print("Kompleksmetoden")

V2LL = fromPolar(V2LL, 0)
VR = fromPolar(R*IL, -180*fi/pi)
VX = fromPolar(X*IL, -180*fi/pi + 90)
deltaVLL = sqrt(3) * (VR + VX)

V1LL = V2LL + deltaVLL
printPolar(V2LL, VR, VX, deltaVLL, V1LL)



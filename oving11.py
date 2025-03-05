from jonas import fromPolar, printPolar
from math import acos, sin, pi, sqrt, tan
from cmath import polar

#
# Innstillinger 
#
V2_ff = 66e3
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
P2_fff = 6e6

print("Prep:")
print("R: ", R)
print("X: ", X)
print("fi: ", (fi/pi)*180)
print("V2:", V2_ff)
print(f"P: {P2_fff:.3g} [W]")

#
# Projeksjonsmetoden
#
print()
print("Projeksjonsmetoden:")
Zlinje = R + X

I2 = P2_fff/(cosfi*V2_ff) / sqrt(3)
Vlinje_ff = sqrt(3) * I2*(R*cosfi + X*sinfi)
V1_ff = V2_ff + Vlinje_ff

print(f"I2: {I2:.3g} [A]")
print(f"V2_ff: {V2_ff:.3g} [V]")
print(f"Vlinje_ff: {Vlinje_ff:.3g} [V]")
print(f"V1_ff: {V1_ff:.3g} [V]")

#
# Effektmetoden
#
print()
print("Effektmetoden:")

I2 = P2_fff / (cosfi*V2_ff) / sqrt(3)
P2_f  = P2_fff / 3
Q2_f = P2_f * tan(fi)
S2_f = sqrt(P2_f*P2_f + Q2_f*Q2_f)
V2_f = S2_f / I2
V2_ff = V2_f * sqrt(3)

Plinje_f = I2*I2*R
Qlinje_f = I2*I2*X
Slinje_f = sqrt(Plinje_f**2 + Qlinje_f**2)

Vlinje_f = Slinje_f / I2
Vlinje_ff = sqrt(3) * Vlinje_f

V1_ff = V2_ff + Vlinje_ff

print()
print(f"V2_ff: {V2_ff:.3g} [V]")
print(f"Vlinje_ff: {Vlinje_ff:.3g} [V]")
print(f"V1_ff: {V1_ff:.3g} [V]")

#
# Kompleksmetoden
#
print()
print("Kompleksmetoden")

I2 = P2_fff / (cosfi*V2_ff) / sqrt(3)
VRlinje_f = fromPolar(R*I2, -180*fi/pi)
VXlinje_f = fromPolar(X*I2, -180*fi/pi + 90)
VZlinje_f = VRlinje_f + VXlinje_f
VZlinje_ff = sqrt(3) * VZlinje_f

V1_ff = V2_ff + VZlinje_ff
printPolar(V2_ff, VRlinje_f, VXlinje_f, VZlinje_f, VZlinje_ff, V1_ff)



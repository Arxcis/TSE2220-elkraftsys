from jonas import toPolar, fromPolar, parallell, printPolar

#
# Oppg 1
#
print("Oppg1:")
Vr  = fromPolar(110, 0)
Vs  = fromPolar(110, -120)
Vt  = fromPolar(110, 120)

Zl  = 5 - 2j
Z   = 10 + 8j
Zeq = Zl + Z

Ir = Vr/Zeq
Is = Vs/Zeq
It = Vt/Zeq

printPolar("Zeq", Zeq, "Ohm")
printPolar("Ir", Ir, "A")
printPolar("Is", Is, "A")
printPolar("It", It, "A")
print()

#
# Oppg 2
#

print("Oppg 2:")

Vr = fromPolar(130, 0)
Vs = fromPolar(130, -120)
Vt = fromPolar(130, 120)
Vrs = fromPolar(130*3**0.5, 0 + 30)
Vst = fromPolar(130*3**0.5, -120 + 30)
Vtr = fromPolar(130*3**0.5, 120 + 30)

printPolar("Vr", Vr, "V")
printPolar("Vs", Vs, "V")
printPolar("Vt", Vt, "V")
printPolar("Vrs", Vrs, "V")
printPolar("Vst", Vst, "V")
printPolar("Vtr", Vtr, "V")

Zl = 5 + 10j
Z  = 20 + 10j
Xc = -30j

print()
printPolar("Zl", Zl, "Ohm")
printPolar("Z", Z, "Ohm")
printPolar("Xc", Xc, "Ohm")

Zeq = Zl + parallell(Z, Xc/3)

print()
printPolar("Zeq", Zeq, "Ohm")

Ir = Vr/Zeq
Is = Vs/Zeq
It = Vt/Zeq

print()
printPolar("Ir", Ir, "A")
printPolar("Is", Is, "A")
printPolar("It", It, "A")

Ir_xc = Ir * (Z/parallell(Z, Xc/3))
Is_xc = Is * (Z/parallell(Z, Xc/3))
It_xc = It * (Z/parallell(Z, Xc/3))

print()
printPolar("Ir_xc", Ir_xc, "A")
printPolar("Is_xc", Is_xc, "A")
printPolar("It_xc", It_xc, "A")

Ir_z = Ir - Ir_xc
Is_z = Is - Is_xc
It_z = It - It_xc

print()
printPolar("Ir_z", Ir_z, "A")
printPolar("Is_z", Is_z, "A")
printPolar("It_z", It_z, "A")


Vr_z = Ir_z * Z
Vs_z = Is_z * Z
Vt_z = It_z * Z 

print()
printPolar("Vr_z", Vr_z, "V")
printPolar("Vs_z", Vs_z, "V")
printPolar("Vt_z", Vt_z, "V")



Sz = 3 * Z * (abs(Ir_z)**2)
Szl = 3 * Zl * (abs(Ir)**2)
Sxc = 3 * Xc * (abs(Ir_xc)**2)
S = Sz + Szl + Sxc

print()
printPolar("Sz",  Sz,  "VA")
printPolar("Szl", Szl, "VA")
printPolar("Sxc", Sxc, "VA")
printPolar("S",   S,   "VA")


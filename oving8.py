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

printPolar(Zeq, "Ohm")
printPolar(Ir, "A")
printPolar(Is, "A")
printPolar(It, "A")
print()

#
# Oppg 2
#

print("Oppg 2:")

# 2.1 Spenninger - fase og linje til linje
Vr = fromPolar(130, 0)
Vs = fromPolar(130, -120)
Vt = fromPolar(130, 120)
Vrs = fromPolar(130*3**0.5, 0 + 30)
Vst = fromPolar(130*3**0.5, -120 + 30)
Vtr = fromPolar(130*3**0.5, 120 + 30)

printPolar(Vr)
printPolar(Vs)
printPolar(Vt)
printPolar(Vr)
printPolar(Vs)
printPolar(Vt)


# 2.2 Zeq (Ztotal)
Zl = 5 + 10j
Z  = 20 + 10j
Xc = -30j
Zeq = Zl + parallell(Z, Xc/3)

print()
printPolar(Zl)
printPolar(Z)
printPolar(Xc)
printPolar(Zeq)


# 2.3 Linjestrømmer
Ir = Vr/Zeq
Is = Vs/Zeq
It = Vt/Zeq

print()
printPolar(Ir)
printPolar(Is)
printPolar(It)


# 2.4 Kondensatorstrømmer
Ir_xc = Ir * (Z/parallell(Z, Xc/3))
Is_xc = Is * (Z/parallell(Z, Xc/3))
It_xc = It * (Z/parallell(Z, Xc/3))

print()
printPolar(Ir_xc)
printPolar(Is_xc)
printPolar(It_xc)


# 2.5 Fasestrømmer
Ir_z = Ir - Ir_xc
Is_z = Is - Is_xc
It_z = It - It_xc

print()
printPolar(Ir_z)
printPolar(Is_z)
printPolar(It_z)


# 2.6 Fasespenninger
Vr_z = Ir_z * Z
Vs_z = Is_z * Z
Vt_z = It_z * Z 

print()
printPolar(Vr_z)
printPolar(Vs_z)
printPolar(Vt_z)


# 2.7 Total aktiv og reaktiv effekt i last, kondensatorer og linjeimpedanser
Sz = 3 * Z * (abs(Ir_z)**2)
Szl = 3 * Zl * (abs(Ir)**2)
Sxc = 3 * Xc * (abs(Ir_xc)**2)
S = Sz + Szl + Sxc

print()
printPolar(Sz)
printPolar(Szl)
printPolar(Sxc)
printPolar(S)

print()


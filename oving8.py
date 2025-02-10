from jonas import fromPolar, parallell, printPolar, printOppg, plotPolar

#
# Oppg 1
#
printOppg(1)
Vr  = fromPolar(110, 0)
Vs  = fromPolar(110, -120)
Vt  = fromPolar(110, 120)

printPolar(Vr, Vs, Vt)

Zl  = 5 - 2j
Z   = 10 + 8j
Zeq = Zl + Z

Ir = Vr/Zeq
Is = Vs/Zeq
It = Vt/Zeq

printPolar(Zeq, Ir, Is, It)

#
# Oppg 2
#
printOppg(2)

# 2.1 Spenninger - fase og linje til linje
Vr = fromPolar(130, 0)
Vs = fromPolar(130, -120)
Vt = fromPolar(130, 120)
Vrs = fromPolar(130*3**0.5, 0 + 30)
Vst = fromPolar(130*3**0.5, -120 + 30)
Vtr = fromPolar(130*3**0.5, 120 + 30)

printPolar(Vr, Vs, Vt, Vrs, Vst, Vtr)
plotPolar(Vr, Vs, Vt, Vrs, Vst, Vtr)

# 2.2 Zeq (Ztotal)
Zl = 5 + 10j
Z  = 20 + 10j
Xc = -30j
Zeq = Zl + parallell(Z, Xc/3)

printPolar(Zl, Z, Xc, Zeq)


# 2.3 Linjestrømmer
Ir = Vr/Zeq
Is = Vs/Zeq
It = Vt/Zeq

printPolar(Ir, Is, It)

from math import sqrt

# 2.4 Kondensatorstrømmer
Idelingsfaktor = Z/((Xc/3) + Z)
Ir_xc_star = Ir * Idelingsfaktor 
Ir_xc_delta = Ir_xc_star * fromPolar(1/sqrt(3), 30)

Is_xc_star = Is * Idelingsfaktor
Is_xc_delta = Is_xc_star * fromPolar(1/sqrt(3), 30)

It_xc_star = It * Idelingsfaktor
It_xc_delta = It_xc_star * fromPolar(1/sqrt(3), 30)

printPolar(Ir_xc_star, Is_xc_star, It_xc_star, Ir_xc_delta, Is_xc_delta, It_xc_delta)
plotPolar(Ir_xc_star, Is_xc_star, It_xc_star, Ir_xc_delta, Is_xc_delta, It_xc_delta)

# 2.5 Fasestrømmer

Idelingsfaktor = (Xc/3)/((Xc/3) + Z)
Ir_z = Ir * Idelingsfaktor 
Is_z = Is * Idelingsfaktor
It_z = It * Idelingsfaktor 

printPolar(Ir_z, Is_z, It_z)


plotPolar(Ir, Is, It, Ir_xc_star, Is_xc_star, It_xc_star, Ir_z, Is_z, It_z)

# 2.6 Fasespenninger
Vr_z = Ir_z * Z
Vs_z = Is_z * Z
Vt_z = It_z * Z 

printPolar(Vr_z, Vs_z, Vt_z)


# 2.7 Total aktiv og reaktiv effekt i last, kondensatorer og linjeimpedanser
Sz = 3 * Z * (abs(Ir_z)**2)
Szl = 3 * Zl * (abs(Ir)**2)
Sxc = 3 * Xc * (abs(Ir_xc_delta)**2)
S = Sz + Szl + Sxc

printPolar(Sz, Szl, Sxc, S)



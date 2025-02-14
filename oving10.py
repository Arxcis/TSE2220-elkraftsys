
from jonas import fromPolar, printPolar, plotPolar, findV0, printOppg

#
# Oppg 1
#
printOppg(1)
Zl = 2 + 4j

Zr = 20 + 10j + Zl
Zs = 30 + 5j + Zl
Zt = 20 - 20j + Zl

Vr = 3000
Vs = fromPolar(3000, -120)
Vt = fromPolar(3000, 120)

V0 = findV0(Zr, Zs, Zt, Vr, Vs, Vt)

printPolar(Zr, Zs, Zt)
printPolar(Vr, Vs, Vt, V0)

Vrdelta = Vr - V0
Vsdelta = Vs - V0
Vtdelta = Vt - V0

printPolar(Vrdelta, Vsdelta, Vtdelta)

Ir = Vrdelta/Zr
Is = Vsdelta/Zs
It = Vtdelta/Zt

printPolar(Ir, Is, It)

Vtr = Vt - Vr
Vts = Vt - Vs

printPolar(Vtr, Vts)

Str = Vtr * (It - Ir).conjugate()
Sts = Vts * (It - Is).conjugate()
S = Str + Sts

printPolar(Str, Sts, S)
plotPolar(Str, Sts, S)

#
# Oppg 2
#
printOppg(2)

Vrs = 208
Vst = fromPolar(208, -120)
Vtr = fromPolar(208, +120)

Zrs = 10
Zst = 15 + 20j
Ztr = 12 - 12j

# a) Fasestrømmene
Irs = Vrs/Zrs
Ist = Vst/Zst
Itr = Vtr/Ztr

printPolar(Irs, Ist, Itr)

# b) Linjestrømmene - Kirchofs current
Ir = Irs - Itr
Is = Ist - Irs
It = Itr - Ist

# c) Effekt
Str = Vtr * Itr.conjugate()
Sts = (-Vst) * (-Ist).conjugate()
S = Str + Sts

printPolar(Str, Sts, S)
plotPolar(Str, Sts, S)


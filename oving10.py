
from jonas import fromPolar, printPolar, plotPolar, findV0, printOppg

#
# Oppg 1
#
printOppg(1)

# Innstillinger
Zl = 2 + 4j
Z2r = 20 + 10j
Z2s = 30 + 5j
Z2t = 20 - 20j
Zr = Z2r + Zl
Zs = Z2s + Zl
Zt = Z2t + Zl
V1r = 3000
V1s = fromPolar(3000, -120)
V1t = fromPolar(3000, 120)

printPolar(Zr, Zs, Zt, V1r, V1s, V1t)

# a) Find V2
V0 = findV0(Zr, Zs, Zt, V1r, V1s, V1t)
V1r_delta = V1r - V0
V1s_delta = V1s - V0
V1t_delta = V1t - V0

printPolar(V0, V1r_delta, V1s_delta, V1t_delta)
plotPolar(V0, V1r, V1s, V1t, V1r_delta, V1s_delta, V1t_delta) 

# b) Finn Ifase = Ilinje i Y-kobling.
Ir = V1r_delta/Zr
Is = V1s_delta/Zs
It = V1t_delta/Zt

printPolar(Ir, Is, It)

# c) Bruk 2-wattmetermetode til å finne P og Q
V2r = Ir * Z2r
V2s = Is * Z2s
V2t = It * Z2t

V2rt = V2r - V2t
V2st = V2s - V2t 
Srt = V2rt * Ir.conjugate()
Sst = V2st * Is.conjugate()
S = Srt + Sst

printPolar(V2rt, V2st, Srt, Sst, S)
plotPolar(Srt, Sst, S)

# d) Bruk 3-wattmetermetode
Sr = V2r * Ir.conjugate()
Ss = V2s * Is.conjugate()
St = V2t * It.conjugate()
S = Sr + Ss + St

printPolar(Sr, Ss, St, S) 
plotPolar(Sr, Ss, St, S)

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


from jonas import parallell, printOppg

Sk = 30e9    # 30GVA
Sbase = 50e6 # 50MVA


printOppg(3)

# Oppgave a)
Xk = Sbase / Sk
ST1 = 80e6
ST2 = 100e6

XT1 = 0.10 * (Sbase / 80e6)
XT2 = 0.08 * (Sbase / 100e6)

XC = Xk + parallell(XT1, XT2)

SkC = Sbase / XC

print(f"a) SkC: {SkC:.3g}")

#
# Oppgave b)
#

Vlinje1 = 132e3  # 132kV
Zbaselinje = (Vlinje1)**2 / Sbase

Xlinje1 = 0.4 * 50 #km
Xlinje1 = Xlinje1 / Zbaselinje # pu

XG = .20 * (Sbase / 50e6)
XT3 = .08 * (Sbase / 50e6)

XA = parallell(XG + XT3, XC + Xlinje1)

SkA = Sbase / XA

print(f"b) SkA: {SkA:.3g}")

#
# Oppgave C)
#

Xlinje2 = 0.4 * 30 # km
Xlinje2 = Xlinje2 / Zbaselinje # pu

XT4 = 0.075 * (Sbase / 80e6)
XT5 = 0.10  * (Sbase / 60e6)

# Delta -> stjerne
Xstarsum = XG + XT3 + Xlinje1 + XC
XstarA = (XG + XT3)*XC / Xstarsum
XstarB = XC*Xlinje1 / Xstarsum
XstarC = Xlinje1*(XG+XT3) / Xstarsum

XB = XstarA + parallell(XstarB + Xlinje2 + XT5, XstarC + XT4)

SkB = Sbase / XB

print(f"c) SkB: {SkB:.3g}")

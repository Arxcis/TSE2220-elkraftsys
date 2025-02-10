from jonas import printOppg, fromPolar, printPolar, plotPolar, parallell

#
# Oppg 1
#
printOppg(1)
Vrs = fromPolar(100, 10)
Vtr = Vrs * fromPolar(1, 120)
Vst = Vtr * fromPolar(1, 120)

Zdelta = 8 + 4j

Irs = Vrs / Zdelta
Itr = Vtr / Zdelta
Ist = Vst / Zdelta

Ir = Irs * fromPolar(3**0.5, -30)
Is = Ir * fromPolar(1,-120)
It = Is * fromPolar(1,-120)

printPolar(Vrs, Vtr, Vst, Irs, Itr, Ist, Ir, Is, It)
plotPolar(Vrs, Vtr, Vst)
plotPolar(Irs, Itr, Ist, Ir, Is, It)

#
# Oppg 2
#
printOppg(2)

Vrs = fromPolar(250,0)
Vr = Vrs / fromPolar(3**0.5, 30)

Z = 30 + 15j
Zl = 5 + 10j
Zxc = -10j

Za = parallell(Zxc, Z/3)
Zb = Zl
Ztot = parallell(Zxc, Za+Zb)

printPolar(Za, Zb, Ztot)

Irs = Vrs/Ztot
Ir = Vr/Ztot
Irc1 = Ir * ((Za + Zb)/(-10j+Za+Zb))
Irzl = Ir * ((-10j)/(-10j+Za+Zb))
Irc2 = Irzl * ((Z/3)/(-10j+(Z/3)))
Irz  = Irzl * ((-10j)/(-10j+(Z/3)))
Irzdelta = Irz / (fromPolar(3**0.5,-30))

printPolar(Ir, Irc1, Irzl, Irc2, Irz, Irzdelta)

plotPolar(Irs, Ir, Irc1, Irzl, Irc2, Irz, Irzdelta)


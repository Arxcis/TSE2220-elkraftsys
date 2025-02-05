from jonas import fromPolar, printPolar, findV0, printOppg


#
# Oppg 1
#
printOppg(1)

Vr = fromPolar(500)
Vs = fromPolar(500, -120)
Vt = fromPolar(500, 120)

Zl = fromPolar(5, 0)
Zr = Zl + fromPolar(10, 30)
Zs = Zl + fromPolar(10, 45)
Zt = Zl + fromPolar(20, 60)

V0 = findV0(Zr, Zs, Zt, Vr, Vs, Vt)

printPolar(Vr, Vs, Vt, Zl, Zr, Zs, Zt, V0)

#
# Oppg 2
#
printOppg(2)
Vr = fromPolar(3000)
Vs = fromPolar(3000, -120)
Vt = fromPolar(3000, 120)

Zl = 2 + 4j
Zr = Zl + 20 + 10j
Zs = Zl + 30 + 5j
Zt = Zl + 20 - 20j

V0 = findV0(Zr, Zs, Zt, Vr, Vs, Vt)

printPolar(Vr, Vs, Vt, Zl, Zr, Zs, Zt, V0)


#
# Oppg 3 
#
printOppg(3)

Vr = fromPolar(5000)
Vs = fromPolar(5000, -120)
Vt = fromPolar(5000, 120)

Zl = 3 + 9j
Zr = Zl + 20 - 5j 
Zs = Zl + 20 + 20j 
Zt = Zl + 30 - 5j 

V0 = findV0(Zr, Zs, Zt, Vr, Vs, Vt)

printPolar(Vr, Vs, Vt, Zl, Zr, Zs, Zt, V0)


#
# Oppg 5 
#
printOppg(5)

Ur = fromPolar(220)
Us = fromPolar(220, -120)
Ut = fromPolar(220, 120)

U0 = (Ur/2 + Us + Ut) / (5/2) 

Uu = Ur - U0
Uv = Us - U0
Uw = Ut - U0

printPolar(Ur, Us, Ut, U0, Uu, Uv, Uw)

S = 5000 + 4000j
Z = (((Uu**2)/S).conjugate()) / 2

printPolar(S, Z)

I1 = Uu / (2*Z)
I2 = Uv / Z
I3 = Uw / Z

printPolar(I1, I2, I3)


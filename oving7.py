from jonas import Polar, Polarstr, findV0


#
# Oppg 1
#
Vr = Polar(500)
Vs = Polar(500, -120)
Vt = Polar(500, 120)

Zl = Polar(5, 0)
Zr = Zl + Polar(10, 30)
Zs = Zl + Polar(10, 45)
Zt = Zl + Polar(20, 60)

V0 = findV0(Zr, Zs, Zt, Vr, Vs, Vt)

print("Oppg1: V0", Polarstr(V0,"V"))


#
# Oppg 2
#
Vr = Polar(3000)
Vs = Polar(3000, -120)
Vt = Polar(3000, 120)

Zl = 2 + 4j
Zr = Zl + 20 + 10j
Zs = Zl + 30 + 5j
Zt = Zl + 20 - 20j

V0 = findV0(Zr, Zs, Zt, Vr, Vs, Vt)

print("Oppg2: V0", Polarstr(V0,"V"))

#
# Oppg 3 
#
Vr = Polar(5000)
Vs = Polar(5000, -120)
Vt = Polar(5000, 120)

Zl = 3 + 9j
Zr = Zl + 20 - 5j 
Zs = Zl + 20 + 20j 
Zt = Zl + 30 - 5j 

V0 = findV0(Zr, Zs, Zt, Vr, Vs, Vt)

print("Oppg3: V0", Polarstr(V0,"V"))


#
# Oppg 5 
#
Ur = Polar(220)
Us = Polar(220, -120)
Ut = Polar(220, 120)

U0 = (Ur/2 + Us + Ut) / (5/2) 

Uu = Ur - U0
Uv = Us - U0
Uw = Ut - U0

print("Oppg5:")
print("    Ur", Polarstr(Ur, "V"))
print("    Us", Polarstr(Us, "V"))
print("    Ut", Polarstr(Ut, "V"))
print()
print("    U0", Polarstr(U0, "V"))
print("    Uu", Polarstr(Uu, "V"))
print("    Uv", Polarstr(Uv, "V"))
print("    Uw", Polarstr(Uw, "V"))
print()

S = 5000 + 4000j
Z = (((Uu**2)/S).conjugate()) / 2

print("     Z  ", Polarstr(Z, "Ω"))
print("     R + jX", Z, "Ω")
print()

I1 = Uu / (2*Z)
I2 = Uv / Z
I3 = Uw / Z

print("    I1", Polarstr(I1, "A"))
print("    I2", Polarstr(I2, "A"))
print("    I3", Polarstr(I3, "A"))


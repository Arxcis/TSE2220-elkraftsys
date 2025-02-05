from jonas import toPolar, fromPolar

#
# Oppg 1
#
Vr  = fromPolar(110, 0)
Vs  = fromPolar(110, -120)
Vt  = fromPolar(110, 120)

Zl  = 5 - 2j
Z   = 10 + 8j
Zeq = Zl + Z

Ir = Vr/Zeq
Is = Vs/Zeq
It = Vt/Zeq

print("Oppg1:")
print("Zeq:", toPolar(Zeq))
print("Ir: ", toPolar(Ir))
print("Is: ", toPolar(Is))
print("It: ", toPolar(It))



#
# Oppg 2
#



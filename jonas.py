from cmath import rect, polar, pi

def fromPolar(magnitude, degrees = 0, unit = ""):
    radians = (degrees/180) * pi
    r = rect(magnitude, radians)
    return r 

def toPolar(rect, unit = ""):
    magnitude, radians = polar(rect)
    degrees = (radians/pi) * 180
    return f"{magnitude:>8.1f}{unit}∠({degrees:>.1f}°){'':>6} or {rect.real:.1f}+j({rect.imag:.1f})"

def findV0(Zr, Zs, Zt, Vr, Vs, Vt):
    Yr, Ys, Yt = Zr**-1, Zs**-1, Zt**-1
    V0 = (Yr*Vr + Ys*Vs + Yt*Vt) / (Yr + Ys + Yt)
    return V0


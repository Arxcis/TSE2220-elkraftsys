from cmath import rect, polar, pi

def fromPolar(magnitude, degrees = 0, unit = ""):
    radians = (degrees/180) * pi
    r = rect(magnitude, radians)
    return r 

def toPolar(rect, unit = ""):
    magnitude, radians = polar(rect)
    degrees = (radians/pi) * 180

    if unit == "Ohm":
        unit = "Ω"

    if unit == "VA":
        real_unit = "W"
        imag_unit = "VAr"
    else:
        real_unit = unit
        imag_unit = unit

    polarstr = f"{magnitude:>8.3g}{unit:<3}∠({degrees:>5.3g}°)" 
    rectstr = f"{rect.real:>12.3g}{real_unit} {rect.imag:>9.3g}j{imag_unit}"

    return f"{polarstr:<16}   | {rectstr:<16}"


def printOppg(number):
    print()
    print( "|------------------------------------------------------------")
    print(f"| Oppg {number}:")
    print( "|------------------------------------------------------------")

from inspect import currentframe

def printPolar(*rects):
    print()
    for rect in rects:
        # 1. Find variable name
        frame = currentframe().f_back # Get callers frame
        name = None
        for nam, val in frame.f_locals.items():
            if val is rect:
                name = nam
                break
        
        # 2. Select unit based on first letter in variable name
        if name[0] in ["V", "U"]:
            unit = "V"
        elif name[0] in ["I"]:
            unit = "A"
        elif name[0] in ["Z", "R", "X"]:
            unit = "Ω"
        elif name[0] in ["S"]:
            unit = "VA"
        elif name[0] in ["P"]:
            unit = "W"
        elif name[0] in ["Q"]:
            unit = "VAr"

        print(f"{name:<10}", toPolar(rect, unit))

import numpy as np
import matplotlib.pyplot as plt


def plotPolar(*rects):
    # Define complex numbers

    # Extract real and imaginary parts
    magnitudes = [abs(z) for z in rects]
    angles = [np.angle(z) for z in rects]

    # Create plot
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    ax.axhline(0, color='gray', linewidth=0.5)
    ax.axvline(0, color='gray', linewidth=0.5)
    
    # Plot arrows from origin
    names = []
    for r, fi, z in zip(magnitudes, angles, rects):
        # 1. Find variable name
        frame = currentframe().f_back # Get callers frame
        name = None
        for nam, val in frame.f_locals.items():
            if val is z:
                name = nam
                break

        names.append(name)

        # 2. Plot quiver
        ax.quiver(fi, 0, 0, r, angles='xy', scale_units='xy', scale=1, color='b')
        # 3. Add label at the tip of the arrow
        ax.text(fi, r, f'{name}', fontsize=12, ha='left', va='bottom')

    # Set limits
    limit = max((abs(rect) for rect in rects))
    ax.set_ylim(0, limit)   # fi-limit
    ax.set_xticklabels([]) # Hide labels
    
    # Set title and save to file 
    title = "-".join((f"{nam}" for nam in names))
    #ax.set_title(title)
    plt.savefig(title+".png", dpi=300)


def findV0(Zr, Zs, Zt, Vr, Vs, Vt):
    Yr, Ys, Yt = Zr**-1, Zs**-1, Zt**-1
    V0 = (Yr*Vr + Ys*Vs + Yt*Vt) / (Yr + Ys + Yt)
    return V0

def parallell(*Z):
    admittances = (1/z for z in Z)
    parallell_impedance = sum(admittances)**-1

    return parallell_impedance



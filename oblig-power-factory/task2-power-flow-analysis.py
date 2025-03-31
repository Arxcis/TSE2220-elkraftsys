
def main():
    Sbase_40MVA = 40e6
    
    #
    # Step 1: Generate the Ybus matrix for the whole network with 8 buses (8x8 matrix)
    #
    print_title("Y admittance matrix")
   
    y_trafo = lambda s, z: (z * (Sbase_40MVA/s))**-1

    YT1, YT2, YT3, YT4 = y_trafo(z=0.03j, s=40.0e6),\
                         y_trafo(z=0.06j, s= 0.4e6),\
                         y_trafo(z=0.06j, s= 0.7e6),\
                         y_trafo(z=0.06j, s= 2.0e6)
    

    y_cable = lambda km, Vbase: (0.11*km/(Vbase**2/Sbase_40MVA) \
                              + 0.20j*km/(Vbase**2/Sbase_40MVA))**-1

    YC1, YC2, YC3 = y_cable(km=0.2, Vbase=11e3),\
                    y_cable(km=2.0, Vbase=11e3),\
                    y_cable(km=1.0, Vbase=11e3)
    

    from numpy import array,abs
    Y = array([
    # Bus   1,         2,             3,    4,              5,    6,         7,    8
        [+YT1,      -YT1,             0,    0,              0,    0,         0,    0], # 1. bus
        [-YT1, (YT1+YC1),          -YC1,    0,              0,    0,         0,    0], # 2. bus
        [   0,      -YC1, (YC1+YT2+YC2), -YT2,           -YC2,    0,         0,    0], # 3. etc...
        [   0,         0,          -YT2, +YT2,              0,    0,         0,    0], # 4.
        [   0,         0,          -YC2,    0,  (YC2+YT3+YC3), -YT3,      -YC3,    0], # 5.
        [   0,         0,             0,    0,           -YT3, +YT3,         0,    0], # 6.
        [   0,         0,             0,    0,           -YC3,    0, (YC3+YT4), -YT4], # 7.
        [   0,         0,             0,    0,              0,    0,      -YT4, +YT4], # 8.
    ])
    for y in Y:
        print(",".join(f"{y:>10.3g}" for y in abs(y)))

    #
    # Step 2: Setup the loads for each bus. Could add generators as well here if present, but with opposite sign.
    #
        
    from math import sin, acos

    Sload = lambda p, cosfi: (p + (1j * p * sin(acos(cosfi)) / cosfi))/Sbase_40MVA
    Sin = array([
        0,
        0,
        0,
        -Sload(p=150e3, cosfi=0.96),
        0,
        -Sload(p=400e3, cosfi=0.96),
        0,
        -Sload(p=1500e3, cosfi=0.96),
    ])
    
    print_title("Bus loads")
    print_bus_header("[VA]")
    print_bus_values(0, Sin*Sbase_40MVA)

    #
    # Step 3: Use Gauss-Siedel method to numerically approximate V
    #
    N = 10_000

    print_title(f"Bus voltages simulation ({N} iterations)")
    print_bus_header("[V]")
    
    from numpy import conjugate, abs, ones, sqrt
    
    Vbases = array([132e3, 11e3, 11e3, 230, 11e3, 230, 11e3, 230])

    V = ones(8)
    Yii = array([Y[i][i] for i in range(8)])

    for i in range(N):
        I = conjugate(Sin) / conjugate(V)
        
        YVij = Y.dot(V)
        YVii = Yii*V

        V = (1/Yii) * (I - YVij + YVii)

        # Always reset slack-bus to 1pu
        V[0] = 1
        
        #print_bus_values(i, V*Vbases)

    #
    # Step 4: Calculate total power flows
    #
    Ibases = Sbase_40MVA / (V*Vbases *sqrt(3))
    I = Y.dot(V) * Ibases
    S = conjugate(I)*V*Vbases*sqrt(3)

    # Print results
    print_title("Bus power flows")
    print_bus_header("")
    print_bus_values_real("Pin[W]", Sin*Sbase_40MVA)
    print_bus_values_imag("Qin[VAr]", Sin*Sbase_40MVA)
    print_bus_values("Videa[V]", Vbases)
    print_bus_values("Vsimu[V]", V*Vbases)
    print_bus_values_real("Ireal[A]", I)
    print_bus_values_imag("Iimag[A]", I)
    print_bus_values_real("P[W]", S) 
    print_bus_values_imag("Q[VAr]", S)


def print_title(title):
        print(f"""\n\n
{title}
-----------------------------------------------------------
""")


def print_bus_header(unit):

    label = f"{" ":>11}"
    print(f" {label} | {" | ".join(f"{f"Bus{i+1} {unit}":<9}" for i in range(8))}")
    print(f" {label} | {" | ".join(f"{f"---------":<9}" for _ in range(8))}")


def print_bus_values(label, values):
    label = f"{label:>11}"
    values = " | ".join(f"{v:>9.4g}" for v in abs(values))
    print(f" {label} | {values}")

def print_bus_values_real(label, values):
    label = f"{label:>11}"
    values = " | ".join(f"{v.real:>9.3g}" if abs(v.real) > 1e-6 else f"{0:>9.3g}" for v in values)
    print(f" {label} | {values}")

def print_bus_values_imag(label, values):
    label = f"{label:>11}"
    values = " | ".join(f"{v.imag:>9.3g}" if abs(v.imag) > 1e-6 else f"{0:>9.3g}" for v in values)
    print(f" {label} | {values}")



if __name__ == "__main__":
    main()

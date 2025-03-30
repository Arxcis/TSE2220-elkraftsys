
def main():
    print("main()")
    Sbase_40MVA = 40e6
    
    #
    # Step 1: Generate the Ybus matrix for the whole network with 8 buses (8x8 matrix)
    #
    y_trafo = lambda s, z: (z * (Sbase_40MVA/s))**-1
    YT1, YT2, YT3, YT4 = y_trafo(z=0.03j, s=40.0e6),\
                         y_trafo(z=0.06j, s= 0.4e6),\
                         y_trafo(z=0.06j, s= 0.7e6),\
                         y_trafo(z=0.06j, s= 2.0e6)
    

    y_cable = lambda km, Vbase: (0.11*km/(Vbase**2/Sbase_40MVA) + 0.20j*km/(Vbase**2/Sbase_40MVA))**-1
    YC1, YC2, YC3 = y_cable(km=0.2, Vbase=132e3),\
                    y_cable(km=2.0, Vbase=11e3),\
                    y_cable(km=1.0, Vbase=11e3)
    
    from numpy import array,abs
    Y = array([
    # Bus   1,         2,             3,    4,              5,    6,         7,    8
        [+YT1,      -YT1,             0,    0,              0,    0,         0,    0], # 1
        [-YT1, (YT1+YC1),          -YC1,    0,              0,    0,         0,    0], # 2
        [   0,      -YC1, (YC1+YT2+YC2), -YT2,           -YC2,    0,         0,    0], # 3
        [   0,         0,          -YT2, +YT2,              0,    0,         0,    0], # 4
        [   0,         0,          -YC2,    0,  (YC2+YT3+YC3), -YT3,       YC3,    0], # 5
        [   0,         0,             0,    0,           -YT3, +YT3,         0,    0], # 6
        [   0,         0,             0,    0,           -YC3,    0, (YC3+YT4), -YT4], # 7
        [   0,         0,             0,    0,              0,    0,      -YT4, +YT4], # 8
    ])
    for y in Y:
        print(",".join(f"{y:>10.3g}" for y in abs(y)))

    #
    # Step 2: Setup the loads for each bus. Could add generators as well here if present, but with opposite sign.
    #
    from math import sin, acos

    Sload = lambda p, cosfi: (p + (1j * p * sin(acos(cosfi)) / cosfi))/Sbase_40MVA
    S = [
        0,
        0,
        0,
        -Sload(p=150e3, cosfi=0.96),
        0,\
        -Sload(p=400e3, cosfi=0.96),
        0,
        -Sload(p=150e3, cosfi=0.96),
    ]
    #print(",  ".join(f"{v:>10.3g}" for v in abs(S)))

    #
    # Step 3: Use Gauss-Siedel method to numerically approximate V
    #
    from numpy import conjugate, abs, ones
    
    Vbases = array([132e3, 11e3, 11e3, 230, 11e3, 230, 11e3, 230])
    V = ones(8)
    Yii = array([Y[i][i] for i in range(len(Y))])

    for _ in range(100000):

        I = conjugate(S) / conjugate(V)
        YVsum = Y @ V

        #print(",".join(f"{v:>10.3g}" for v in abs(YVsum)))

        V = (1/Yii) * (I - (YVsum - (Yii*V)))

        # Always reset slack-bus to 1pu
        V[0] = 1

        #print(",  ".join(f"{v:>10.3g}" for v in abs(V*Vbases)))

if __name__ == "__main__":
    main()

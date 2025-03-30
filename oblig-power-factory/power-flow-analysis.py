from dataclasses import dataclass

@dataclass
class Trafo:
    S: int       # Rated power
    X_pu: float  # short-circuit impedance per unit


def main():
    print("main()")
    Sbase = 40e6 # 40MVA
    Vbase = 132e3 # 132kV
    Zbase = Vbase**2 / Sbase
    

    #
    # Step 1: Generate the Ybus matrix for the whole network with 8 buses (8x8 matrix)
    #
    Ytrafo = lambda s, z: (z * (Sbase/s))**-1
    YT1, YT2, YT3, YT4 = Ytrafo(z=0.03j, s=40.0e6),\
                         Ytrafo(z=0.06j, s= 0.4e6),\
                         Ytrafo(z=0.06j, s= 0.7e6),\
                         Ytrafo(z=0.06j, s= 2.0e6)


    Ycable = lambda km: ((0.11*km + 0.20j*km)/Zbase)**-1
    YC1, YC2, YC3 = Ycable(km=0.2),\
                    Ycable(km=2.0),\
                    Ycable(km=1.0)
    
    from numpy import array
    Ypu = array([
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
    
    Ydiag_pu= array([
        +YT1,
        +YT1+YC1,
        +YC1+YT2+YC2,
        +YT2,
        +YC2+YT3+YC3,
        +YT3,
        +YC3+YT4,
        +YT4
    ])
   
    #
    # Step 2: Set all initial 8 bus voltages to 1pu
    #
    Vpu = array([1, 1, 1, 1, 1, 1, 1, 1])

    #
    # Step 3: Setup the loads for each bus. Could add generators as well here if present, but with opposite sign.
    #
    from math import sin, acos

    Sload = lambda p, cosfi: -(p + (1j*p/cosfi)*sin(acos(cosfi))) / Sbase
    Spu = [
        0,\
        0,\
        0,\
        Sload(p=150e3, cosfi=0.96),\
        0,\
        Sload(p=400e3, cosfi=0.96),\
        0,\
        Sload(p=1500e3, cosfi=0.96),\
    ]



    print(Vpu)


if __name__ == "__main__":
    main()

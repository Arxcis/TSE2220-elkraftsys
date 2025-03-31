
def main():
    #
    # Step 0: Set network Sbase
    #
    Sbase = 40e6
    
    #
    # Step 1: Generate the Ybus matrix for the whole network with 8 buses (8x8 matrix)
    #
    def ytrafo_pu(s, z):
        z_pu = z * (Sbase/s)
        return 1/z_pu

    YT1, YT2, YT3, YT4 = ytrafo_pu(z=0.03j, s=40.0e6),\
                         ytrafo_pu(z=0.06j, s=0.4e6),\
                         ytrafo_pu(z=0.06j, s=0.7e6),\
                         ytrafo_pu(z=0.06j, s=2.0e6)
    

    def ycable_pu(km, vbase):
        zbase = vbase**2/Sbase
        r_pu = 0.11*km / zbase
        x_pu = 0.20j*km / zbase

        return 1/(r_pu + x_pu)

    YC1, YC2, YC3 = ycable_pu(km=0.2, vbase=11e3),\
                    ycable_pu(km=2.0, vbase=11e3),\
                    ycable_pu(km=1.0, vbase=11e3)
    

    from numpy import array
    Ybus = array([
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

    #
    # Step 2: Setup the loads for each bus.
    #           * Generators + positive sign.
    #           * Loads - negative sign
    #
    from math import sin, acos

    def s_pu(p, cosfi):
        fi = acos(cosfi)
        s = p/cosfi
        q = 1j * s * sin(fi)

        return (p + q) / Sbase

    title("Task 2a): Bus voltage and power flow simulation")

    load_flow(Ybus, Sbase, Sload = array([
        0,
        0,
        0,
        -s_pu(p=150e3, cosfi=0.96),
        0,
        -s_pu(p=400e3, cosfi=0.96),
        0,
        -s_pu(p=1500e3, cosfi=0.96),
    ]))
    
    
    title("Task 2b-1): Add 200kW load to Area 1")

    load_flow(Ybus, Sbase, Sload = array([
        0,
        0,
        0,
        -s_pu(p=150e3, cosfi=0.96) - s_pu(p=200e3, cosfi=0.96), # <-- Add 200kw load to Area 1
        0,
        -s_pu(p=400e3, cosfi=0.96),
        0,
        -s_pu(p=1500e3, cosfi=0.96),
    ]))
    
    
    title("Task 2b-2): Add 200kW load to Area 2")

    load_flow(Ybus, Sbase, Sload = array([
        0,
        0,
        0,
        -s_pu(p=150e3, cosfi=0.96),
        0,
        -s_pu(p=400e3, cosfi=0.96) - s_pu(p=200e3, cosfi=0.96), # <-- Add 200kw load to Area 2
        0,
        -s_pu(p=1500e3, cosfi=0.96),
    ]))


    title("Task 2b-3): Add 200kW load to Area 3")

    load_flow(Ybus, Sbase, Sload = array([
        0,
        0,
        0,
        -s_pu(p=150e3, cosfi=0.96),
        0,
        -s_pu(p=400e3, cosfi=0.96),
        0,
        -s_pu(p=1500e3, cosfi=0.96) - s_pu(p=200e3, cosfi=0.96), # <-- Add 200kw load to Area 3
    ]))


def load_flow(Ybus, Sbase, Sload):
    #
    # Step 3: Use Gauss-Siedel method to numerically approximate V
    #
    from numpy import conjugate, ones, sqrt, array
    
    N = 10_000
    Vbus = ones(8) # V = [1pu, 1pu, 1pu, 1pu, ...]
    Yii = array([Ybus[i][i] for i in range(8)])
    Vbases = array([132e3, 11e3, 11e3, 230, 11e3, 230, 11e3, 230])

    for _ in range(N):
        I = conjugate(Sload / Vbus)
        
        YVij = Ybus.dot(Vbus)
        YVii = Yii*Vbus

        Vbus = (1/Yii) * (I - YVij + YVii)

        # Always reset slack-bus to 1pu
        Vbus[0] = 1
        
    #
    # Step 4: Calculate total power flows
    #
    Ibases = Sbase / (Vbus*Vbases * sqrt(3))
    I = Ybus.dot(Vbus) * Ibases
    Sbus = conjugate(I) * Vbus*Vbases * sqrt(3)


    #
    # Step 5: Print results
    #
    print(f"""
    |-------------| {line()} |
    |             | {names("Bus", 8)} |
    |-------------| {line()} |
    | Vinit [V]   | {abs_values(Vbases)} |
    | Vsimu [V]   | {abs_values(Vbus*Vbases)} |
    |-------------| {line()} |
    | Pload [W]   | {real_values(Sload*Sbase)} |
    | Psimu [W]   | {real_values(Sbus)} |
    |-------------| {line()} |
    | Qload [VAr] | {imag_values(Sload*Sbase)} |
    | Qsimu [VAr] | {imag_values(Sbus)} |
    |-------------| {line()} |
    """)


# Print helpers
def title(text):
    print("\n\t"+text)
def line():
    return " | ".join("----------" for _ in range(8))
def names(name, count):
    return " | ".join(f"{f"{name} {i}":<10}" for i in range(1, count+1))
def real_values(values): 
    return" | ".join(f"{x.real:>10.4g}" if abs(x) > 1e-6 else f"{0:>10}" for x in values)
def imag_values(values): 
    return" | ".join(f"{x.imag:>10.4g}" if abs(x) > 1e-6 else f"{0:>10}" for x in values)
def abs_values(values): 
    return" | ".join(f"{abs(x):>10.4g}" if abs(x) > 1e-6 else f"{0:>10}" for x in values)


if __name__ == "__main__":
    main()

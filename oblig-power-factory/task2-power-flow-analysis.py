"""
------------------------------------------------------------------------------
TSE2220: Oblig Power factory / Task2 Power-flow analysis
Student: Jonas (267431@usn.no)
------------------------------------------------------------------------------
"""

from dataclasses import dataclass, field
from numpy import array, ndarray

@dataclass
class Network():
    """Contains only the static part of the network, before any loads are attached and voltages applied"""
    Sgridmin: float
    Sgridmax: float
    Sbase: float
    Vbases: ndarray
    StrafoMax: ndarray
    Ytrafo_pu: ndarray
    Ybus_pu: ndarray
    Ycable_pu: ndarray

def configure_network():
    """
    The network we want to configure:
               --------
               | Grid |  min/max: 60/100MVA
               --------
                   |
     Bus 1 ---------------
           Trafo 1 | 132kV
                   O 40MVA
                   O j0.03
                   | 11kV
     Bus 2 ---------------   
                   | 
           Cable 1 |   |---- - Cable 2 2km --------|---- Cable 3 1km ----------| <-- (0.12 + j0.20) Ohm/km
              200m |   |                           |                           |    
 Area 1 HV ----------------       Area 2 HV ---------------   Area 3 HV --------------- 
            Trafo 2 | 11kV                 Trafo 3 | 11kV              Trafo 4 | 11kV
                    O 400kVA                       O 700kVA                    O 2000kVA
                    O j0.06                        O j0.06                     O j0.06
                    | 230V                         | 230V                      | 230V
 Area 1 LV -----------------      Area 2 LV ---------------   Area 3 LV ---------------
                   |                               |                           |
                   v                               v                           v
                Load 1                           Load 2                      Load 3

    """

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

    YC1, YC2, YC3 = ycable_pu(km=cable1_km, vbase=11e3),\
                    ycable_pu(km=2.0, vbase=11e3),\
                    ycable_pu(km=1.0, vbase=11e3)
    

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
    
    net = Network(
        Sgridmin = 60e6,
        Sgridmax = 100e6,
        Sbase = Sbase,
        Strafo = array([40e3, 400e3, 700e3, 2000e3]),
        Vbases = array([132e3, 11e3, 11e3, 230, 11e3, 230, 11e3, 230]),
        Ybus_pu = Ybus,
        Ytrafo_pu = array([YT1, YT2, YT3, YT4]),
        Ycable_pu = array([YC1, YC2, YC3]),
    )
    
    return net



def main():
    #
    # Task 1 - Configure network
    #
    net = configure_network()

    #
    # Task 2a)
    #
    title("Task 2a): Do a load flow simulation")
    Vbus = load_flow(net)
    trafo_utilization(net, Vbus)
    
    #
    # Task 2b)
    #
    title("Task 2b-1): Add 200kW load to Area 1")
    Vbus = load_flow(extra_p_area1 = 200e3)
    trafo_utilization(net, Vbus)
    
    
    title("Task 2b-2): Add 200kW load to Area 2")
    Vbus = load_flow(extra_p_area2 = 200e3)
    trafo_utilization(net, Vbus)


    title("Task 2b-3): Add 200kW load to Area 3")
    Vbus = load_flow(extra_p_area3 = 200e3)
    trafo_utilization(net, Vbus)

    #
    # Task 2c)
    #
    title("Task 2c): Change length of the cable 1 from 200m to 16 000m")
    Vbus = load_flow(cable1_km=16.0)

    #
    # Task 2d)
    #
    title("Task 2d): How much active power losses are there when running 2c)?")
    active_cable_losses(net, Vbus)
 

def load_flow(net: Network, extra_p_area1 = 0, extra_p_area2 = 0, extra_p_area3 = 0, cable1_km = 0.2):
    """Do a load flow using Gauss-Siedel-numerical approximation method,
        for a given network and load. 

        Returns the resulting voltages - the Vbus"""
    from numpy import array
    
    #
    # Step 1: Setup the loads for each bus.
    #           * Generators + positive sign.
    #           * Loads - negative sign
    #
    def s_pu(p, cosfi):
        from math import sin, acos

        fi = acos(cosfi)
        s = p/cosfi
        q = 1j * s * sin(fi)

        return (p + q) / net.Sbase

    Sload = array([
        0,
        0,
        0,
        -s_pu(p=150e3, cosfi=0.96) - s_pu(p = extra_p_area1, cosfi=0.96),
        0,
        -s_pu(p=400e3, cosfi=0.96) - s_pu(p = extra_p_area2, cosfi=0.96),
        0,
        -s_pu(p=1500e3, cosfi=0.96) - s_pu(p = extra_p_area3, cosfi=0.96),
    ])

    #
    # Step 2: Use Gauss-Siedel method to numerically approximate V
    #
    from numpy import conjugate, ones, sqrt, array
    
    N = 10_000
    Vbus = ones(8) # V = [1pu, 1pu, 1pu, 1pu, ...]
    Yii = array([Ybus[i][i] for i in range(8)])

    for _ in range(N):
        I = conjugate(Sload / Vbus)
        
        YVij = net.Ybus.dot(Vbus)
        YVii = Yii*Vbus

        Vbus = (1/Yii) * (I - YVij + YVii)

        # Always reset slack-bus to 1pu
        Vbus[0] = 1
        
    #
    # Step 3: Calculate total power flows
    #
    Ibases = net.Sbase / (Vbus*net.Vbases * sqrt(3))
    I = net.Ybus.dot(Vbus) * Ibases
    Sbus = conjugate(I) * Vbus*net.Vbases * sqrt(3)

    #
    # Step 4: Print results
    #
    Vnominal = net.Vbases[2:]
    Vactual  = (Vbus*net.Vbases)[2:]
    Vactual_pu = Vbus[2:]

    print(f"""
    |--------------| {line(6)} |
    |              | {areas()} |
    |--------------| {line(6)} |
    | Vnominal [V] | {abs_values(Vnominal)} |
    | Vactual  [V] | {abs_values(Vactual)} |
    | Vactual [pu] | {abs_values(Vactual_pu)} |
    |--------------| {line(6)} |
    """)
    
    return Vbus


def active_cable_losses(net, Vbus):
    """Calculate active power losses on the cables in the network for a given Vbus"""
    from numpy import array, conjugate

    Vcable = array([
        Vbus[2]-Vbus[1], # between busbar 3 and 2
        Vbus[4]-Vbus[2], # between busbar 5 and 3
        Vbus[6]-Vbus[4], # between busbar 7 and 5
    ])

    Icable = (Vcable*net.Ycable / 3**0.5)

    Scable = conjugate(Icable) * Vcable

    print(f"""
    |-------------| {line(3)} |
    |             | {names("Cable", 3)} |
    |-------------| {line(3)} |
    | Vcable [V]  | {abs_values(Vcable)} |
    | Icable [A]  | {abs_values(Icable)} |
    | Pcable [W]  | {real_values(Scable)} |
    |-------------| {line(3)} |
    """)


def trafo_utilization(net, Vbus):
    """Calculate trafo utilization of trafos in the network for a given Vbus."""
    
    from numpy import array, conjugate, sqrt

    StrafoMax = net.StrafoMax[1:]
    VbasesLV = array([net.Vbases[3::2]) 
    VtrafoHV_pu = array([Vbus[2::2]) 
    VtrafoLV_pu = array([Vbus[3::2])  

    # Voltage drop across each trafo
    ΔVtrafo_pu = VtrafoHV_pu - VtrafoLV_pu

    # Current through each trafo
    Itrafo_pu = ΔVtrafo_pu * net.Ytrafo

    # Assume that all current is discharged to 0V on the low voltage side of the trafo.
    # This gives us the trafo power loading:
    ItrafoLV = Itrafo_pu * (net.Sbase / VbasesLV) 
    StrafoLV = VtrafoLV_pu * VbasesLV * conjugate(ItrafoLV)
    StrafoLoadPercent = (abs(StrafoLV) / StrafoMax )*100
    
    # Print results
    print(f"""
    |---------------- | {line(len(StrafoMax))} |
    |                 | {names("Area", len(StrafoMax))} |
    |-----------------| {line(len(StrafoMax))} |
    | StrafoMax  [VA] | {abs_values(StrafoMax)} |
    | StrafoLoad [VA] | {abs_values(StrafoLV)} |
    | StrafoLoad [%]  | {abs_values(StrafoLoadPercent)} |
    |-----------------| {line(len(StrafoMax))} |
    """) 



#
# Print helpers
#
def title(text):
    print("\n\t"+text)
def line(count):
    return " | ".join("--------" for _ in range(count))
def names(name, count):
    return " | ".join(f"{f"{name} {i}":<8}" for i in range(1, count+1))
def areas():
    return " | ".join(f"{f"{i}":<8}" for i in ["Area1HV", "Area1LV", "Area2HV", "Area2LV", "Area3HV", "Area3LV"])
def real_values(values): 
    return" | ".join(f"{x.real:>8.3g}" if abs(x) > 1e-6 else f"{0:>8}" for x in values)
def imag_values(values): 
    return" | ".join(f"{x.imag:>8.3g}" if abs(x) > 1e-6 else f"{0:>8}" for x in values)
def abs_values(values): 
    return" | ".join(f"{abs(x):>8.3g}" if abs(x) > 1e-6 else f"{0:>8}" for x in values)


if __name__ == "__main__":
    main()

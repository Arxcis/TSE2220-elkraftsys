"""
------------------------------------------------------------------------------
TSE2220: Oblig Power factory / Task 1 configure network
Student: Jonas (267431@usn.no)
------------------------------------------------------------------------------
"""

from dataclasses import dataclass
from numpy import array, ndarray

@dataclass
class Network():
    """Contains only the static part of the network, before any loads are attached and voltages applied"""
    Sgrid_min: float
    Sgrid_max: float
    Sbase: float
    Vbase: ndarray
    
    # Loads
    Sload_pu: ndarray

    # Trafos
    Strafo_max: ndarray
    Ytrafo_pu: ndarray
    
    # Cables
    Lcable_km: ndarray
    Ycable_pu: ndarray

    # Ybus 8x8 matrix
    Ybus_pu: ndarray

def configure_network(
        Lcable1_km=0.2,
        Sgrid_min=60e6,
        Sgrid_max=100e6, 
        Ztrafo1_pu=0.03,
        Pextra_area1 = 0,
        Pextra_area2 = 0,
        Pextra_area3 = 0,
    ) -> Network:
    """
    The default network:
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
    
    #
    # Step 0: Select an Sbase
    #
    Sbase = 40e6

    #
    # Step 1: Configure the trafo admittances
    #
    def ytrafo_pu(s, z_pu):
        z_pu_based = z_pu * (Sbase/s)
        return 1/z_pu_based

    YT1, YT2, YT3, YT4 = ytrafo_pu(z_pu=Ztrafo1_pu, s=40.0e6),\
                         ytrafo_pu(z_pu=0.06j, s=0.4e6),\
                         ytrafo_pu(z_pu=0.06j, s=0.7e6),\
                         ytrafo_pu(z_pu=0.06j, s=2.0e6)
    

    #
    # Step 2: Configure the trafo cable admittances
    #
    def ycable_pu(km, vbase):
        zbase = vbase**2/Sbase
        r_pu = 0.124*km / zbase
        x_pu = 0.20j*km / zbase

        return 1/(r_pu + x_pu)

    Lcable_km = array([Lcable1_km, 2.0, 1.0])
    YC1, YC2, YC3 = ycable_pu(km=Lcable_km, vbase=11e3)


    #
    # Step 3: Configure the Ybus 8x8 matrix 
    #
    Ybus_pu = array([
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
    # Step 4: Setup the loads for each bus.
    #           * Generators + positive sign.
    #           * Loads - negative sign
    #
    def s_pu(p, cosfi):
        from math import sin, acos

        fi = acos(cosfi)
        s = p/cosfi
        q = 1j * s * sin(fi)

        return (p + q) / Sbase

    Sload = array([
        0,
        0,
        0,
        -s_pu(p=150e3, cosfi=0.96) - s_pu(p = Pextra_area1, cosfi=0.96),
        0,
        -s_pu(p=400e3, cosfi=0.96) - s_pu(p = Pextra_area2, cosfi=0.96),
        0,
        -s_pu(p=1500e3, cosfi=0.96) - s_pu(p = Pextra_area3, cosfi=0.96),
    ])

    #
    # Step 5: Init the Network object and return
    # 
    return Network(
        Sgrid_min = Sgrid_min,
        Sgrid_max = Sgrid_max,
        Sbase = Sbase,
        Sload_pu = Sload,
        Strafo_max = array([40e6, 400e3, 700e3, 2000e3]),
        Vbase = array([132e3, 11e3, 11e3, 230, 11e3, 230, 11e3, 230]),
        Ybus_pu = Ybus_pu,
        Ytrafo_pu = array([YT1, YT2, YT3, YT4]),
        Ycable_pu = array([YC1, YC2, YC3]),
        Lcable_km=Lcable_km
    )
    

if __name__ == "__main__":#
    net = configure_network()

    print(net)
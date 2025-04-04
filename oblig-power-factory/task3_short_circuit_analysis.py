"""
------------------------------------------------------------------------------
TSE2220: Oblig Power factory / Task3 Short-circuit analysis
Student: Jonas (267431@usn.no)
------------------------------------------------------------------------------
"""
from task1_configure_network import Network, configure_network
from numpy import array, sqrt

def main():

    # Basic network 
    net = configure_network(Sgrid_min = 60e6, Sgrid_max = 100e6, Ztrafo1_pu = 0.03j)
    short_circuit(net)

    # Changing external grid to have 10x more short circuit power
    net = configure_network(Sgrid_min = 600e6, Sgrid_max = 1000e6, Ztrafo1_pu = 0.03j)
    short_circuit(net)

    # Changing Trafo 1 to have 10% more short circuit impedance
    net = configure_network(Sgrid_min = 600e6, Sgrid_max = 1000e6, Ztrafo1_pu = 0.13j)
    short_circuit(net)


def short_circuit(net: Network):
    print("---------------------------------")
    print(f"Grid min: {net.Sgrid_min:.3g}, Grid max: {net.Sgrid_max:.3g}")
    print("---------------------------------")

    # Base
    Sbase = net.Sbase  # MVA
    Vbase = 132e3 # kV

    # Gridreaktanser
    Xgrid_min = Sbase / net.Sgrid_min 
    Xgrid_max = Sbase / net.Sgrid_max

    # Traforeaktanser
    XT1, XT2, XT3, XT4 = abs(net.Ytrafo_pu**-1)
    print(" | ".join([f"XTrafo{i+1}: {x:.3g}" for i,x in enumerate([XT1, XT2, XT3, XT4])]))

    XCable1, XCable2, XCable3 = abs(net.Ycable_pu**-1)
    print(" | ".join([f"XCable{i+1}: {x:.3g}" for i,x in enumerate([XCable1, XCable2, XCable3])]))


    # Kortslutningsreaktanser
    Xkss = XT1 + XCable1 + array([
        0,             # Area 1 HV
        XT2,           # Area 1 LV
        XCable2,       # Area 2 HV
        XCable2 + XT3, # Area 2 LV
        XCable2 + XCable3,       # Area 3 HV
        XCable2 + XCable3 + XT4, # Area 3 LV
    ])

    Xkss_min = Xgrid_min + Xkss
    Xkss_max = Xgrid_max + Xkss

    # Kortslutningsstrømmer min og max
    Vkbase = net.Vbase[2:]

    Skss_min_base = Sbase / Xkss_min
    Ikss_min_base = Skss_min_base / (sqrt(3) * Vbase)
    Ikss_min = Ikss_min_base * (Vbase / Vkbase)

    Skss_max_base = Sbase / Xkss_max
    Ikss_max_base = Skss_max_base / (sqrt(3) * Vbase)
    Ikss_max = Ikss_max_base * (Vbase / Vkbase)

    #
    # Skriv resultater til skjerm
    #
    Names = ["Area 1 HV", "Area 1 LV", "Area 2 HV", "Area 2 LV", "Area 3 HV", "Area 3 LV"]
    
    # Hjelpefunksjoner til print
    line = lambda names: " | ".join("----------" for _ in names)
    names = lambda names: " | ".join(f"{x:<10}" for x in names)
    values = lambda values: " | ".join(f"{x:>10.3g}" for x in values)

    print(f"""
    |--------------------| {line(Names)} |
    |                    | {names(Names)} |
    |--------------------| {line(Names)} |
    | Xkss_min           | {values(Xkss_min)} |
    | Ikss_min v/132kv   | {values(Ikss_min_base)} |
    | Ikss_min v/kortsl. | {values(Ikss_min)} |
    |--------------------| {line(Names)} |
    | Xkss_max           | {values(Xkss_max)} |
    | Ikss_max v/132kv   | {values(Ikss_max_base)} |
    | Ikss_max v/kortsl. | {values(Ikss_max)} |
    |--------------------| {line(Names)} |

    """)


if __name__ == "__main__":
    main()

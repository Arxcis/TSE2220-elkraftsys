"""
------------------------------------------------------------------------------
TSE2220: Oblig Power factory / Task3 Short-circuit analysis by hand
Student: Jonas (267431@usn.no)
------------------------------------------------------------------------------
"""

def main():
    # Basic network 
    short_circuit(Sgrid_min = 60e6, Sgrid_max = 100e6, XT1merke = 0.03)
    
    # Changing external grid to have 10x more short circuit power
    short_circuit(Sgrid_min = 600e6, Sgrid_max = 1000e6, XT1merke = 0.03)

    # Changing Trafo 1 to have 10% more short circuit impedance
    short_circuit(Sgrid_min = 600e6, Sgrid_max = 1000e6, XT1merke = 0.13)


def short_circuit(Sgrid_min, Sgrid_max, XT1merke):
    print("---------------------------------")
    print(f"Grid min: {Sgrid_min:.3g}, Grid max: {Sgrid_max:.3g}")
    print("---------------------------------")

    # Base
    Sbase = 40e6  # MVA
    Vbase = 132e3 # kV
    Xbase = ((Vbase)**2 / Sbase) # Antar at X ~= Z og bruker bare X videre. Gjør denne antagelsen siden har ingen informasjon fra nettet som sier noe om cosfi og forholdet mellom X og Z.

    # Gridreaktanser
    Xgrid_min = Sbase / Sgrid_min 
    Xgrid_max = Sbase / Sgrid_max

    # Traforeaktanser
    def xtrafo(Xmerke, Smerke, Sny):
        return Xmerke *( (Sny / Smerke) )

    XT1 = xtrafo(Xmerke=XT1merke, Smerke=Sbase, Sny=Sbase) 
    XT2 = xtrafo(Xmerke=0.06, Smerke=0.4e6, Sny=Sbase)
    XT3 = xtrafo(Xmerke=0.06, Smerke=0.7e6, Sny=Sbase)
    XT4 = xtrafo(Xmerke=0.06, Smerke=2.0e6, Sny=Sbase)

    print(" | ".join([f"XTrafo{i+1}: {x:.3g}" for i,x in enumerate([XT1, XT2, XT3, XT4])]))

    # Kabelreaktanser
    def xcable(km):
        """For kabel flat forlegning, kabelavstand 70mm og 150mm2 tverrsnitt"""
        XCable_km = 0.20 # Ohm/km - flat forlegning (ikke trekant).
        RCable_km = 0.11 # Ohm/km - brukes ikke siden vi bare jobber med X. Antar at R << X for hele nettet.

        return XCable_km * km / Xbase

    XCable1 = xcable(km = 0.2)
    XCable2 = xcable(km = 2.0)
    XCable3 = xcable(km = 1.0) 

    print(" | ".join([f"XCable{i+1}: {x:.3g}" for i,x in enumerate([XCable1, XCable2, XCable3])]))


    # Kortslutningsreaktanser
    from numpy import array
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

    from math import sqrt

    # Kortslutningsstrømmer min og max
    Vkss = array([11e3, 0.230e3, 11e3, 0.230e3, 11e3, 0.230e3])

    Skss_min_base = Sbase / Xkss_min
    Ikss_min_base = Skss_min_base / (sqrt(3) * Vbase)
    Ikss_min = Ikss_min_base * (Vbase / Vkss)

    Skss_max_base = Sbase / Xkss_max
    Ikss_max_base = Skss_max_base / (sqrt(3) * Vbase)
    Ikss_max = Ikss_max_base * (Vbase / Vkss)

    #
    # Skriv resultater til skjerm
    #
    Names = ["Area 1 HV", "Area 1 LV", "Area 2 HV", "Area 2 LV", "Area 3 HV", "Area 3 LV"]
    
    # Hjelpefunksjoner til print
    line = lambda names: " | ".join("----------" for _ in names)
    names = lambda names: " | ".join([f"{x:<10}" for x in names])
    values = lambda values: " | ".join([f"{x:>10.3g}" for x in values])

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

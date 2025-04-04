"""
------------------------------------------------------------------------------
TSE2220: Oblig Power factory / Task2 Power-flow analysis
Student: Jonas (267431@usn.no)
------------------------------------------------------------------------------
"""

from task1_configure_network import Network, configure_network
from numpy import array, conjugate, sqrt, ndarray, ones

def main():
    #
    # Task 2a) - Do a load flow simulation on the configured network from task 1
    #
    title("Task 2a): Do a load flow simulation")
    net = configure_network()
    Vbus = load_flow(net)
    trafo_utilization(net, Vbus)
    
    #
    # Task 2b) - compare adding a 200kW load to either Area 1, 2 or 3
    #
    title("Task 2b-1): Add 200kW load to Area 1")
    net = configure_network(Pextra_area1 = 200e3)
    Vbus = load_flow(net)
    trafo_utilization(net, Vbus)
    
    
    title("Task 2b-2): Add 200kW load to Area 2")
    net = configure_network(Pextra_area2 = 200e3)
    Vbus = load_flow(net)
    trafo_utilization(net, Vbus)


    title("Task 2b-3): Add 200kW load to Area 3")
    net = configure_network(Pextra_area3 = 200e3)
    Vbus = load_flow(net)
    trafo_utilization(net, Vbus)

    #
    # Task 2c)
    #
    title("Task 2c): Change length of the cable 1 from 200m to 16 000m")
    net = configure_network(Lcable1_km=16.0)
    Vbus = load_flow(net)

    #
    # Task 2d)
    #
    title("Task 2d): How much active power losses are there when running 2c)?")
    active_cable_losses(net, Vbus)
 

def load_flow(net: Network):
    """
    Does a load flow using Gauss-Siedel-numerical approximation method, for a given network and load. 

        Returns the resulting per unit voltages -> Vbus_pu
    """
    

    #
    # Step 2: Use Gauss-Siedel method to numerically approximate V
    #
    
    N = 10_000
    Vbus_pu = ones(8) # V = [1pu, 1pu, 1pu, 1pu, ...]
    Yii_pu = array([net.Ybus_pu[i][i] for i in range(8)])

    for _ in range(N):
        I_pu = conjugate(net.Sload_pu / Vbus_pu)
        
        YVij_pu = net.Ybus_pu.dot(Vbus_pu)
        YVii_pu = Yii_pu*Vbus_pu

        Vbus_pu = (1/Yii_pu) * (I_pu - YVij_pu + YVii_pu)

        # Always reset slack-bus to 1pu
        Vbus_pu[0] = 1
        
    #
    # Step 3: Calculate total power flows
    #
    Ibases = net.Sbase / (Vbus_pu*net.Vbase * sqrt(3))
    I = net.Ybus_pu.dot(Vbus_pu) * Ibases

    #
    # Step 4: Print results
    #
    Vnominal = net.Vbase[2:]
    Vactual  = (Vbus_pu*net.Vbase)[2:]
    Vactual_pu = Vbus_pu[2:]

    print(f"""
    |--------------| {line(6)} |
    |              | {areas()} |
    |--------------| {line(6)} |
    | Vnominal [V] | {abs_values(Vnominal)} |
    | Vactual  [V] | {abs_values(Vactual)} |
    | Vactual [pu] | {abs_values(Vactual_pu)} |
    |--------------| {line(6)} |
    """)
    
    return Vbus_pu



def trafo_utilization(net: Network, Vbus_pu: ndarray):
    """Calculate trafo utilization of trafos in the network for a given Vbus_pu."""
    
    Strafo_max = net.Strafo_max[1:]
    VbaseLV = array(net.Vbase[3::2]) 
    VtrafoHV_pu = array(Vbus_pu[2::2]) 
    VtrafoLV_pu = array(Vbus_pu[3::2])  

    # Voltage drop across each trafo
    ΔVtrafo_pu = VtrafoHV_pu - VtrafoLV_pu

    # Current through each trafo
    Itrafo_pu = ΔVtrafo_pu * net.Ytrafo_pu[1:]

    # Assume that all current is discharged to 0V on the low voltage side of the trafo.
    # This gives us the trafo power loading:
    ItrafoLV = Itrafo_pu * (net.Sbase / VbaseLV) / sqrt(3)
    StrafoLV = VtrafoLV_pu * VbaseLV * conjugate(ItrafoLV) * sqrt(3)
    StrafoLoadPercent = (abs(StrafoLV) / Strafo_max )*100
    
    # Print results
    print(f"""
    |------------------| {line(len(Strafo_max))} |
    |                  | {names("Area", len(Strafo_max))} |
    |------------------| {line(len(Strafo_max))} |
    | Strafo_max  [VA] | {abs_values(Strafo_max)} |
    | StrafoLoad [VA]  | {abs_values(StrafoLV)} |
    | StrafoLoad [%]   | {abs_values(StrafoLoadPercent)} |
    |------------------| {line(len(Strafo_max))} |
    """) 


def active_cable_losses(net: Network, Vbus_pu):
    """Calculate active power losses on the cables in the network for a given Vbus_pu"""

    ΔVcable = array([
        Vbus_pu[2]-Vbus_pu[1], # between busbar 3 and 2
        Vbus_pu[4]-Vbus_pu[2], # between busbar 5 and 3
        Vbus_pu[6]-Vbus_pu[4], # between busbar 7 and 5
    ]) * 11e3

    # Current through the cables
    Icable = (ΔVcable*net.Ycable_pu / sqrt(3))

    # Power loss on the cable
    Scable = conjugate(Icable) * ΔVcable * sqrt(3)

    print(f"""
    |-------------| {line(len(ΔVcable))} |
    |             | {names("Cable", len(ΔVcable))} |
    |-------------| {line(len(ΔVcable))} |
    | ΔVcable [V] | {abs_values(ΔVcable)} |
    | Icable [A]  | {abs_values(Icable)} |
    | Pcable [W]  | {real_values(Scable)} |
    |-------------| {line(len(ΔVcable))} |
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

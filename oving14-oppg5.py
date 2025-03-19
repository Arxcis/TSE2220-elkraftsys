"""
Oppgave 5: Lag admitansmatrise til følgende system
"""

# 5 linjer
ZA = 0.723 + 1.050j
ZB = 0.123 + 0.518j
ZC = 0.282 + 0.640j
ZD = 0.300 + 0.618j
ZE = 0.080 + 0.370j

YA, YB, YC, YD, YE = ZA**-1, ZB**-1, ZC**-1, ZD**-1, ZE**-1

from numpy import array

Y = array([[YA+YD,      -YA,      -YD,     0],  # Node 1
           [  -YA, YA+YB+YE,      -YE,   -YB],  # Node 2
           [  -YD,      -YE, YC+YD+YE,   -YC],  # Node 3
           [    0,      -YB,      -YC, YB+YC]]) # Node 4

print("[")
for row in Y:

    print(row, ",")

print("]")

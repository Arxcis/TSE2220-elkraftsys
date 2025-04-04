# Oblig - Power Factory

## Introduction

This work accounts for 10% of the total grade of the subject TSE2220. It uses the simulation software DIGSILENT Power Factory and Python to solve 3 tasks. Task 1 (25%) is to build a 11kV distribution network given some preliminary data. Task 2 - Load flow simulation (35%) and Task 3 - Short-circuit analysis (40%) carries out calculations and analysis of the network.

This work contains:

- A "README.pdf"-file      - containing the text you are currently reading.
- "task2-load-analysis.py" - which contains the load-analysis using Gauss-Siedel-method, formalized into a python-script.
- "task3-short-circuit.py" - which contains the shortcut-analysis using the impedance-method, formalized into a python-script.

## Task 1: Network Configuration
```
               --------
               | Grid |
               --------
                   |
     Bus 1 ---------------
           Trafo 1 | 132kV
                   O
                   O
                   |  11kV
     Bus 2 ---------------   
                   |
           Cable 1 |   |--- Cable 2 ---------------|--- Cable 3 ---------------|
                   |   |                           |                           |    
 Area 1 HV ----------------       Area 2 HV ---------------   Area 3 HV --------------- 
            Trafo 2 | 11kV                 Trafo 3 | 11kV              Trafo 4 | 11kV
                    O                              O                           O
                    O                              O                           O
                    | 230V                         | 230V                      | 230V
 Area 1 LV -----------------      Area 2 LV ---------------   Area 3 LV ---------------
                   |                               |                           |
                   v                               v                           v
                Load 1                           Load 2                      Load 3
```
_Caption: View of the network with all the different components_


## Task 2: Load-flow analysis

### Task 2a): Do a load flow in Power Factory

```sh
jonas@pop-os:~/git/TSE2220-elkraftsys/oblig-power-factory$ python task2-power-flow-analysis.py

	Task 2a): Do a load flow simulation

    |--------------| -------- | -------- | -------- | -------- | -------- | -------- |
    |              | Area1HV  | Area1LV  | Area2HV  | Area2LV  | Area3HV  | Area3LV  |
    |--------------| -------- | -------- | -------- | -------- | -------- | -------- |
    | Vnominal [V] |  1.1e+04 |      230 |  1.1e+04 |      230 |  1.1e+04 |      230 |
    | Vactual  [V] |  1.1e+04 |      228 | 1.09e+04 |      226 | 1.09e+04 |      225 |
    | Vactual [pu] |    0.999 |    0.992 |    0.993 |    0.982 |    0.991 |    0.976 |
    |--------------| -------- | -------- | -------- | -------- | -------- | -------- |

    |-------------------- | -------- | -------- | -------- |
    |                     | Area 1   | Area 2   | Area 3   |
    |---------------------| -------- | -------- | -------- |
    | StrafoMax  [VA]     |    4e+05 |    7e+05 |    2e+06 |
    | StrafoLoad [VA]     | 1.56e+05 | 4.17e+05 | 1.56e+06 |
    | StrafoLoad/Max [%]  |     39.1 |     59.5 |     78.1 |
    |---------------------| -------- | -------- | -------- |
```

### 2b) Add 200kW to the system to either Area 1, 2 or 3


#### Undesøker endring i spenning før og etter last settes inn

Tabell under viser at å sette inn en ekstra 200kW last i område 1, gir et totalt spenningsfall levert til forbruker på -4V eller -1.7%. Om lasten settes inn i enten område 2 eller 3 blir spenningsfallet levert til forbruker i begge disse områdene på -6V eller -2.6%. Dette er et akseptabelt fall for det meste av utstyr. NEK400 anbefaler maksimalt spenningsfall på 5% på generell basis og 2-3% spesifikt for motorer. Tallene taler til fordel for å legge til 200kW last til Area 1, fordi dette fører til minst spenningsfall levert til forbruker, bare 1.7%. Om lasten legges til område 2 eller 3 blir spenningsfallet levert i grenseland for det som er anbefalt for motorer.


| Vactual [V]        | Area1LV | Area2LV | Area3LV |
|--------------------|---------|---------|---------|
| Vfør +0kW      [V] | 228     | 226     | 225     |
| Vetter +200kW  [V] | 226     | 224     | 224     |
| Vfall fra 230V [V] | -4      | -6      | -6      |
| Vfall fra 230V [%] | -1.7%   | -2.6%   | -2.6%   |



#### Undersøker utnyttelsesgrad i trafo (lasteffekt / merkeeffekt)

Om vi ser på trafo sin utnyttelsesgrad, vil den bli påvirket veldig ulikt avhengig av hvor lasten plasseres. For Area1 øker utnyttelsesgrad til trafo fra 39.1% til 91.1% (+52%) økning. På en måte er dette positivt. Area 1 sin trafo var underutnyttet før lasten ble lagt til. Å legge til lasten til area 1 skaper en mer jevn fordeling av belastningen på tvers av alle 3 områdene, med 91%, 60% og 78% belastning på de respektive trafoene.

| StrafoLoad/Max [%]  | Area1LV | Area2LV | Area3LV |
|---------------------|---------|---------|---------|
| før   +0kW    [%]   | 39.1    | 59.5    | 78.1    |
| etter +200kW  [%]   | 91.1    | 89.3    | 88.5    |
| delta         [%]   | +52%    | +29.8%  | +10.4%  |


#### Konklusjon

Det er anbefalt å plassere 200kW last i Area 1, da dette vil føre til lavest spenningsfall levert til forbruker i alle 3 områder og en jevnest mulig belastningsgrad om en sammenligner alle de 3 ulike trafoene.



### 2c) Change length of the cable 1 from 200m to 16 000m

After changing the cable from 200m to 16km, we do not have a satisfactory network anymore. The voltage drop delivered to all consumers now exceed 6% in Area1 and 7% in Area 2 and 3. This is way above the recommended NEK maximum of 5%. Consider upgrading the cross-sectional area of Cable1, or increase the voltage to 22kV or more to lower the voltage drop below 5% at least, and ideally below 3%.
```sh
	Task 2c): Change length of the cable 1 from 200m to 16 000m

    |--------------| -------- | -------- | -------- | -------- | -------- | -------- |
    |              | Area1HV  | Area1LV  | Area2HV  | Area2LV  | Area3HV  | Area3LV  |
    |--------------| -------- | -------- | -------- | -------- | -------- | -------- |
    | Vnominal [V] |  1.1e+04 |      230 |  1.1e+04 |      230 |  1.1e+04 |      230 |
    | Vactual  [V] | 1.04e+04 |      216 | 1.03e+04 |      214 | 1.03e+04 |      212 |
    | Vactual [pu] |    0.946 |    0.939 |     0.94 |    0.929 |    0.938 |    0.922 |
    |--------------| -------- | -------- | -------- | -------- | -------- | -------- |
```

### 2d) How much active power losses are there in 2c)?

The active

```
	Task 2d): How much active power losses are there when running 2c)?

    |-------------| ---------- | ---------- | ---------- |
    |             | Cable 1    | Cable 2    | Cable 3    |
    |-------------| ---------- | ---------- | ---------- |
    | Vcable [V]  |      766.5 |      88.91 |      35.15 |
    | Icable [A]  |      121.2 |      112.5 |      88.91 |
    | Pcable [W]  |  4.476e+04 |       4818 |       1506 |
    |-------------| ---------- | ---------- | ---------- |
```

## Task 3: Short-circuit analysis

### 3a) Max and min three-phase short circuit

- External grid 60MVA, 100MVA short-circuit power.
- Take a picture of the screen as an answer to this task

### 3b) Why are the short-circuit values different for different bus bars?

### 3c) Calculate the short-circuit values by hand using impedance method

```
jonas@pop-os:~/git/TSE2220-elkraftsys$ python oblig-power-factory/main.py
---------------------------------
Grid min: 6e+07, Grid max: 1e+08
---------------------------------
XTrafo1: 0.03 | XTrafo2: 6 | XTrafo3: 3.43 | XTrafo4: 1.2
XCable1: 9.18e-05 | XCable2: 0.000918 | XCable3: 0.000459

    |--------------------| ---------- | ---------- | ---------- | ---------- | ---------- | ---------- |
    |                    | Area 1 HV  | Area 1 LV  | Area 2 HV  | Area 2 LV  | Area 3 HV  | Area 3 LV  |
    |--------------------| ---------- | ---------- | ---------- | ---------- | ---------- | ---------- |
    | Xkss_min           |      0.697 |        6.7 |      0.698 |       4.13 |      0.698 |        1.9 |
    | Ikss_min v/132kv   |        251 |       26.1 |        251 |       42.4 |        251 |       92.2 |
    | Ikss_min v/kortsl. |   3.01e+03 |    1.5e+04 |   3.01e+03 |   2.43e+04 |   3.01e+03 |   5.29e+04 |
    |--------------------| ---------- | ---------- | ---------- | ---------- | ---------- | ---------- |
    | Xkss_max           |       0.43 |       6.43 |      0.431 |       3.86 |      0.431 |       1.63 |
    | Ikss_max v/132kv   |        407 |       27.2 |        406 |       45.3 |        405 |        107 |
    | Ikss_max v/kortsl. |   4.88e+03 |   1.56e+04 |   4.87e+03 |    2.6e+04 |   4.87e+03 |   6.15e+04 |
    |--------------------| ---------- | ---------- | ---------- | ---------- | ---------- | ---------- |


```

### 3d) Recalculate a) with 10x external grid short-circuit

- External grid min: 600MVA and max 1000MVA.

```
---------------------------------
Grid min: 6e+08, Grid max: 1e+09
---------------------------------
XTrafo1: 0.03 | XTrafo2: 6 | XTrafo3: 3.43 | XTrafo4: 1.2
XCable1: 9.18e-05 | XCable2: 0.000918 | XCable3: 0.000459

    |--------------------| ---------- | ---------- | ---------- | ---------- | ---------- | ---------- |
    |                    | Area 1 HV  | Area 1 LV  | Area 2 HV  | Area 2 LV  | Area 3 HV  | Area 3 LV  |
    |--------------------| ---------- | ---------- | ---------- | ---------- | ---------- | ---------- |
    | Xkss_min           |     0.0968 |        6.1 |     0.0977 |       3.53 |     0.0981 |        1.3 |
    | Ikss_min v/132kv   |   1.81e+03 |       28.7 |   1.79e+03 |       49.6 |   1.78e+03 |        135 |
    | Ikss_min v/kortsl. |   2.17e+04 |   1.65e+04 |   2.15e+04 |   2.85e+04 |   2.14e+04 |   7.73e+04 |
    |--------------------| ---------- | ---------- | ---------- | ---------- | ---------- | ---------- |
    | Xkss_max           |     0.0701 |       6.07 |      0.071 |        3.5 |     0.0715 |       1.27 |
    | Ikss_max v/132kv   |    2.5e+03 |       28.8 |   2.46e+03 |         50 |   2.45e+03 |        138 |
    | Ikss_max v/kortsl. |      3e+04 |   1.65e+04 |   2.96e+04 |   2.87e+04 |   2.94e+04 |    7.9e+04 |
    |--------------------| ---------- | ---------- | ---------- | ---------- | ---------- | ---------- |
```

### 3e) Compare 3a) and 3d) - Why are the results different?

### 3f) Increase interanl inductance (Uk) in transformer T1 to 13%.

```
---------------------------------
Grid min: 6e+08, Grid max: 1e+09
---------------------------------
XTrafo1: 0.13 | XTrafo2: 6 | XTrafo3: 3.43 | XTrafo4: 1.2
XCable1: 9.18e-05 | XCable2: 0.000918 | XCable3: 0.000459

    |--------------------| ---------- | ---------- | ---------- | ---------- | ---------- | ---------- |
    |                    | Area 1 HV  | Area 1 LV  | Area 2 HV  | Area 2 LV  | Area 3 HV  | Area 3 LV  |
    |--------------------| ---------- | ---------- | ---------- | ---------- | ---------- | ---------- |
    | Xkss_min           |      0.197 |        6.2 |      0.198 |       3.63 |      0.198 |        1.4 |
    | Ikss_min v/132kv   |        889 |       28.2 |        885 |       48.2 |        883 |        125 |
    | Ikss_min v/kortsl. |   1.07e+04 |   1.62e+04 |   1.06e+04 |   2.77e+04 |   1.06e+04 |   7.18e+04 |
    |--------------------| ---------- | ---------- | ---------- | ---------- | ---------- | ---------- |
    | Xkss_max           |       0.17 |       6.17 |      0.171 |        3.6 |      0.171 |       1.37 |
    | Ikss_max v/132kv   |   1.03e+03 |       28.4 |   1.02e+03 |       48.6 |   1.02e+03 |        128 |
    | Ikss_max v/kortsl. |   1.23e+04 |   1.63e+04 |   1.23e+04 |   2.79e+04 |   1.22e+04 |   7.32e+04 |
    |--------------------| ---------- | ---------- | ---------- | ---------- | ---------- | ---------- |
```

### 3g) Compare 3a) and 3f) - Why are the results different?

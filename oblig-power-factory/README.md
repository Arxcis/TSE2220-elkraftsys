# Oblig - Power Factory

## Introduction

This work accounts for 10% of the total grade of the subject TSE2220. It uses the simulation software DIGSILENT Power Factory and Python to solve 3 tasks. Task 1 (25%) is to build a 11kV distribution network given some preliminary data. Task 2 - Load flow simulation (35%) and Task 3 - Short-circuit analysis (40%) carries out calculations and analysis of the network.

This work contains:

- A "README.pdf"-file - containing the text you are currently reading.
- A "network-configuration.pfd"-file (Power factory data file) containing the 11kV network fully configured and ready to run simulations.
- A "network-short-circuit-analysis-by-hand.py"-file - which contains the shortcut-analysis using the impedance-method, done first by hand, and then formalized into a python-script.

## Task 1: Network Configuration

_Picture of the network here_

_Caption: Power Factory idle view of the network found inside network-configuration.pfd_

## Task 2: Load-flow analysis

### Task 2a): Do a load flow in Power Factory

```sh
jonas@pop-os:~/git/TSE2220-elkraftsys/oblig-power-factory$ python task2-power-flow-analysis.py

	Task 2a): Bus voltage and power flow simulation

    |--------------| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
    |              | Bus 1    | Bus 2    | Bus 3    | Bus 4    | Bus 5    | Bus 6    | Bus 7    | Bus 8    |
    |--------------| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
    | Vnominal [V] | 1.32e+05 |  1.1e+04 |  1.1e+04 |      230 |  1.1e+04 |      230 |  1.1e+04 |      230 |
    | Vactual  [V] | 1.32e+05 |  1.1e+04 |  1.1e+04 |      228 | 1.09e+04 |      226 | 1.09e+04 |      225 |
    |--------------| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
```

### 2b) Add 200kW to the system to either Area 1, 2 or 3


#### Undesøker endring i spnning før og etter last settes inn

Kjører lastflytanalyse på alle 3 varianter:

| Area | Før | Etter |
|------|-----|-------|
| 1    | 228V | 226V |
| 2    | 226V | 224V |
| 3    | 225V | 224V |

Resultatene er ikke så ille. Vi har fortsatt "god spenning". Innenfor 10% av nominell.

```sh
	Task 2b-1): Add 200kW load to Area 1

    |--------------| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
    |              | Bus 1    | Bus 2    | Bus 3    | Bus 4    | Bus 5    | Bus 6    | Bus 7    | Bus 8    |
    |--------------| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
    | Vnominal [V] | 1.32e+05 |  1.1e+04 |  1.1e+04 |      230 |  1.1e+04 |      230 |  1.1e+04 |      230 |
    | Vactual  [V] | 1.32e+05 |  1.1e+04 |  1.1e+04 |      226 | 1.09e+04 |      226 | 1.09e+04 |      225 |
    |--------------| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |


	Task 2b-2): Add 200kW load to Area 2

    |--------------| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
    |              | Bus 1    | Bus 2    | Bus 3    | Bus 4    | Bus 5    | Bus 6    | Bus 7    | Bus 8    |
    |--------------| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
    | Vnominal [V] | 1.32e+05 |  1.1e+04 |  1.1e+04 |      230 |  1.1e+04 |      230 |  1.1e+04 |      230 |
    | Vactual  [V] | 1.32e+05 |  1.1e+04 |  1.1e+04 |      228 | 1.09e+04 |      224 | 1.09e+04 |      224 |
    |--------------| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |


	Task 2b-3): Add 200kW load to Area 3

    |--------------| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
    |              | Bus 1    | Bus 2    | Bus 3    | Bus 4    | Bus 5    | Bus 6    | Bus 7    | Bus 8    |
    |--------------| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
    | Vnominal [V] | 1.32e+05 |  1.1e+04 |  1.1e+04 |      230 |  1.1e+04 |      230 |  1.1e+04 |      230 |
    | Vactual  [V] | 1.32e+05 |  1.1e+04 |  1.1e+04 |      228 | 1.09e+04 |      226 | 1.09e+04 |      224 |
    |--------------| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
```

#### Undersøker effektbelastning i trafo


- Which area would I put the load?
- Here are some things worth considering:

  1. Is the remaining capacity of the upstream trafos sufficient to support this new load?
  2. Which trafo has the most/least available capacity?
  3. What would the trafo utilization rate be for Area 1,2 and 3, before and after insertion of the 200kW load?
  4. What should be the deciding factor? Utilization rate or balacing spare capacity?

     - Having a balanced spare capacity in both area 1, 2 and 3 gives flexibility of where future load increases could be located. On the downside, this would decrease the maximum load. Keeping a big spare capacity in one area, and maxing out the two other areas might be beneficial if one wants to attract business with high power demands. If all the areas are averaged out, none have enough spare capacity to compete for this big customer.

     - Keeping utilization rate below 90% may increase longevity of components.
     - It comes down to priorities and politics in the end. What should be the deciding factor?

### 2c) Change length of the cable 1 from 200m to 16 000m

- Display results like in 2a)

```sh
	Task 2c): Change length of the cable 1 from 200m to 16 000m

    |--------------| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
    |              | Bus 1    | Bus 2    | Bus 3    | Bus 4    | Bus 5    | Bus 6    | Bus 7    | Bus 8    |
    |--------------| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
    | Vnominal [V] | 1.32e+05 |  1.1e+04 |  1.1e+04 |      230 |  1.1e+04 |      230 |  1.1e+04 |      230 |
    | Vactual  [V] | 1.32e+05 |  1.1e+04 | 1.04e+04 |      216 | 1.03e+04 |      214 | 1.03e+04 |      212 |
    |--------------| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
```

- Does the power system still have a satisfactory network?
- Consider the voltages on the busbars.
    * Lengden på kabelen blir for lang med 11kV.
    * Vurder å steppe opp spenningen fra 11kV -> 22kV over et så langt strekke.

### 2d) How much active power losses are?

- When running the 2c)-simulation?

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

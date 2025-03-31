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

### 2a) Do a load flow in Power Factory

```sh
~/git/TSE2220-elkraftsys$ python oblig-power-factory/task2-power-flow-analysis.py



Y admittance matrix
-----------------------------------------------------------

      33.3,      33.3,         0,         0,         0,         0,         0,         0
      33.3,      96.8,      66.3,         0,         0,         0,         0,         0
         0,      66.3,        73,     0.167,      6.63,         0,         0,         0
         0,         0,     0.167,     0.167,         0,         0,         0,         0
         0,         0,      6.63,         0,      20.1,     0.292,      13.3,         0
         0,         0,         0,         0,     0.292,     0.292,         0,         0
         0,         0,         0,         0,      13.3,         0,        14,     0.833
         0,         0,         0,         0,         0,         0,     0.833,     0.833



Bus loads
-----------------------------------------------------------

      | Bus1 [VA] | Bus2 [VA] | Bus3 [VA] | Bus4 [VA] | Bus5 [VA] | Bus6 [VA] | Bus7 [VA] | Bus8 [VA]
    - | --------- | --------- | --------- | --------- | --------- | --------- | --------- | ---------
    0 |         0 |         0 |         0 | 1.562e+05 |         0 | 4.167e+05 |         0 | 1.562e+06



Bus voltages simulation (13 iterations to 4 digits stable)
-----------------------------------------------------------

      | Bus1 [V]  | Bus2 [V]  | Bus3 [V]  | Bus4 [V]  | Bus5 [V]  | Bus6 [V]  | Bus7 [V]  | Bus8 [V]
    - | --------- | --------- | --------- | --------- | --------- | --------- | --------- | ---------
    0 |  1.32e+05 |   1.1e+04 |   1.1e+04 |     228.5 |   1.1e+04 |     227.8 |   1.1e+04 |     227.2
    1 |  1.32e+05 |   1.1e+04 |   1.1e+04 |     228.4 |   1.1e+04 |     227.5 | 1.098e+04 |     226.7
    2 |  1.32e+05 |   1.1e+04 |   1.1e+04 |     228.4 | 1.098e+04 |     227.5 | 1.097e+04 |     226.3
    3 |  1.32e+05 |   1.1e+04 |   1.1e+04 |     228.4 | 1.098e+04 |     227.2 | 1.096e+04 |     226.1
    4 |  1.32e+05 |   1.1e+04 |   1.1e+04 |     228.4 | 1.097e+04 |     227.1 | 1.096e+04 |     225.9
    5 |  1.32e+05 |   1.1e+04 |   1.1e+04 |     228.4 | 1.097e+04 |     226.9 | 1.094e+04 |     225.8
    6 |  1.32e+05 |   1.1e+04 |   1.1e+04 |     228.3 | 1.096e+04 |     226.8 | 1.094e+04 |     225.5
    7 |  1.32e+05 |   1.1e+04 | 1.099e+04 |     228.3 | 1.096e+04 |     226.6 | 1.093e+04 |     225.5
    8 |  1.32e+05 |   1.1e+04 | 1.099e+04 |     228.3 | 1.095e+04 |     226.6 | 1.093e+04 |     225.3
    9 |  1.32e+05 |   1.1e+04 | 1.099e+04 |     228.3 | 1.095e+04 |     226.5 | 1.093e+04 |     225.3
   10 |  1.32e+05 |   1.1e+04 | 1.099e+04 |     228.2 | 1.094e+04 |     226.4 | 1.092e+04 |     225.1
   11 |  1.32e+05 |   1.1e+04 | 1.099e+04 |     228.2 | 1.094e+04 |     226.4 | 1.092e+04 |     225.1
   12 |  1.32e+05 | 1.099e+04 | 1.099e+04 |     228.2 | 1.094e+04 |     226.3 | 1.092e+04 |       225



Bus power flow
-----------------------------------------------------------

      | Bus1      | Bus2      | Bus3      | Bus4      | Bus5      | Bus6      | Bus7      | Bus8
    - | --------- | --------- | --------- | --------- | --------- | --------- | --------- | ---------
  [V] |  1.32e+05 | 1.099e+04 | 1.099e+04 |     228.2 | 1.094e+04 |     226.3 | 1.092e+04 |       225
  [A] |     3.289 |     3.458 |     13.84 |     227.8 |     2.587 |     606.4 |     8.022 |      2309
 [VA] | 1.302e+06 | 1.141e+05 | 4.565e+05 |  1.56e+05 |  8.49e+04 | 4.117e+05 | 2.628e+05 | 1.558e+06
```

### 2b) Add 200kW to the system to either Area 1, 2 or 3

#### Add 200kW to Area 1

```sh
  i | Bus1 [VA] | Bus2 [VA] | Bus3 [VA] | Bus4 [VA] | Bus5 [VA] | Bus6 [VA] | Bus7 [VA] | Bus8 [VA]
  - | --------- | --------- | --------- | --------- | --------- | --------- | --------- | ---------
  0 |         0 |         0 |         0 |  3.65e+05 |         0 |  4.17e+05 |         0 |  1.56e+05


  i | Bus1 [V]  | Bus2 [V]  | Bus3 [V]  | Bus4 [V]  | Bus5 [V]  | Bus6 [V]  | Bus7 [V]  | Bus8 [V]
  - | --------- | --------- | --------- | --------- | --------- | --------- | --------- | ---------
 ..
 12 |  1.32e+05 |   1.1e+04 |   1.1e+04 |     226.1 | 1.098e+04 |     227.2 | 1.098e+04 |     229.3
```

#### Add 200kW to Area 2

```sh
  i | Bus1 [VA] | Bus2 [VA] | Bus3 [VA] | Bus4 [VA] | Bus5 [VA] | Bus6 [VA] | Bus7 [VA] | Bus8 [VA]
  - | --------- | --------- | --------- | --------- | --------- | --------- | --------- | ---------
  0 |         0 |         0 |         0 |  1.56e+05 |         0 |  6.25e+05 |         0 |  1.56e+05


  i | Bus1 [V]  | Bus2 [V]  | Bus3 [V]  | Bus4 [V]  | Bus5 [V]  | Bus6 [V]  | Bus7 [V]  | Bus8 [V]
  - | --------- | --------- | --------- | --------- | --------- | --------- | --------- | ---------
 ..
 12 |  1.32e+05 |   1.1e+04 |   1.1e+04 |     228.4 | 1.098e+04 |     225.7 | 1.098e+04 |     229.2
```

#### Add 200kW to Area 3

```sh
  i | Bus1 [VA] | Bus2 [VA] | Bus3 [VA] | Bus4 [VA] | Bus5 [VA] | Bus6 [VA] | Bus7 [VA] | Bus8 [VA]
  - | --------- | --------- | --------- | --------- | --------- | --------- | --------- | ---------
  0 |         0 |         0 |         0 |  1.56e+05 |         0 |  4.17e+05 |         0 |  3.65e+05

  i | Bus1 [V]  | Bus2 [V]  | Bus3 [V]  | Bus4 [V]  | Bus5 [V]  | Bus6 [V]  | Bus7 [V]  | Bus8 [V]
  - | --------- | --------- | --------- | --------- | --------- | --------- | --------- | ---------
 ..
 12 |  1.32e+05 |   1.1e+04 |   1.1e+04 |     228.4 | 1.098e+04 |     227.1 | 1.097e+04 |     228.8
```

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
- Does the power system still have a satisfactory network?
- Consider the voltages on the busbars.

### 2d) How much active power losses are?

- When running the 2c)-simulation?

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

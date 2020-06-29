# Temperature Ploter
Use Temp_ploter.py to generate plots from data collected by Arduino using an infrared thermometer sensor.

# Table of Contents
* [Setup](#Setup)
* [Data-Acquisition](#Data-Acquisition)
* [Code Example](#Code-Example)
    * [Code Ouput](##Code-Ouput)
    * [Another Example for plot_temp() Output](##Another-Example-for-plot_temp()-Output)

# Setup
Infrared Thermometer - MLX90614

<img src="https://cdn.sparkfun.com/r/500-500/assets/parts/3/3/5/1/09570-01.jpg" height="300" width="300">
<img src="https://cdn.sparkfun.com/assets/learn_tutorials/4/5/0/mlx90614-pinout.png" height="300" width="300">

MLX90614 Pin | Arduino Pin | Note
--- | --- | ---
VDD | 3.3V
VSS | 0V
PWN/SDA | SDA (A4) | Pulled up to 3.3V via a 4.7kΩ Resistor
SCL/Vz | SCL (A5) | Pulled up to 3.3V via a 4.7kΩ Resistor

![setup](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/4/5/0/breadboard-mlx90614.jpg)

# Data Acquisition
Use thermometer_time.ino to record data with Arduino.\
Used [CoolTerm](https://freeware.the-meiers.org/) program to record data from Arduino to desktop.\
Saved data into a text file using this format:\
general: `YYYY-MM-DD HH-MM-SS.txt`\
example: `2020-04-27 23-36-40.txt`

Example of text file contents.
>68.02 72.77\
68.27 72.77\
68.20 72.73\
68.16 72.66\
68.20 72.70\
68.16 72.70\
68.09 72.70\
68.02 72.70\
68.09 72.70\
68.09 72.70\
68.02 72.66\
68.09 72.66\
68.31 72.66

# Code Example
```python
import Temp_ploter as tplt 

plts = tplt.Plots()
alist = ['2020-04-27 23-36-40 to 7-07.txt', '2020-04-28 20-55-50 to 8-41.txt',
         '2020-04-29 22-34-19 to 8-48.txt']
for i in alist:
    plts.add_plot(i)
plts.plot_files() # outputs the first 3 plots
plts.plot_temp() # outputs the last plot
```
## Code Ouput
![plot1](https://i.imgur.com/ABWZ3gA.png)

![plot2](https://i.imgur.com/VvEMhLW.png)

![plot3](https://i.imgur.com/XXWIoYc.png)

![plot4](https://i.imgur.com/cNX21Qq.png)

## Another Example for plot_temp() Output
![plot5](https://i.imgur.com/SoVwotK.png)

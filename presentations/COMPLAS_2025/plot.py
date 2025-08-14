import os
import glob
import pandas as pd
import matplotlib.pyplot as plt, mpld3

#find all csv files 
csv_files = glob.glob('*.{}'.format('csv'))

fig, ax = plt.subplots()    
for file in csv_files:
    df = pd.read_csv(file)
    x = df["External_Displacementx"]
    y = df["External_Forcex"]

    ax.plot(x, y, label=file)
# ax.set_title("Daily Temperature")
ax.set_xlabel("Displacement [mm]")
ax.set_ylabel("Force [N]")
ax.grid(True)
ax.legend()
ax.tick_params(axis="x", rotation=45) 
# plt.show()
html_file = "assets/plot.html"
mpld3.save_html(fig, html_file)
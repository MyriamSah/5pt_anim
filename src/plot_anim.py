# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 15:22:16 2021
@author: Myriam
"""

import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import argparse

# Parse arguments
parser = argparse.ArgumentParser()
parser.add_argument(
    "-i",
    "--input",
    default=None,
    type=str,
    help="Log file to animate",
)
parser.add_argument(
    "-o",
    "--output",
    default=None,
    type=str,
    help="Name of the output (.mp4) file",
)



def main(data_fname, video_fname):
    # Load the data
    Coord = pd.read_csv("./data/" + data_fname, sep=";")
    Coord = np.array(Coord)
    print(Coord[:,5])
    X = Coord[:,1]
    Y = Coord[:,2]
    Next = Coord[:,5]
    
    # Initialise figure
    X2 = [63,63,252,441,441]
    Y2 = [63,315,189,63,315]
    
    fig= plt.figure()
    error = plt.plot(X2,Y2, color="darkorange", marker="o", markersize=106.864, linewidth =0)
    dots2 = plt.plot(X2,Y2, "bo", markersize=44.22)
    dots = plt.plot(X2,Y2, "ko", markersize=36.849)
    lines = plt.plot([], color = "pink", linewidth = 5)
    line = lines[0]
    plt.axis("scaled")
    plt.xlim(0,500)
    plt.ylim(0,350)
    
    x_data = []
    y_data = []
    x_data1 = []
    y_data1 = []
    
    # Update figure
    def animate(i):
        if X[i] != 0 or Y[i] != 0:
            x_data.append(X[i])
            y_data.append(Y[i])
        if Next[i] == True:
            x_data.clear()
            y_data.clear()  
        line.set_xdata(x_data)
        line.set_ydata(y_data)
        error
        dots
        dots2
        return line
    
    # Animate and save
    anim = FuncAnimation(fig, animate, frames=Coord.shape[0], interval=1, repeat=False)
    anim.save("./animations/" + video_fname)


if __name__ == "__main__":
    args = parser.parse_args()
    data_fname = args.input
    video_fname = args.output
    main(data_fname, video_fname)
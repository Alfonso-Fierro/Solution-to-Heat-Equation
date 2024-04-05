import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation
import temperatura
print("2D heat equation solver")

plaque_length = 5
plaque_height = 5
k = 0.001
num_iters = 100

def init_cond(x, y):
     return 700
def gausssian_cond(x, y):
    x_center = plaque_length / 2
    y_center = plaque_height / 2

    amplitude = 15
    sigma_x = plaque_length / 8 
    sigma_y = plaque_height / 8  

    gaussian = amplitude * np.exp(-((x - x_center)**2 / (2 * sigma_x**2) + (y - y_center)**2 / (2 * sigma_y**2)))
    return 700

x = np.linspace(0,plaque_length,100)
y = np.linspace(0,plaque_height,100)

plaque_x, plaque_y = np.meshgrid(x,y)




def paint_grid(time):
        grid = temperatura.plaque_temp(plaque_x,plaque_y,time,a=plaque_length, b=plaque_height,alpha=k,f=init_cond)
        return grid

def plotheatmap(u_k, k):
    # Clear the current plot figure
    plt.clf()

    plt.title(f"Temperatura cuando t = {k:.3f} unit time")
    plt.xlabel("x")
    plt.ylabel("y")

    # This is to plot u_k (u at time-step k)
    plt.pcolormesh(u_k, cmap=plt.cm.jet, vmin=0, vmax=750)
    plt.colorbar()

    return plt

# Do the calculation here


def animate(k):
    plotheatmap(paint_grid(k), k)

anim = animation.FuncAnimation(plt.figure(), animate, interval=1, frames=70, repeat=False)
anim.save("Posada_Fierro.gif")
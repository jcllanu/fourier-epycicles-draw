import math
import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np
import matplotlib.image as mpimg

def numerical_integral_trapezoidal_rule(inf_limit, sup_limit, f, N=10000):
    h=(sup_limit-inf_limit)/N
    sum_accum = (f(inf_limit) + f(inf_limit))/2
    xn = inf_limit
    for _ in range(N-1):
        xn += h
        sum_accum += f(xn)
    return h*sum_accum

def a(n, f):
    return numerical_integral_trapezoidal_rule(-math.pi, math.pi, lambda x: f(x)*math.cos(n*x))/math.pi

def b(n, f):
    return numerical_integral_trapezoidal_rule(-math.pi, math.pi, lambda x: f(x)*math.sin(n*x))/math.pi

def c(n, g, h):
    return ((a(n,g)+b(n,h))/2, (a(n,h)-b(n,g))/2)

def module(c):
    return math.sqrt(pow(c[0],2)+ pow(c[1],2))

def argument(c):
    return math.atan2(c[1],c[0])

def animate_frame_2D(x, c_values, K, previous_points, g, h, M, ax, L, name):
    ax[1,0].clear()
    ax[1,1].clear()
    ax[0,0].clear()

    ax[1,0].plot([g(t) for t in np.linspace(-math.pi, math.pi, M + 1)], [h(t) for t in np.linspace(-math.pi, math.pi, M + 1)], linestyle='-', color='red')
    # Add the circle to the axis
    ax[1,0].add_patch(plt.Circle((0, 0), module(c_values[0]), fill=False))
    ax[1,0].arrow(0, 0, c_values[0][0], c_values[0][1],
         head_width=0.05, head_length=0.1, fc='blue', ec='black', length_includes_head=True)
    sum_acum = list((module(c_values[0])*math.cos(argument(c_values[0])), module(c_values[0])*math.sin(argument(c_values[0]))))
    for k in range(1, K+1):
        ax[1,0].add_patch(plt.Circle((sum_acum[0], sum_acum[1]), module(c_values[k]), fill=False))
        ax[1,0].arrow(sum_acum[0], sum_acum[1], module(c_values[k])*math.cos(k*x+argument(c_values[k])), module(c_values[k])*math.sin(k*x+argument(c_values[k])),
         head_width=0.05, head_length=0.1, fc='blue', ec='black', length_includes_head=True)
        sum_acum[0]=sum_acum[0]+module(c_values[k])*math.cos(k*x+argument(c_values[k]))
        sum_acum[1]=sum_acum[1]+module(c_values[k])*math.sin(k*x+argument(c_values[k]))

        ax[1,0].add_patch(plt.Circle((sum_acum[0], sum_acum[1]), module(c_values[-k]), fill=False))
        ax[1,0].arrow(sum_acum[0], sum_acum[1], module(c_values[-k])*math.cos(-k*x+argument(c_values[-k])), module(c_values[-k])*math.sin(-k*x+argument(c_values[-k])),
         head_width=0.05, head_length=0.1, fc='blue', ec='black', length_includes_head=True)
        sum_acum[0]=sum_acum[0]+module(c_values[-k])*math.cos(-k*x+argument(c_values[-k]))
        sum_acum[1]=sum_acum[1]+module(c_values[-k])*math.sin(-k*x+argument(c_values[-k]))
    previous_points.append(sum_acum)
    # Separate the list of points into x and y coordinates
    x_vals, y_vals = zip(*previous_points)

    ax[1,0].plot(x_vals, y_vals, linestyle='-', color='blue')
    ax[1,0].plot([x_vals[-1], x_vals[-1]], [y_vals[-1], L], linestyle='--', color='black')
    ax[1,0].plot([x_vals[-1], L], [y_vals[-1], y_vals[-1]], linestyle='--', color='black')
    ax[1,0].plot([x_vals[-1]], [y_vals[-1]], 'o', color='black')
    ax[1,0].set_xlim(-L, L)
    ax[1,0].set_ylim(-L, L)
    ax[1,0].set_aspect('equal')
    ax[1,0].set_title("Fourier Drawing - Epicycles")
    ax[1,0].set_xlabel('x')
    ax[1,0].set_ylabel('y')

    ax[0,0].plot([g(t) for t in np.linspace(-math.pi, math.pi, M + 1)],np.linspace(-math.pi, math.pi, M + 1),  linestyle='-', color='red')
    ax[0,0].plot([x_vals[-1], x_vals[-1]], [-math.pi, x], linestyle='--', color='black')
    ax[0,0].plot([x_vals[-1]], [x], 'o', color='black')
    ax[0,0].plot(x_vals, np.linspace(- math.pi, x, len(x_vals)),  linestyle='-', color='blue')
    
    ax[0,0].set_ylim(-0.1-math.pi, math.pi + 0.1)
    ax[0,0].set_xlim(-L, L)
    ax[0,0].set_title("X axis")
    ax[0,0].set_xlabel('t')
    ax[0,0].set_ylabel('x')

    ax[1,1].plot(np.linspace(-math.pi, math.pi, M + 1),[h(t) for t in np.linspace(-math.pi, math.pi, M + 1)], linestyle='-', color='red')
    ax[1,1].plot(np.linspace(- math.pi, x, len(y_vals)),y_vals, linestyle='-', color='blue')

    ax[1,1].plot([-math.pi, x],[y_vals[-1], y_vals[-1]], linestyle='--', color='black')
    ax[1,1].plot([x],[y_vals[-1]], 'o', color='black')
    ax[1,1].set_xlim(-0.1 - math.pi, math.pi + 0.1)
    ax[1,1].set_ylim(-L, L)
    ax[1,1].set_title("Y axis")
    ax[1,1].set_xlabel('t')
    ax[1,1].set_ylabel('y')

    plt.suptitle(name + '\n' + 't = ' + "{:.2f}".format((x+math.pi)/(2*math.pi)))

def initFunction():
    return 

def heart_x_v2(t):
    return 16*pow(math.sin(t),3)

def heart_y_v2(t):
    return 13*math.cos(t)-5*math.cos(2*t)-2*math.cos(3*t)-math.cos(4*t)

def heart_x(t):
    if t<0:
        return 1+2*t/math.pi
    if t<math.pi/2:
        return 1/2+math.cos(2*t)/2
    return -1/2+math.cos(2*t-math.pi)/2

def heart_y(t):   
    if t<-math.pi/2:
        return -1-2*t/math.pi
    if t<0:
        return 1+2*t/math.pi
    if t<math.pi/2:
        return 1+math.sin(2*t)/2
    return 1+math.sin(2*t-math.pi)/2

def lemniscate_x(t,a=1):
    return a*math.cos(t)/(1+pow(math.sin(t),2))

def lemniscate_y(t,a=1):
    return a*math.cos(t)*math.sin(t)/(1+pow(math.sin(t),2))

def polygone_x(t,n):
    theta = (t + math.pi)/(2*math.pi)
    n1=math.floor(n*theta)
    n2=n1+1
    x0=math.cos(n1*2*math.pi/n +math.pi)
    x1=math.cos(n2*2*math.pi/n+math.pi)
    
    tau=n*theta-n1
    return x0 + tau*(x1-x0)

def polygone_y(t,n):
    theta = (t + math.pi)/(2*math.pi)
    n1=math.floor(n*theta)
    n2=n1+1
    y0=math.sin(n1*2*math.pi/n +math.pi)
    y1=math.sin(n2*2*math.pi/n+math.pi)
    
    tau=n*theta-n1
    return y0 + tau*(y1-y0)

def polygonal(points, t):
    points.append(points[0])
    theta = (t + math.pi)/(2*math.pi)
    n1=math.floor(len(points)*theta)
    n2=n1+1
    tau=len(points)*theta-n1
    return points[n1%len(points)] + tau*(points[n2%len(points)]- points[n1%len(points)])

def draw(name, g, h, K, L, N=100, M=1000):
    c_values=dict()
    for k in range(-K,K+1):
        c_values[k] = c(k, g, h)

    previous_points = []

    figure, ax = plt.subplots(2,2,figsize=(10, 10))

    ani = animation.FuncAnimation(
        figure,
        func=animate_frame_2D,
        frames=np.linspace(-math.pi, math.pi, N + 1),
        fargs=(c_values, K, previous_points, g, h, M, ax, L, name),
        init_func=initFunction
    )

    ani.save('animations/'+name + ".gif", writer='pillow', fps=100)

# draw('Heart', heart_x_v2, heart_y_v2, 5, 18)
# draw('Lemniscate', lemniscate_x, lemniscate_y, 5, 1.2)
# draw('Equilateral Triangle', lambda x: polygone_x(x,3), lambda x: polygone_y(x,3), 10, 1.2)
# draw('Square', lambda x: polygone_x(x,4), lambda x: polygone_y(x,4), 10, 1.2)
# draw('Regular Pentagon', lambda x: polygone_x(x,5), lambda x: polygone_y(x,5), 10, 1.1)
# draw('Regular Hexagon', lambda x: polygone_x(x,6), lambda x: polygone_y(x,6), 10, 1.1)
# draw('Regular Heptagon', lambda x: polygone_x(x,7), lambda x: polygone_y(x,7), 10, 1.1)
# draw('Regular Octagon', lambda x: polygone_x(x,8), lambda x: polygone_y(x,8), 10, 1.1)



points = []

# Function that is executed each time that a click on the script is listened
def onclick(event):
    if event.xdata is not None and event.ydata is not None:
        x, y = event.xdata, event.ydata
        points.append([x, y])
        plt.plot(np.array(points)[:,0], np.array(points)[:,1], 'r-o')
        plt.draw()

# Create figure
fig, ax = plt.subplots()
path = input('Insert the path of a background image (S for skip): ')

if path !='S':
    img = mpimg.imread(path)  # Usa un archivo .png o .jpg
    ax.imshow(img, extent=[-10, 10, -10, 10], aspect='auto')

ax.set_title("Click to draw. Close the window when finished.")
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.grid(True)

# Conect click event with onclick function 
cid = fig.canvas.mpl_connect('button_press_event', onclick)

# Show pop-up window (blocked until it is closed)
plt.show()
num_epycicles = input('Introduce the number of epycicles: ')
output = input('Name your animation: ')
draw(output, lambda x: polygonal(list(np.array(points)[:,0]),x), lambda x: polygonal(list(np.array(points)[:,1]),x), int(num_epycicles), 10)
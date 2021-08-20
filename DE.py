from scipy.integrate import odeint
import numpy as np

def predator_prey_model(x, t, a, b, c, d):
    # Assign each ODE to a element from the list x
    predators = x[0] # x(t)
    preys = x[1] # y(t)
    
    # define each ODE
    dx_dt = predators*(-a + b*preys)
    dy_dt = preys*(d - c*predators)
    
    return [dx_dt, dy_dt]

def lineal_system(y, t, x1, y1, x2, y2):
    initial_x = y[0]
    initial_y = y[1]
    
    dx_dt = x1*initial_x + y1*initial_y
    dy_dt = x2*initial_x + y2*initial_y
    
    return [dx_dt, dy_dt]
    
    




    


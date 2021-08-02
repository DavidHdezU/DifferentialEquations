from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

def predator_prey_model(x, t, a, b, c, d):
    # Assign each ODE to a element from the list x
    predators = x[0] # x(t)
    preys = x[1] # y(t)
    
    # define each ODE
    dx_dt = predators*(-a + b*preys)
    dy_dt = preys*(d - c*predators)
    
    return [dx_dt, dy_dt]





    


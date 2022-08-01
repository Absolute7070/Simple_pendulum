import numpy as np 



def theta_k(theta, omega, deltat): 
    '''Compute the next step of theta'''
    return theta+ omega*deltat


def omega_k(theta, omega, deltat):
    return omega+ g/L* np.sin(theta)* deltat
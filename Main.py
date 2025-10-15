import numpy as np
#https://en.wikipedia.org/wiki/Hyperplane_separation_theorem for collision detection

# ssh= soil suction head, e.g psi from the equation
def green_amp_equation(infiltration, hydraulic_con, ssh, effective_porosity, time, repeated):
    # numpy.log = ln
    infiltration = hydraulic_con*time + ssh*effective_porosity*np.log(1 + infiltration/(ssh*effective_porosity))
    if repeated == 5000:
        return infiltration
    repeated += 1
    print(infiltration)
    green_amp_equation(infiltration, hydraulic_con, ssh, effective_porosity, time, repeated)

def green_amp_test(infiltration, hydraulic_con, ssh, effective_porosity, time):
    return hydraulic_con*time + ssh*effective_porosity*(np.log(1 + (infiltration/(ssh*effective_porosity))))

repeated = 0
infilt_temp = 1 # value does not mater
#  Function must be a loop, interation limit is less then needed
while repeated < 1000:
    temp = green_amp_test(infilt_temp, 0.05, 29.22,0.338, 1)
    infilt_temp = temp
    print(infilt_temp)
    repeated += 1




#res_infiltration = green_amp_equation(50, 0.05, 29.22,0.423, 1, 0)
#print("\n",res_infiltration)

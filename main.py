import numpy as np
#https://en.wikipedia.org/wiki/Hyperplane_separation_theorem for collision detection

# ssh = soil suction head, E.G psi from the equation
def green_amp_equation_acc(infiltration, hydraulic_con, ssh, effective_porosity, time, repeated, nodes):
    # numpy.log = ln
    temp_infiltration = hydraulic_con * time + ssh * effective_porosity * np.log(1 + infiltration / (ssh * effective_porosity))
    if repeated > 100:
        return nodes
    repeated += 1
    nodes.append(temp_infiltration)
    infiltration = temp_infiltration
    return green_amp_equation_acc(infiltration, hydraulic_con, ssh, effective_porosity, time, repeated, nodes)


def green_amp_equation_dxdy(infiltration, hydraulic_con, ssh, effective_porosity, time, repeated, nodes):
    temp_infiltration = hydraulic_con * (1 + (ssh * effective_porosity) / infiltration)
    if repeated > 100:
        return nodes
    repeated += 1
    nodes.append(temp_infiltration)
    infiltration = temp_infiltration
    return green_amp_equation_dxdy(infiltration, hydraulic_con, ssh, effective_porosity, time, repeated, nodes)

infiltration_nodes = []
first_guess= 1 # first_guess does not matter


temp_nodes = green_amp_equation_acc(first_guess, 0.05, 29.22,0.338, 1, 0, infiltration_nodes)
first_guess= 1
#temp_nodes_dxdy = green_amp_equation_dxdy(first_guess, 0.05, 29.22,0.338, 1, 0, infiltration_nodes)

in_nodes = np.array(temp_nodes)



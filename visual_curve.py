# Start date: 24/5/2020
# Last edit date: 25/5/2020
# This task ask user to input the simulation days, meeting_probability
# and the health point of patient zero, then show the graph of the simulation.

from simulation import *
from matplotlib import pyplot as plt
import numpy as np

default_health = 75


def visual_curve(days, meeting_probability, patient_zero_health):
    # get the simulation result(in list)
    simulation_result = run_simulation(days, meeting_probability, patient_zero_health)
    print(simulation_result)
    # create a list of days for draw the x-axes
    x = np.arange(1, days + 1)
    # label the x-axes and y-axes
    plt.xlabel("Days")
    plt.ylabel("Count")
    # draw the graph
    plt.plot(x, simulation_result)
    plt.show()
    # save the graph
    # plt.savefig("scenario_c.png")


if __name__ == '__main__':
    days = int(input('Please input the number of simulation days: '))
    meeting_probability = float(input('Please input the simulation meeting probability: '))
    patient_zero_health = float(input('Please input the patient zero\'s health: '))
    visual_curve(days, meeting_probability, patient_zero_health)



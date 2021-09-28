# Start date: 24/5/2020
# Last edit date: 25/5/2020
# This file has Patient class inheritance from task1, and add some new methods,
# such as check a person is contagious or not, and the health reduced by contract
# contagious people. The run_simulation function simulate the virus spread status
# by given days, meeting_probability, patient_zero_health.

import random
from load_people import *

# set initial health for all people
default_health = 75


class Patient(Person):
    def __init__(self, first_name, last_name, health):
        # inherited from person class
        Person.__init__(self, first_name, last_name)
        self.health = health

    def get_health(self):
        return self.health

    def set_health(self, new_health):
        self.health = new_health

    def is_contagious(self):
        # check the contagious status of this person,
        # is it's health less than 50 means the person has been contagious
        #if int(self.health) >= 50:
        if round(self.health) >= 50:
            return False
        else:
            return True

    def infect(self, viral_load):

        if self.health <= 29:
            self.health = self.health - (0.1 * viral_load)
        elif self.health < 50:
            self.health = self.health - (1.0 * viral_load)
        else:
            self.health = self.health - (2.0 * viral_load)
        # the health can't lose any further if less than 0
        if self.health < 0:
            self.health = 0

    def sleep(self):
        self.health += 5
        # the health can't recover any further if over than 100
        if self.health > 100:
            self.health = 100


def run_simulation(days, meeting_probability, patient_zero_health):
    # initialize patients objects, and the list for store number of contagious people
    patients = load_patients(default_health)
    contagious_case = []
    # set patients zero's health
    patients[0].set_health(patient_zero_health)
    # simulation loop
    for day in range(days):
        # store the number of contagious people in a day
        infected = 0
        for person in patients:
            for friend in person.get_friends():
                # create a random number in [0,1] to decide this person meets or not meet friends
                meet_para = random.uniform(0, 1)
                # meet friend
                if meet_para <= meeting_probability:
                    # infect friend of this person
                    if person.is_contagious():
                        self_viral_load = 5 + (((person.get_health() - 25) ** 2) / 62)
                        friend.infect(self_viral_load)
                    # the friend of this person infect him
                    if friend.is_contagious():
                        friend_viral_load = 5 + (((friend.get_health() - 25) ** 2) / 62)
                        person.infect(friend_viral_load)
        # at the end of the day calculate the number of contagious people, and let all people to sleep
        for person in patients:
            if person.is_contagious():
                infected += 1
            person.sleep()
        # add the number of contagious people in that day to contagious_case list
        contagious_case.append(infected)
    return contagious_case


def load_patients(initial_health):
    # open file
    sample_patients = open('a2_sample_set.txt', 'r')
    # initialize two list to store the patients objects and other one store name only(in str type)
    patients, patients_name = [], []
    i = 0
    # read patients
    for read_name in sample_patients:
        # split first name and last name
        first_name = read_name.split(':', 1)[0].split(' ', 1)[0].strip()
        last_name = read_name.split(':', 1)[0].split(' ', 1)[1].strip()
        # create patients object and add it to patients list, and their name to patients_name list
        patients_obj = Patient(first_name, last_name, initial_health)
        patients.append(patients_obj)
        patients_name.append(patients_obj.get_name())
    # set the pointer to the start of the file
    sample_patients.seek(0)
    # get friends' name from the sample file
    for read_friend in sample_patients:
        friends = read_friend.split(':', 1)[1].split(',')
        # enumerate all friend in friends list
        for friend in friends:
            for name in patients_name:
                # compare the name, if they are same, add the patient object as friends to friends list
                if friend.strip() == name:
                    patients[i].add_friend(patients[patients_name.index(name)])
        i += 1
    # close the file
    sample_patients.close()
    return patients


if __name__ == '__main__':
    # You may add your own testing code within this main block
    # to check if the code is working the way you expect.

    # This is a sample test case. Write your own testing code here.
    test_result = run_simulation(15, 0.8, 49)
    print(test_result)
    # Sample output for the above test case (15 days of case numbers):
    # [8, 16, 35, 61, 93, 133, 153, 171, 179, 190, 196, 198, 199, 200, 200]
    #
    # Note: since this simulation is based on random probability, the
    # actual numbers may be different each time you run the simulation.

    # Another sample test case (high meeting probability means this will
    # spread to everyone very quickly; 40 days means will get 40 entries.)
    test_result = run_simulation(40, 1, 1)
    print(test_result)
    # sample output:
    # [19, 82, 146, 181, 196, 199, 200, 200, 200, 200, 200, 200, 200, 200,
    # 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200,
    # 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200]

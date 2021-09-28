# Start date: 23/5/2020
# Last edit date: 2/6/2020
# This file create Person class with name and friends attribute,
# and load_people function read each line of the example file to import
# the person and their friend, the return a list with all people objects.


class Person:

    def __init__(self, first_name, last_name):
        # set attributes for Person objects
        self.first_name = first_name
        self.last_name = last_name
        self.friend_list = []

    # method add a friend(person objects) to friend list
    def add_friend(self, friend_person):
        self.friend_list.append(friend_person)

    # return the name of this object
    def get_name(self):
        return self.first_name + ' ' + self.last_name

    # return the friend list of this object
    def get_friends(self):
        return self.friend_list


def load_people():
    # open file
    sample_people = open('a2_sample_set.txt', 'r')
    # initialize two list to store the people objects and other one store name only(in str type)
    people, people_name = [], []
    i = 0
    # read people
    for read_name in sample_people:
        # split first name and last name
        first_name = read_name.split(':', 1)[0].split(' ', 1)[0].strip()
        last_name = read_name.split(':', 1)[0].split(' ', 1)[1].strip()
        # create people object and add it to people list, and their name to people_name list
        person_obj = Person(first_name, last_name)
        people.append(person_obj)
        people_name.append(person_obj.get_name())
    # set the pointer to the start of the file for next read
    sample_people.seek(0)
    # get friends' name from the sample file
    for read_friend in sample_people:
        friends = read_friend.split(':', 1)[1].split(',')
        # enumerate all friend in friends list
        for friend in friends:
            for name in people_name:
                # compare the name, if they are same, add the people object as friends to friends list
                if friend.strip() == name:
                    people[i].add_friend(people[people_name.index(name)])
        i += 1
    # close the file
    sample_people.close()
    return people

if __name__ == '__main__':
    pass # placeholder only. You may add your own testing code within this
         # main block to check if the code is working the way you expect.


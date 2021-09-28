# Modeling-infectious-epidemics
FIT9136-Assignment-2

## Background

In the past, there have been viral disease epidemics (including the 1918 influenza pandemic) which have got out of hand. We would like to simulate the way such diseases spread, to better understand how this happens.


In this assignment, you will create the necessary data structure to simulate social links and disease transmission between people, simulate infections among the population over a period of time, and plot graphs to determine whether an outbreak is contained or not.


The model we’ll use is a simplification of the real world; we will not use actual parameters or consider all important factors. However, on completion of this assignment, you will have a better understanding of how such simulations are written in the real world.

## The source data

We surveyed 200 fake people, all with unique names, and asked them to provide the names of their friends in the group who they are in regular contact with. You may assume that each person has specified at least one friend, and each of the person’s friends has also named that person as a friend.
Please download the file named a2_sample_set.txt as your program will need to open and read data from this file. You may place the file in the same folder as your assignment code.1


The data file consists of 200 records. Each record is recorded on its own line in the file, and consists of a person’s name, together with all the names of that person’s friends. The real file is 200 lines long, but to illustrate the file format, just the first two lines of the file are shown here as a sample: Gill Bates: Jodee Killam, Natacha Osterhoudt, Jom Tones, Verdie Tong, Ossie Digangi Jom Tones: Marry Blakely, Masako Miguel, Gill Bates


### Syntax of each record line: 

As seen in the example above, each line of data in the file consists of the first and last name of a particular person, followed by a colon and a space character “: “ and then the first and last names of each of their friends (people they are in regular contact with) with each friend’s name separated by a comma and a space “, ”.


### Example interpretation of source data above:

• The first line in the file is the record for Gill Bates. Gill Bates has named the following people as her social connections: Jodee Killam, Natacha Osterhoudt, Jom Tones, Verdie Tong, and Ossie Digangi. This means that if Gill Bates is contagious (able to spread the virus), Gill Bates may infect the people she has named, and if her friends are contagious, they may infect Gill Bates.


• On the next line, Jom Tones has named his friends in a similar way, and so on.


• Note that Gill Bates has named Jom Tones as one of her friends. This means that Jom Tones must also name Gill Bates as one of his friends. It’s not unusual that may both visit each other, and the virus may travel from either person to the other. You can assume that this rule is followed for all records in the file.


## Health of each person

Each person has a number of health points which changes over time depending on a person’s health. The government has published the following guidance about health points. The number of health points is used to check if a patient is contagious (i.e. able to infect other people) or not:


76-100 health points: perfect health, not contagious


75 health points: average health, not contagious


50-74 health points: fair health, not contagious


30-49 health points: contagious


0-29 health points: poor health, contagious


When sleeping after each day, each person’s immune system will naturally add 5 health points to that person, up to a maximum of 100 health points.


Health points are not required to be in an integer form, so each time you need to check if a person is contagious or not, the person’s current health should be rounded to the nearest integer. The maximum possible health of a healthy person is 100 (the health point value of each person should be limited to this maximum), and the minimum possible value is 0. A person with 0 health can still recover, but cannot lose any further health points.


Allowed libraries:


  • math
  
  
  • random
  
  
  • numpy
  
  
  • scipy
  
  
  • matplotlib
  
  
  • pandas

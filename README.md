# Modeling-infectious-epidemics
FIT9136-Assignment-2

load_people.py use a2_sample_set.txt


simulation.py use class in load_people


visul_curve.py imports all functions in simulation


File link load_people.py -> simulation.py -> visul_curve.py -> show result

  
*   _if the import file code doesn't work, create an empty file call: \_\_init\_\_.py




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



## Meeting probability

Each day, a person may or may not visit another person for a meeting. For each person, the probability that they will travel to visit one of their friends depends on social distancing regulations. A single meeting probability parameter will be applied to all people in the group to determine the effect of a certain level of social distancing. This probability is a fraction of 1. For example, running the simulation with a meeting probability of 1.0 means that every day, every person will leave home to visit all of their friends, and all their friends will also travel to visit them during the same day. A probability of 0.0 means nobody can leave home to visit anyone else, and a probability of 0.333 means there is a 33.3% random chance of each visit happening.

## Viral load

The virus spreads when a contagious person2 passes a viral load to a person they are visiting, or a person who has visited them. The term ‘viral load’ is a measure of the quantity of virus in the air which the other person breathes in when they are visiting and/or being visited by any contagious person. A person can be affected by a viral load even if they are already partly sick.


The viral load produced by a contagious person is given by the following formula (where L_v is the viral loadproduced, and HP_c is the number of health points of the contagious person who spreads the virus):


<img src="https://render.githubusercontent.com/render/math?math=L_v = 5 + \frac{(HP_c - 25)^2}{62}">


A small viral load will not make a healthy patient sick, but a larger viral load or viral loads from several people might reduce a patient’s health to the point that they become contagious with the disease and begin to spread it to others. 


Also, our Lv formula shows that a contagious person who is only mildly sick may produce a larger viral load than a person whose health has worsened, due to the nature of this disease. 


## Effect of infection
When a contagious person produces a viral load, every person they meet when visiting (or being visited) will be infected by their viral load. If the viral load is small, or a person is healthy, the person who is infected might not become sick, and they will quickly recover their health later when they sleep.


The change in health from receiving a viral load from another person is given by the following formula (where HPa is the current health points of the recipient before the viral load hits them, and HPb is the new value of person’s health points after receiving the viral load). The formula is different depending on the health of the person who receives the viral load:

if HP <= 29, HP = HP -(o.1 X L_V)


if 29 < HP < 50, HP = HP -(1.0 X L_V)


if HP >= 50, HP = HP -(2.0 X L_V)



Allowed libraries:


  • math
  
  
  • random
  
  
  • numpy
  
  
  • scipy
  
  
  • matplotlib
  
  
  • pandas

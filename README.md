# [Assesment 1 - GEOG5990](https://alikime.github.io/)

This task comprises of an online portfolio for the practical task. The project section contains the link to the Geog5990_final.py (Spyder - python file).

## To Run the Program
You need the following files;

Main program: Geog5990_final.py
Function files; distance_between.py 

Note that Main program must be in the same folder as function files.

To run, open the main program in either spyder or jupiter notebook for python and click run.

## Input/Output

The user initially defines the number of agents and number of iterations as input. 

Output: The program plots multiple agent coordinates (based on the number of agents defined as input, 20 for example)
The program also has the distance_between function; The function recieves as input; two arbitary agents (two rows in the agents list, each containing two values), and calculates how far apart they are, to produce the distance value as output. 

## Project Documentation 

### Overview 
In this project a main 'Model' program was built, this contains variables representing two agents' locations (y and x coordinates for each), the code provides the ability to move the locations around by user input, they'll start from some position, and then move one step in based on a random number.The program also provides the ability to work out the distance between the two locations.

These are two key elements of ABM: agents need to move, and they need to work out whether they are close enough to interact.

The algorithm for the program is presented below;

### Model
* Make a y variable.
* Make a x variable.
* Change y and x based on random numbers.
* Make a second set of y and xs, and make these change randomly as well.
* Work out the distance between the two sets of y and xs.

### Implementation:
* A file called model.py was created with Spyder 
* Two variable labels, "y0" and "x0" were made and assigned values 50 and 50.These variables will serve as location points, to be included into an agent code in subsequent steps.

Planned Developement of the Software; No further plans to develop the software.

## Preview
[![Resume Preview](https://github.com/Alikime/alikime.github.io/blob/master/img/PreviewImage.JPG)]
(https://alikime.github.io/)

**[View Live Preview](https://alikime.github.io/)**

## Reference

The template used for this task is free licenced template taken from Start Bootstrap - an open source library of free Bootstrap templates and themes. All of the free templates and themes on Start Bootstrap are released under the MIT license, which means you can use them for any purpose, even for commercial projects.

* https://startbootstrap.com
* https://twitter.com/SBootstrap

## Copyright and License

Copyright 2013-2018 Blackrock Digital LLC. Code released under the [MIT](https://github.com/BlackrockDigital/startbootstrap-resume/blob/gh-pages/LICENSE) license.

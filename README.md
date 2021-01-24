# python-challenge
This is the third homework for the University of Minnesota Data Visualization and Analytics Boot Camp using python.

This project uses python script to analyze two csv files and generate summaries. One is financial records of a company (PyBank) and the other is to modernize the vote counting process for a small town(PyPoll). 

Methodology for PyBank
1. Copied over a basic csv read instructions from activities in class
1. Ensured that the code was reading the correct csv files by generating both a print out of the path and the headers of the csv files, which was later removed
1. For the financial analysis the python script sets up a series of variables to store information to read back to during the for loop as the csv is being read
1. Set up a for loop to read from the csv and assign values to each of the necessary variables
1. Set up an if statement to read the largest and smallest change numbers and assign them to the correct variable
1. Sum all of the change values in the list and divide them by the number of rows minus one to get the correct average
1. Print the information to the terminal as well as make a txt file with the information

Methodology for PyPoll
1. Copied over a basic csv read instructions from activities in class
1. Ensured that the code was reading the correct csv files by generating both a print out of the path and the headers of the csv files, which was later removed
1. For the poll data analysis the python script uses a counter as the basis of the analysis
1. Use the counter to count votes and store them.
1. Print the results to the terminal as well as a txt file.

Limitations:
The PyPoll script depends on you to copy the results from the terminal to report out to the txt file, which is not ideal.

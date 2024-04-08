#Requirements
#Must code a deterministic function that takes a 2 or more arguments and returns a value

#Must start up multiple-processes and executes this function in parallel within the created, distinct processes

#Function arguments should be randomly generated

#Note that the function itself should not generate the random values

#Must save the function inputs and the function's returned value into a SQLite database

#Must generate an unique identifer for each function call

#Before the function is called, the inputs and identifier must be committed as a new row into the database

#When the results are returned from the function, these values must be updated into the existing corresponding row

#Each row should represent an execution of the function, a data-point

#Must allow specification of a user-specified number of data-points/rows to create

#The database should end-up with this number of data-points/rows when the script completes

#If the database already has this number or more, then the script should end immediately

#Must print-out to console each time data is saved to database

#In a separate script, must pull data from database and create a plot that visualizes the data-points in a scatter plot, color-coded by the result-value (if you have more than 2 function input parameters, choose any 2 of the parameters)

#Points will be deduced for each significant-requirement violation.

#Must employ parallel processing in algorithm

#Must avoid using existing modules/libraries that directly implement the algorithm's specialized logic

#Must type all the code by hand; no copying and pasting code from ChatGPT or another implementation

#Must store code in a Git repo (such as either git.antcenter.net or GitHub)

#Must configure Git repo to execute your unit tests on code changes

#Must have Git repo successfully run your unit tests for all capabilities that do not have bugs

#Must use a .gitignore file with the proper configuration of the programming language used

#Must specify dependencies through a programming language standard, such as through a requirements.txt file or the newer pyproject.toml file

#See https://packaging.python.org/en/latest/tutorials/packaging-projects/ Links to an external site.for advanced options to organize files for distribution

#Must demonstrate implementation with three datasets (two test datasets, one challenge dataset)

#Must allow hyper-parameter specification from users of module

#Must be free of major bugs that prevent itself from fulfilling purpose

#Must comment or document all unresolved minor bugs 

#Must work with other datasets that may not have the same number of variables or types of variables

#Can review existing implementations of the algorithm to get ideas on how to implement

#Can use the following Python modules without restrictions: numpy, pandas, multiprocessing, mpi4py, numba, sympy

#change to be tracked


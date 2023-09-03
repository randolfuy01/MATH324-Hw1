# Assignment1CSC324

Using aninteresting numberical data of your own which is not too small, find the following unit of measurements
mean (complete)
five number summary (complete)
boxplot (complete)
Based on the above comment on the:
Center of the data, Spread of the data
Shape of the data
Outlirers in the data
Is the data skewed? If yes, explain why. If no, explaion why not.
Find a density histogram and mention the breaks used.

For this dataset, I decided to use a dataset I found in Kaggle which is a NBA players dataset. For this I wanted to see the distribution of the players who are drafted based on their heights.
I needed to imoprt the csv data as floats instead of strings but that wasn't possible / difficult to do straight from reading from the csv. So my solution was to convert it to a pandas dataframe, get the column for players heights, conver that to a list, take that list and work with the data. 

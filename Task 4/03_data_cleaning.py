import pandas
from termcolor import colored as c

"""


Usually when working with data we:
1. Look at the data
2. What's the quality of data?
3. Is there something in there that we will never use?
4. Deletion of unusable data / filling in missing data
5. Research - looking at graphs from this data and results of statistical analysis
6. Report

Your task:
0. All outputs need to be accompanied by full short sentence explaining what is being output. - 1point

1. open csv - 0.5point
https://pandas.pydata.org/docs/reference/io.html

2. output column names and using info function output information about table - 1point 
https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html in Attributes and Methods sections

Further you will need to use https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html in Methods sections

3. output a random sample line - 1point

4. check for isnull on all columns, output total empty cells - 1points
Additionally you will need sum and any functions

5. Delete column "normalized-losses", check again for empty spaces, this time output per column - 2 points

6. Find lines 52, 53 and 60. Output by using iloc function. - 1point

7. Fill in column "bore" with columns "bore" mean value
   Fill in column "stroke" with column "stroke" median value
   Fill in column "num-of-doors" with column "num-of-doors" mode value
   1.5 points

8. Explain what is mean, median and mode in context of filling in values with statistical values. (Short, precise explanation) - 1.5 poins


9. Save the result in "result.xlsx" in one sheet - 0.5 points


"""
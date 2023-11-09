"""
xls, xlsx, csv
xls - older format, less rows and less columns - don't use it anymore
xlsx - limit of rows ~1m, if you try to do any type of analysis with more that 300k rows - mostly the limitation is your device - everything becomes glitchy
csv - kinda old format, but no limit on row count, the limit is your laptop RAM and maybe power options

Libraries - are previously written code that you download trough terminal 
To download you write:
pip install numpy

numpy
1.21< OK
1.21.6 - there is looser checks for correct data shape
1.24< - it requires strict coding
is library that provides additonal calculations - such as more efficient lists, calculations and arange (range function with float variable)
it's uses as basis for other libraries 

xlwt, xlrd
libraries that provide read and write functionality for xls files

openpyxl
it provides read and write for xlsx format, it is being renewed (new version, optimisation for this library) 

pandas
uses openpyxl, numpy (and xlwt, xlrd) to open data and work with it

all imports are supposted to be located at the top of file

Extensions: Excel Viewer, CSV Rainbow

import
functions
code
"""

import pandas

# by default if you don't write sheet name or there is only one sheet - it will open the first sheet no matter the shee name
info = pandas.read_excel("animals.xls")

# output all table
print(info)
# output first 2 rows
print(info.head(2))
# output last 2 rows
print(info.tail(2))
# output table size
# table size is built in part of the table (DataFrame which consist of column name - index and series - data rows)
print("table size", info.shape) # rows, columns
print("rows:", info.shape[0])
print("columns:", info.shape[1])

# read other data sheet
info2 = pandas.read_excel("animals.xls", sheet_name = "Sheet2")
# if we wanted to read both pages at the same time 
# sheet_name = ["Sheet1", "Sheet2"]
print(info2)

# join both tables together
# methods may vary - depending on year
# before it was ok to use just append
# concat - concatanation
joined_tables = pandas.concat([info,info2])
print(joined_tables)

# sort data
sorted_data = joined_tables.sort_values("Age")
print(sorted_data)
sorted_data = joined_tables.sort_values("Age", ascending=False) # this DESC
print(sorted_data)

# save the result in one sheet
sorted_data.to_excel("joined_animals.xlsx", index=False)
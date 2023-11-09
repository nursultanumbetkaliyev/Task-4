"""
termcolor
this library provides coloring of output in terminal
it is supported by VS Code itself and partially supported by operating systems
red, green, blue, cyan, magenta, yellow, black, white
"""
from termcolor import colored as c
import pandas

file = pandas.ExcelFile("bookshop.xlsx")

pages = []

# output all page names
print(c(f"Page names:","green"))
print(file.sheet_names) # sheet_names is part of the variable and not a function

# add page to list of pages
for page_name in file.sheet_names:
    pages.append(file.parse(page_name))

# output column names
print(c(f"Column names:", "blue"))
print(pages[0].columns) # no brackets


# calculate all empty columns
# .isnull() .notnull() .sum() .mean() .any() etc
# print(c(f"Empty spaces: \n{pages[0].isnull().any()}", "blue"))
print(c(f"Empty spaces: {pages[0].isnull().sum().sum()}", "blue"))


"""
Markup is 30% (0.3)
Placement cost is 0.07 per unit
Price per unit is (Out of pocket price + placement price ) + Markup
Wages are from sales of unit, it's calculated from Unit price as 3%
Total is Price per unit * count
Profit is per all, take out all expenses.
"""
# 'No', 'Author', 'Name', 'Date', 'Count', 'Out-of-pocket-cost','Price per unit', 'Markup', 'Placement cost', 'Wages', 'Total','Profit'
pages[0]["Markup"] = pages[0]["Out-of-pocket-cost"] * 0.3
print(pages[0]["Markup"])
pages[0]["Placement"] = pages[0]["Count"] * 0.07
pages[0]["Price per unit"] = (pages[0]["Out-of-pocket-cost"] + 0.07)  + pages[0]["Markup"]
pages[0]["Wages"] = pages[0]["Price per unit"] * 0.03
pages[0]["Total"] = pages[0]["Price per unit"] * pages[0]["Count"]
pages[0]["Profit"] = pages[0]["Total"] - pages[0]["Wages"] * pages[0]["Count"] - pages[0]["Placement"] - pages[0]["Out-of-pocket-cost"] * pages[0]["Count"]

print(pages[0][["Placement","Price per unit", "Wages", "Total","Profit"]])

# you've edited this info in page with index 0
# add this page to list of pages as new page
pages.append(pages[0])
# add total (sum) per column in page with index 0
new_line = pages[1][["Placement","Price per unit", "Wages", "Total","Profit"]].sum()
print(c("Adding total line","green"))
print(new_line)
print(type(new_line))

rotated_line = pandas.DataFrame(data = new_line).T
# t - transpone - rotate
print(rotated_line)

line = rotated_line.reindex(columns=pages[1].columns)
print(line)

pages[1] = pandas.concat([pages[1], line])
print(pages[1].tail(3))

# create another copy of page with index 0
# pages.append(pages[0])
grouped_data = pages[0][["Date","Count", "Total"]].groupby("Date").sum()
print(c("Grouped data", "green"))
print(grouped_data)
grouped_data = grouped_data.reset_index()
print(grouped_data)

# find all the data for 24th october 2020
print(c("Filter data","green"))
filter = grouped_data["Date"] == "2020-10-24"
print(filter)
print(grouped_data[filter])
# print(grouped_data[~filter])
pages.append(grouped_data)

# save all pages in one file as separate sheets
counter = 1
with pandas.ExcelWriter("result.xlsx") as file:
    for page in pages:
        page.to_excel(file, sheet_name=str(counter), index=False)
        counter += 1


import pandas as pd

excel_file = 'Assignment_Timecard.xlsx';

#  Take the file as an input

df = pd.read_excel(excel_file);

data = df['Pay Cycle End Date']-df['Pay Cycle Start Date']

data2 = df['Time Out']-df['Time']



df2 = df.assign( Days = data,WorkHour = data2)


# who has worked for 7 consecutive days.

df3 = df2.sort_values('Days')==7

print(df3)

# Who has worked for more than 14 hours in a single shift
df4 = df2.sort_values('WorkHour')==14

print(df4)

#  who have less than 10 hours of time between shifts but greater than 1 hour
cond1 = df2.WorkHour > 1
cond2 = df2.WorkHour< 10

df5 = df2.where(cond1 | cond2 ,'NA',inplace=True)
print(df5)
 





# 2. Provide a program to read the CSV file.
# • CSV file has three columns, the first column names, the second column is birthdate(YYYYMM-
# DD) the third column is salary.
# • Read the file and display the data and age in the terminal.
# • The file path, delimiter, and quote char are the input by the user.
# • The program has to work from the terminal. The input and output have been taken/displayed
# on the terminal.



import pandas as pd
from datetime import datetime
from datetime import date



def calculate_age(born1):
    #born1 = datetime.strptime(born1, "%Y-%m-%d").date()
    today = date.today()
    return today.year - born1.year - ((today.month, today.day) < (born1.month, born1.day))


try:
    filename=input(" Enter Filename/path (For default enter Employees.csv)- ")
    delm=input("Enter delimiter (For default enter ',') - ")
    d=pd.read_csv(filename,sep = delm) 
    df = pd.DataFrame(data= d)
    
    df['birthdate'] = pd.to_datetime(df['birthdate'])

    df['age'] = df['birthdate'].apply(calculate_age)
    print(df)
        
    df.to_csv('filename')
except Exception as e:
    print(e)




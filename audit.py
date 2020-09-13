
# coding: utf-8

# In[ ]:

def change_column_names(df):
        print ("Your selected data has " + str(df.shape[1]) + " columns.\n"      
            "They are: ")
        for x in range(0, df.shape[1]):
            print(df.columns[x])
        print("\n")
        print("Which column do you want to change?")
        b = str(input())
        print ("What name it should have?")
        n = str(input())
        df.rename(columns={b: n}, inplace=True)
        print("\n")
        print(list(df.columns))
        print("\n")
        print("For other changes repeat the function")


# In[2]:

def missing_values_table(df):
        import pandas as pd
        mis_val = df.isnull().sum()
        mis_val_percent = 100 * df.isnull().sum() / len(df)
        mis_val_table = pd.concat([mis_val, mis_val_percent], axis=1)
        mis_val_table_ren_columns = mis_val_table.rename(
        columns = {0 : 'Missing Values', 1 : '% of Total Values'})
        mis_val_table_ren_columns = mis_val_table_ren_columns[
            mis_val_table_ren_columns.iloc[:,1] != 0].sort_values(
        '% of Total Values', ascending=False).round(1)
        print ("Your selected dataframe has " + str(df.shape[1]) + " columns.\n"      
            "There are " + str(mis_val_table_ren_columns.shape[0]) +
              " columns that have missing values.")

        return mis_val_table_ren_columns


# In[ ]:

def summary_by_account(df):
    print("Select the name of the Account column:")
    x = str(input())
    print("Select the name of the AccountDesc column:")
    y = str(input())
    table = df.groupby([x,y]).sum().round(2)
    print("Do you want to save it as excel file? Yes or No")
    z = str(input())
    if z == "Yes":
        table.to_excel('summary_by_account.xlsx')
        print('Excel file was saved')
        
    else:
        print('No Excel file was saved')
    return table

# In[ ]:

def summary_by_account_period(df):
    print("Select the name of the Account column:")
    x = str(input())
    print("Select the name of the Period column:")
    y = str(input())
    table = df.groupby([x, y]).sum().round(2)
    print("Do you want to save it as excel file? Yes or No")
    z = str(input())
    if z == "Yes":
        table.to_excel('summary_by_account_period.xlsx')
        print('Excel file was saved')

    else:
        print('No Excel file was saved')
    return table


# In[ ]:

def summary_by_specific_account_period(df):
    print("Select the name of the Account column:")
    x = str(input())
    print("Select the account number in a provided period xx-xx-xxxx:")
    z = str(input())
    print("Select the column which contains the period:")
    y = str(input())
    print("Select the period in format yyyy-m")
    n = str(input())
    
    table = df.loc[(df[x] == z) & (df[y] == n)]
    print("There are " + str(table.shape[0])+ " items found")
    print("Do you want to save it as excel file? Yes or No")
    p = str(input())
    if p == "Yes":
        table.to_excel('summary_by_specific_account_period.xlsx')
        print('Excel file was saved')
        
    else:
        print('No Excel file was saved')
    return table


# In[ ]:

def summary_by_specific_account(df):
    print("Select the name of the Account column:")
    x = str(input())
    print("Select the account number in a provided period xx-xx-xxxx:")
    y = str(input())
    table = df.loc[(df[x] == y)]
    print("Do you want to save it as excel file? Yes or No")
    p = str(input())
    if p == "Yes":
        table.to_excel('summary_by_specific_account.xlsx')
        print('Excel file was saved')
    else:
        print('No Excel file was saved')
    print("There are " + str(table.shape[0])+ " items found")
    return table


# In[ ]:

def summary_by_noname_account(df):
    print("Select the name of the AccountDesc column:")
    x = str(input())
    print("Select the column which contains the period:")
    y = str(input())
    table = df.groupby([x,y]).sum().round(2)
    print("There are " + str(table.shape[0])+ " items found")
    print("Do you want to save it as excel file? Yes or No")
    p = str(input())
    if p == "Yes":
        table.to_excel('summary_by_noname_account.xlsx')
        print('Excel file was saved')
    else:
        print('No Excel file was saved')
    return table


# In[ ]:

def summary_by_JnlNo(df):
    print("Select the name of the JnlNo column:")
    x = str(input())
    print("Select the name of the Amount column:")
    z = str(input())
    
    table = df.groupby([x]).sum().round(2).loc[df.groupby([x]).sum().round(2)[z] != 0]
    print ("Journals with amount not equal to 0")
    print("There are " + str(table.shape[0])+ " items found")
    print("Do you want to save it as excel file? Yes or No")
    p = str(input())
    if p == "Yes":
        table.to_excel('summary_by_JnlNo.xlsx')
        print('Excel file was saved')
    else:
        print('No Excel file was saved')
    return table


# In[ ]:

def summary_by_items_posted_before_6(df):
    print("Select the name of the time column:")
    x = str(input())
    table = df.loc[(df[x] <'06:00')]
    print("There are " + str(table.shape[0])+ " items found")
    print ("Journals with items before 6 am")
    print("Do you want to save it as excel file? Yes or No")
    p = str(input())
    if p == "Yes":
        table.to_excel('summary_by_items_posted_before_6.xlsx')
        print('Excel file was saved')
    else:
        print('No Excel file was saved')
    return table


# In[ ]:

def summary_by_amount(df):
    print("Select the name of the Absolute Amount column:")
    x = str(input())
    table = df.loc[df[x]>=150000]
    print("There are " + str(table.shape[0])+ " items found")
    print ("Items with amount > 150000")
    print("Do you want to save it as excel file? Yes or No")
    p = str(input())
    if p == "Yes":
        table.to_excel('summary_by_amount.xlsx')
        print('Excel file was saved')
    else:
        print('No Excel file was saved')
    return table


# In[ ]:

def summary_by_period(df):
    print("Select the name of the Period column:")
    x = str(input())
    table = df.groupby([x]).sum().round(2)
    print("There are " + str(table.shape[0])+ " items found")
    print ("Summary by period")
    print("Do you want to save it as excel file? Yes or No")
    p = str(input())
    if p == "Yes":
        table.to_excel('summary_by_period.xlsx')
        print('Excel file was saved')
    else:
        print('No Excel file was saved')
    return table


# In[ ]:

def summary_by_journal_type(df):
    print("Select the name of the Journal type column:")
    x = str(input())
    table = df.groupby([x]).sum()
    print("There are " + str(table.shape[0])+ " items found")
    print ("Summary by journals")
    print("Do you want to save it as excel file? Yes or No")
    p = str(input())
    if p == "Yes":
        table.to_excel('summary_by_journal_type.xlsx')
        print('Excel file was saved')
    else:
        print('No Excel file was saved')
    return table


# In[ ]:

def summary_by_journal_perfomance(df):
    print("Select the name of the Amount regarding the perofomance column:")
    x = str(input())
    table = df.loc[df[x]>=150000]
    print("There are " + str(table.shape[0])+ " items found")
    print ("Summary by perfomance")
    print("Do you want to save it as excel file? Yes or No")
    p = str(input())
    if p == "Yes":
        table.to_excel('summary_by_journal_perfomance.xlsx')
        print('Excel file was saved')
    else:
        print('No Excel file was saved')
    return table


# In[ ]:

def summary_by_user(df):
    print("Select the name of the user/JnlPrep regarding column:")
    x = str(input())
    table = df.groupby([x]).sum()
    print("There are " + str(table.shape[0])+ " items found")
    print ("Summary by JnlPrep")
    print("Do you want to save it as excel file? Yes or No")
    p = str(input())
    if p == "Yes":
        table.to_excel('summary_by_user.xlsx')
        print('Excel file was saved')
    else:
        print('No Excel file was saved')
    return table


# In[ ]:

def summary_by_authoriser(df):
    print("Select the name of the user/JnlAuth regarding column:")
    x = str(input())
    table = df.groupby(['JnlAuth']).sum()
    print("There are " + str(table.shape[0])+ " items found")
    print ("Summary by JnlPrep")
    print("Do you want to save it as excel file? Yes or No")
    p = str(input())
    if p == "Yes":
        table.to_excel('summary_by_authoriser.xlsx')
        print('Excel file was saved')
    else:
        print('No Excel file was saved')
    return table


# In[ ]:

def summary_by_authoriser_user(df):
    print("Select the name of the JnlPrep regarding column:")
    x = str(input())
    print("Select the name of the JnlAuth regarding column:")
    y = str(input())
    table = df.groupby([y,x]).sum().round(2)
    print("There are " + str(table.shape[0])+ " items found")
    print ("Summary by JnlPrep")
    print("Do you want to save it as excel file? Yes or No")
    p = str(input())
    if p == "Yes":
        table.to_excel('summary_by_authoriser_user.xlsx')
        print('Excel file was saved')
    else:
        print('No Excel file was saved')
    return table
        


# In[ ]:

def summary_by_authoriser_user_equal(df):
    print("Select the name of the JnlPrep regarding column:")
    x = str(input())
    print("Select the name of the JnlAuth regarding column:")
    y = str(input())
    table = df.loc[df[y] == df[x]].groupby([y,x]).sum().round(2)
    print("There are " + str(table.shape[0])+ " items found")
    print ("Summary by JnlPrep")
    print("Do you want to save it as excel file? Yes or No")
    p = str(input())
    if p == "Yes":
        table.to_excel('summary_by_authoriser_user_equal.xlsx')
        print('Excel file was saved')
    else:
        print('No Excel file was saved')
    return table


# In[ ]:

def Items_no_description(df):
    print("Select the name of the AccountDesc regarding column:")
    x = str(input())
    table = df[df[x] == '']
    print("There are " + str(table.shape[0])+ " items found")
    print ("Summary by items with no description")
    print("Do you want to save it as excel file? Yes or No")
    p = str(input())
    if p == "Yes":
        table.to_excel('Items_no_description.xlsx')
        print('Excel file was saved')
    else:
        print('No Excel file was saved')
    return table


# In[ ]:

def general_summary_by_authoriser_user_equal(df):
    print("Select the name of the JnlPrep identificator column:")
    x = str(input())
    print("Select the name of the JnlAuth identificator column:")
    y = str(input())
    table = df.loc[df[y] == df[x]]
    print("There are " + str(table.shape[0])+ " items found where authoriser and user are the same.")
    return table

# In[ ]:

def general_summary_by_JnlNo(df):
    print("Select the name of the Journal identificator column:")
    x = str(input())
    print("Select the name of the Amount identificator column:")
    z = str(input())

    table = df.groupby([x]).sum().round(2).loc[df.groupby([x]).sum().round(2)[z] != 0]
    print("There are " + str(table.shape[0]) + " Unbalanced journals with amount not equal to 0")
    return table

# In[ ]:

def general_info(df):
    print("Select the name of Account identificator column")
    x = str(input())
    print("Select the name of Transaction descriptions identificator column")
    y = str(input())
    print("Select the name of Period column")
    u = str(input())
    print("Select the name of JnlPrep  identificator column")
    i = str(input())
    print("Select the name of JnlAuth identificator column")
    o = str(input())
    print ("Your selected data has " + str(df[x].nunique()) + " unique Accounts.")
    print ("Your selected data has " + str(df[y].nunique()) + " unique Transaction descriptions.")
    print ("Your selected data has " + str(df[u].nunique()) + " Periods.")
    print ("Your selected data has " + str(df[i].nunique()) + " unique JnlPrep values.")
    print ("Your selected data has " + str(df[o].nunique()) + " unique JnlAuth values.")

# In[ ]:

def summary_by_JnlPrep_perfomance(df):
    print("Select the name of the JnlPrep identificator column:")
    x = str(input())
    calc = df.groupby([x]).sum().round(1)
    table = calc.loc[calc['AbsAmount'] > 150000]
    print("Do you want to save it as excel file? Yes or No")
    z = str(input())
    if z == "Yes":
        table.to_excel('summary_by_JnlPrep_perfomance.xlsx')
        print('Excel file was saved')

    else:
        print('No Excel file was saved')
    return table

# In[ ]:

def summary_by_JnlAuth_perfomance(df):
    print("Select the name of the JnlAuth identificator column:")
    x = str(input())
    calc = df.groupby([x]).sum().round(1)
    table = calc.loc[calc['AbsAmount'] > 150000]
    print("Do you want to save it as excel file? Yes or No")
    z = str(input())
    if z == "Yes":
        table.to_excel('summary_by_JnlAuth_perfomance.xlsx')
        print('Excel file was saved')

    else:
        print('No Excel file was saved')
    return table

# In[ ]:

def summary_by_journal_perfomance(df):
    print("Select the name of the Journal identificator column:")
    x = str(input())
    calc = df.groupby([x]).sum().round(1)
    table = calc.loc[calc['AbsAmount'] > 150000]
    print("Do you want to save it as excel file? Yes or No")
    z = str(input())
    if z == "Yes":
        table.to_excel('summary_by_journal_perfomance.xlsx')
        print('Excel file was saved')

    else:
        print('No Excel file was saved')
    return table

# In[ ]:

def summary_by_account_perfomance(df):
    print("Select the name of the Account identificator column:")
    x = str(input())
    calc = df.groupby([x]).sum().round(1)
    table = calc.loc[calc['AbsAmount'] > 150000]
    print("Do you want to save it as excel file? Yes or No")
    z = str(input())
    if z == "Yes":
        table.to_excel('summary_by_account_perfomance.xlsx')
        print('Excel file was saved')

    else:
        print('No Excel file was saved')
    return table

# In[ ]:

def information(df):
    print ("Your selected data has " + str(df.shape[1]) + " columns.\n"      
            "They are: ")
    for x in range(0, df.shape[1]):
        print(df.columns[x])
    print("\n")
    print("Select the name of Account identificator column")
    x = str(input())
    print("Select the name of Transaction descriptions identificator column")
    y = str(input())
    print("Select the name of Period column")
    u = str(input())
    print("Select the name of JnlPrep  identificator column")
    i = str(input())
    print("Select the name of JnlAuth identificator column")
    o = str(input())
    print("Select the name of the time column")
    l = str(input())
    print("Select the Debit column")
    k = str(input())
    calc = df.groupby([x]).sum().round(1)
    table = calc.loc[calc['AbsAmount'] > 150000]
    table1 = df.loc[df[o] == df[i]].groupby([o,i]).sum().round(2)
    print ("Your selected data has " + str(df[x].nunique()) + " unique Accounts.")
    print ("Your selected data has " + str(df[y].nunique()) + " unique Transaction descriptions.")
    print ("Your selected data has " + str(df[u].nunique()) + " Periods.")
    print ("Your selected data has " + str(df[i].nunique()) + " unique JnlPrep values.")
    print ("Your selected data has " + str(df[o].nunique()) + " unique JnlAuth values.")
    print("\n\nHere is the information available for certain data set:\n")
    print (df.info())
    print ('\n\nThere are ' + str(df.loc[(df[l] <'06:00')].shape[0]) + " transactions posted before 6 am")
    print ("There are " + str(df.loc[(df[l] >'18:00')].shape[0]) +" transactions posted after 6 pm" )
    print ("There are " + str(table.shape[0]) + " accounts which absolute amount is more than 150.000")
    print ("There are " + str(table1.shape[0]) + " account where user is the same as authoriser")
    print ("\nAccount with the highest Debit/Credit value is " + str(df.loc[data[k]==max(data[k])][x]))
    print ('\n\nHere is the statistical information available for certain data set')
    return df.describe().round(2)
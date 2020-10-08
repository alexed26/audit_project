
# coding: utf-8

# In[ ]:
#----------------------------------------Manipulative part-------------------------------------------------
#----------------------------------------------------------------------------------------------------------

# In[1]:

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

#----------------------------------------Extracting General Information------------------------------------
#----------------------------------------------------------------------------------------------------------

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

# In[3]:

def maxamount_by_period(df):
    print("Select the name of the amount column:")
    t = str(input())
    print("Select the column which contains the period:")
    y = str(input())
    print('Max transaction for each period:')
    period_nums = df[y].unique()
    for x in range(0, period_nums.shape[0]):
        print("\n--------------------------------------" + period_nums[x] + "-------------------------------------\n")
        ttt=df.loc[df[y] == period_nums[x]]
        display(ttt.loc[ttt[t] == max(ttt[t])])

# In[4]:

def transactions_by_period(df):
    print("Select the column which contains the period:")
    y = str(input())
    period_nums = df[y].unique()
    for x in range(0, period_nums.shape[0]):
        print("Below is the total amount of transactions for the following period " + period_nums[x] + ":")
        print(df.loc[df[y] == period_nums[x]].shape[0])

# In[5]:

def total_amount_for_periods(df):
    print("Select the name of the amount column:")
    t = str(input())
    print("Select the column which contains the period:")
    y = str(input())
    period_nums = df[y].unique()
    for x in range(0, period_nums.shape[0]):
        print("Below is the total amount for the following period " + period_nums[x] + ":")
        print(df.loc[df[y] == period_nums[x]][t].sum().round(2))

# In[6]:

def information(df):
    print ("Your selected data has " + str(df.shape[1]) + " columns.\n"      
            "They are: ")
    for x in range(0, df.shape[1]):
        print(df.columns[x])
    print("\n")
    print("Select the name of account identificator column")
    x = str(input())
    print("Select the name of transaction descriptions identificator column")
    y = str(input())
    print("Select the name of period column")
    u = str(input())
    print("Select the name of user  identificator column")
    i = str(input())
    print("Select the name of authoriser identificator column")
    o = str(input())
    print("Select the name of the time column")
    l = str(input())
    print("Select the Debit column")
    k = str(input())
    calc = df.groupby([x]).sum().round(1)
    table = calc.loc[calc['AbsAmount'] > 150000]
    table1 = df.loc[df[o] == df[i]].groupby([o,i]).sum().round(2)
    print ("Your selected data has " + str(df[x].nunique()) + " unique accounts.")
    print ("Your selected data has " + str(df[y].nunique()) + " unique transaction descriptions.")
    print ("Your selected data has " + str(df[u].nunique()) + " Periods.")
    print ("Your selected data has " + str(df[i].nunique()) + " unique users values.")
    print ("Your selected data has " + str(df[o].nunique()) + " unique authorisers values.")
    print("\n\nHere is the information available for certain data set:\n")
    print (df.info())
    print ('\n\nThere are ' + str(df.loc[(df[l] <'06:00')].shape[0]) + " transactions posted before 6 am")
    print ("There are " + str(df.loc[(df[l] >'18:00')].shape[0]) +" transactions posted after 6 pm" )
    print ("There are " + str(table.shape[0]) + " accounts which absolute amount is more than 150.000")
    print ("There are " + str(table1.shape[0]) + " account where user is the same as authoriser")
    print ("\nAccount with the highest Debit/Credit value is " + str(df.loc[df[k]==max(df[k])][x]))
    print ('\n\nHere is the statistical information available for certain data set')
    return df.describe().round(2)

#----------------------------------Summary by account test-------------------------------------------------
#----------------------------------------------------------------------------------------------------------
# In[8]:

def summary_by_two_variables(df):
    print("Select the name of the first column for grouping:")
    x = str(input())
    print("Select the name of the second column for grouping")
    y = str(input())
    table = df.groupby([x, y]).sum().round(2)
    print("Do you want to save it as excel file? Yes or No")
    z = str(input())
    if z == "Yes":
        table.to_excel('summary_by_two_variables.xlsx')
        print('Excel file was saved')
    else:
        print('No Excel file was saved')
    return table

# In[9]:

def summary_by_one_variable(df):
    print("Select the column name for grouping")
    x = str(input())
    table = df.groupby([x]).sum().round(2)
    print("Do you want to save it as excel file? Yes or No")
    z = str(input())
    if z == "Yes":
        table.to_excel('summary_by_one_variable.xlsx')
        print('Excel file was saved')
    else:
        print('No Excel file was saved')
    return table

# In[10]:

def summary_by_account_and_description(df):
    print("Select the name of the account number column:")
    x = str(input())
    print("Select the name of the account description column:")
    y = str(input())
    table = df.groupby([x,y]).sum().round(2)
    print("Do you want to save it as excel file? Yes or No")
    z = str(input())
    if z == "Yes":
        table.to_excel('summary_by_account_and_description.xlsx')
        print('Excel file was saved')
    else:
        print('No Excel file was saved')
    return table


# In[11]:

def summary_by_accountnumber(df):
    print("Select the name of the account number column:")
    x = str(input())
    table = df.groupby([x]).sum().round(2)
    print("Do you want to save it as excel file? Yes or No")
    z = str(input())
    if z == "Yes":
        table.to_excel('summary_by_accountnumber.xlsx')
        print('Excel file was saved')
    else:
        print('No Excel file was saved')
    return table

#----------------------------------Summary by period-------------------------------------------------------
#----------------------------------------------------------------------------------------------------------

# In[12]:

def summary_by_period(df):
    print("Select the name of the period column:")
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


# In[13]:

def summary_by_account_and_period(df):
    print("Select the name of the account column:")
    x = str(input())
    print("Select the name of the period column:")
    y = str(input())
    table = df.groupby([x, y]).sum().round(2)
    print("Do you want to save it as excel file? Yes or No")
    z = str(input())
    if z == "Yes":
        table.to_excel('summary_by_account_and_period.xlsx')
        print('Excel file was saved')

    else:
        print('No Excel file was saved')
    return table


# In[14]:

def summary_by_specific_account_and_period(df):
    print("Select the name of the account column:")
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
        table.to_excel('summary_by_specific_account_and_period.xlsx')
        print('Excel file was saved')
    else:
        print('No Excel file was saved')
    return table


# In[15]:

def summary_by_specific_period(df):
    print("Select the name of the account column:")
    x = str(input())
    print("Select the account number in a provided period xx-xx-xxxx:")
    y = str(input())
    table = df.loc[(df[x] == y)]
    print("Do you want to save it as excel file? Yes or No")
    p = str(input())
    if p == "Yes":
        table.to_excel('summary_by_specific_period.xlsx')
        print('Excel file was saved')
    else:
        print('No Excel file was saved')
    print("There are " + str(table.shape[0])+ " items found")
    return table

#-------------------------Summary by journal number--------------------------------------------------------
#----------------------------------------------------------------------------------------------------------
# In[16]:

def summary_by_journal(df):
    print("Select the name of the journal number column:")
    x = str(input())
    table = df.groupby([x]).sum().round(2)
    print("Do you want to save it as excel file? Yes or No")
    z = str(input())
    if z == "Yes":
        table.to_excel('summary_by_journal.xlsx')
        print('Excel file was saved')

    else:
        print('No Excel file was saved')
    return table

# In[16]:

def summary_by_journal_type(df):
    print("Select the name of the journal type column:")
    x = str(input())
    table = df.groupby([x]).sum().round(2)
    print("Do you want to save it as excel file? Yes or No")
    z = str(input())
    if z == "Yes":
        table.to_excel('summary_by_journal_type.xlsx')
        print('Excel file was saved')

    else:
        print('No Excel file was saved')
    return table

# In[17]:

def unbalanced_journals(df):
    print("Select the name of the journal number column:")
    x = str(input())
    print("Select the name of the amount column:")
    z = str(input())
    table = df.groupby([x]).sum().round(2).loc[df.groupby([x]).sum().round(2)[z] != 0]
    print ("Journals with amount not equal to 0")
    print("There are " + str(table.shape[0])+ " items found")
    print("Do you want to save it as excel file? Yes or No")
    p = str(input())
    if p == "Yes":
        table.to_excel('unbalanced_journals.xlsx')
        print('Excel file was saved')
    else:
        print('No Excel file was saved')
    return table

#----------------------------Items posted out of working time----------------------------------------------
#----------------------------------------------------------------------------------------------------------
# In[18]:

def transaction_posted_before_6AM(df):
    print("Select the name of the time column:")
    x = str(input())
    table = df.loc[(df[x] <'06:00')]
    print("There are " + str(table.shape[0])+ " transactions before 6 AM found")
    print("Do you want to save it as excel file? Yes or No")
    p = str(input())
    if p == "Yes":
        table.to_excel('summary_by_items_posted_before_6AM.xlsx')
        print('Excel file was saved')
    else:
        print('No Excel file was saved')
    return table

# In[19]:

def transactions_posted_after_6PM(df):
    print("Select the name of the time column:")
    x = str(input())
    table = df.loc[(df[x] >'18:00')]
    print("There are " + str(table.shape[0])+ " transactions after 6 PM found")
    print("Do you want to save it as excel file? Yes or No")
    p = str(input())
    if p == "Yes":
        table.to_excel('summary_by_items_posted_after_6PM.xlsx')
        print('Excel file was saved')
    else:
        print('No Excel file was saved')
    return table

#------------------------Transaction where amount over 150000----------------------------------------------
#----------------------------------------------------------------------------------------------------------
# In[20]:

def transactions_over_150000(df):
    print("Select the name of the amount regarding the perofomance column:")
    x = str(input())
    table = df.loc[df[x]>=150000]
    print("There are " + str(table.shape[0])+ " transactions found")
    print("Do you want to save it as excel file? Yes or No")
    p = str(input())
    if p == "Yes":
        table.to_excel('transactions_over_150000.xlsx')
        print('Excel file was saved')
    else:
        print('No Excel file was saved')
    return table

# In[21]:

def user_amount_over_150000(df):
    print("Select the name of the user column:")
    x = str(input())
    calc = df.groupby([x]).sum().round(1)
    table = calc.loc[calc['AbsAmount'] > 150000]
    print("Do you want to save it as excel file? Yes or No")
    z = str(input())
    if z == "Yes":
        table.to_excel('JnlPrep_amount_over_150000.xlsx')
        print('Excel file was saved')

    else:
        print('No Excel file was saved')
    return table

# In[22]:

def authoriser_amount_over_150000(df):
    print("Select the name of the authoriser column:")
    x = str(input())
    calc = df.groupby([x]).sum().round(1)
    table = calc.loc[calc['AbsAmount'] > 150000]
    print("Do you want to save it as excel file? Yes or No")
    z = str(input())
    if z == "Yes":
        table.to_excel('JnlAuth_amount_over_150000.xlsx')
        print('Excel file was saved')

    else:
        print('No Excel file was saved')
    return table

# In[23]:

def GroupByVariable_amount_over_value(df):
    print("Select the name of the variable to group by")
    x = str(input())
    print("Select the value exceed which the data should be")
    y = int(input())
    calc = df.groupby([x]).sum().round(1)
    table = calc.loc[calc['AbsAmount'] > y]
    print("Do you want to save it as excel file? Yes or No")
    z = str(input())
    if z == "Yes":
        table.to_excel('GroupByVariable_amount_over_150000.xlsx')
        print('Excel file was saved')

    else:
        print('No Excel file was saved')
    return table

def transactions_over_value(df):
    print("Select the name of the amount regarding the perofomance column:")
    x = str(input())
    print("Select the value exceed which the data should be")
    y = int(input())
    table = df.loc[df[x]>=y]
    print("There are " + str(table.shape[0])+ " transaction over set value found")
    print("Do you want to save it as excel file? Yes or No")
    p = str(input())
    if p == "Yes":
        table.to_excel('transactions_over_150000.xlsx')
        print('Excel file was saved')
    else:
        print('No Excel file was saved')
    return table


#-----------------------Summary by user--------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------

# In[24]:

def summary_by_user(df):
    print("Select the name of the user/JnlPrep regarding column:")
    x = str(input())
    table = df.groupby([x]).sum()
    print("There are " + str(table.shape[0])+ " users found")
    print("Do you want to save it as excel file? Yes or No")
    p = str(input())
    if p == "Yes":
        table.to_excel('summary_by_user.xlsx')
        print('Excel file was saved')
    else:
        print('No Excel file was saved')
    return table

#-----------------------Summary by Authoriser--------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------

# In[25]:

def summary_by_authoriser(df):
    print("Select the name of the authoriser/JnlAuth regarding column:")
    x = str(input())
    table = df.groupby([x]).sum()
    print("There are " + str(table.shape[0])+ " authorisers found")
    print("Do you want to save it as excel file? Yes or No")
    p = str(input())
    if p == "Yes":
        table.to_excel('summary_by_authoriser.xlsx')
        print('Excel file was saved')
    else:
        print('No Excel file was saved')
    return table

#-----------------------Summary by Authoriser and User-----------------------------------------------------
#----------------------------------------------------------------------------------------------------------

# In[26]:

def summary_by_authoriser_user(df):
    print("Select the name of the user/JnlPrep regarding column:")
    x = str(input())
    print("Select the name of the autoriser/JnlAuth regarding column:")
    y = str(input())
    table = df.groupby([y,x]).sum().round(2)
    print("There are " + str(table.shape[0])+ " items found")
    print ("Summary by user and authoriser")
    print("Do you want to save it as excel file? Yes or No")
    p = str(input())
    if p == "Yes":
        table.to_excel('summary_by_authoriser_user.xlsx')
        print('Excel file was saved')
    else:
        print('No Excel file was saved')
    return table
        


# In[27]:

def summary_by_authoriser_user_equal(df):
    print("Select the name of the user column:")
    x = str(input())
    print("Select the name of the autoriser column:")
    y = str(input())
    table = df.loc[df[y] == df[x]].groupby([y,x]).sum().round(2)
    print("There are " + str(table.shape[0])+ " authoriser equal to user found")
    print("Do you want to save it as excel file? Yes or No")
    p = str(input())
    if p == "Yes":
        table.to_excel('summary_by_authoriser_user_equal.xlsx')
        print('Excel file was saved')
    else:
        print('No Excel file was saved')
    return table

# In[28]:

def transactions_authoriser_user_equal(df):
    print("Select the name of the user identificator column:")
    x = str(input())
    print("Select the name of the autoriser identificator column:")
    y = str(input())
    table = df.loc[df[y] == df[x]]
    print("There are " + str(table.shape[0])+ " items found where authoriser and user are the same.")
    return table

#-----------------------Transactions with no description---------------------------------------------------
#----------------------------------------------------------------------------------------------------------

# In[29]:

def items_no_description(df):
    print("Select the name of the account description column:")
    x = str(input())
    table = df[df[x] == '']
    print("There are " + str(table.shape[0])+ " items with no description found")
    print("Do you want to save it as excel file? Yes or No")
    p = str(input())
    if p == "Yes":
        table.to_excel('Items_no_description.xlsx')
        print('Excel file was saved')
    else:
        print('No Excel file was saved')
    return table

#-----------------------Visualisation----------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------

def pie_plot_by_specific_variables(df):
    print("Select the name of the column which your specific variable is located")
    x = str(input())
    print("Select the name of the specific variable")
    y = str(input())
    print("Select the name of the column for grouping data")
    f = str(input())
    print("Select the name of the amount column:")
    z = str(input())
    print("Select the name of the debit column:")
    g = str(input())
    print("Select the name of the credit column:")
    h = str(input())
    table = df.loc[(df[x] == y)]
    table1 = table.groupby([f]).sum().round(2)
    table2 = table1.drop([z,g,h], axis=1)
    gg = table2.plot(kind='pie', subplots=True, figsize=(20, 20))
    return gg

def violin_plot(df):
    import seaborn as sns
    print("Select the name of the column which would by your X axis")
    f = str(input())
    print("Select the name of the column which would by your Y axis")
    r = str(input())
    gg = sns.catplot(x=f, y=r, kind='violin', data=df)
    return gg

def boxen_plot(df):
    import seaborn as sns
    print("Select the name of the column which would by your X axis")
    f = str(input())
    print("Select the name of the column which would by your Y axis")
    r = str(input())
    gg = sns.catplot(x=f, y=r, kind='boxen', data=df)
    return gg

def box_plot(df):
    import seaborn as sns
    print("Select the name of the column which would by your X axis")
    f = str(input())
    print("Select the name of the column which would by your Y axis")
    r = str(input())
    gg = sns.catplot(x=f, y=r, kind='box', data=df)
    return gg

def strip_plot(df):
    import seaborn as sns
    print("Select the name of the column which would by your X axis")
    f = str(input())
    print("Select the name of the column which would by your Y axis")
    r = str(input())
    gg = sns.catplot(x=f, y=r, kind='strip', data=df)
    return gg




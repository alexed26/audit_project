
# coding: utf-8

# In[ ]:

def change_column_names(df):
        print ("Your selected data has " + str(df.shape[1]) + " columns.\n"      
            "They are: ")
        for x in range(0, df.shape[1]):
            print(df.columns[x])
        print("\n")
        print("Which column do you want to change?")
        b = raw_input()
        print ("What name it should have?")
        n = raw_input()
        df.rename(columns={b: n}, inplace=True)
        print("\n")
        print(list(df.columns))
        print("\n")
        print("For other changes repeat the function")


# In[2]:

def missing_values_table(df):

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

        plt.pie(mis_val_table_ren_columns[[1]],autopct='%1.1f%%', shadow=True)

        plt.axis('equal')
        plt.legend(mis_val_table_ren_columns.index.values, loc="best")
        plt.show()

        return mis_val_table_ren_columns


# In[ ]:

def summary_by_account(df):
    print("Select the name of the Account column:")
    x = raw_input()
    print("Select the name of the Period column:")
    y = raw_input()
    table = df.groupby([x,y]).sum().round(2)
    print("Do you want to save it as excel file? Yes or No")
    z = str(raw_input())
    if z == "Yes":
        table.to_excel('summary_by_account.xlsx')
        print('Excel file was saved')
        
    else:
        print('No Excel file was saved')
    return table


# In[ ]:

def summary_by_specific_account_period(df):
    print("Select the name of the Account column:")
    x = raw_input()
    print("Select the account number in a provided period xx-xx-xxxx:")
    z = raw_input()
    print("Select the column which contains the period:")
    y = raw_input()
    print("Select the period in format yyyy-m")
    n = raw_input()
    
    table = df.loc[(df[x] == z) & (df[y] == n)]
    print("There are " + str(table.shape[0])+ " items found")
    print("Do you want to save it as excel file? Yes or No")
    p = str(raw_input())
    if p == "Yes":
        table.to_excel('summary_by_specific_account_period.xlsx')
        print('Excel file was saved')
        
    else:
        print('No Excel file was saved')
    return table


# In[ ]:

def summary_by_specific_account(df):
    print("Select the name of the Account column:")
    x = raw_input()
    print("Select the account number in a provided period xx-xx-xxxx:")
    y = raw_input()
    table = df.loc[(df[x] == y)]
    print("Do you want to save it as excel file? Yes or No")
    p = str(raw_input())
    if p == "Yes":
        table.to_excel('summary_by_specific_account.xlsx')
        print('Excel file was saved')
    else:
        print('No Excel file was saved')
    print("There are " + str(table.shape[0])+ " items found")
    return table


# In[ ]:

def summary_by_noname_account(df):
    print("Select the name of the Account column:")
    x = raw_input()
    print("Select the column which contains the period:")
    y = raw_input()
    table = df.groupby([x,y]).sum().round(2)
    print("There are " + str(table.shape[0])+ " items found")
    print("Do you want to save it as excel file? Yes or No")
    p = str(raw_input())
    if p == "Yes":
        table.to_excel('summary_by_specific_account.xlsx')
        print('Excel file was saved')
    else:
        print('No Excel file was saved')
    return table


# In[ ]:

def summary_by_JnlNo(df):
    print("Select the name of the JnlNo column:")
    x = raw_input()
    print("Select the name of the Amount column:")
    z = raw_input()
    
    table = df.groupby([x]).sum().round(2).loc[df.groupby([x]).sum().round(2)[z] != 0]
    print ("Journals with amount not equal to 0")
    print("There are " + str(table.shape[0])+ " items found")
    print("Do you want to save it as excel file? Yes or No")
    p = str(raw_input())
    if p == "Yes":
        table.to_excel('summary_by_specific_account.xlsx')
        print('Excel file was saved')
    else:
        print('No Excel file was saved')
    return table


# In[ ]:

def summary_by_items_posted_before_6(df):
    print("Select the name of the time column:")
    x = raw_input()
    table = df.loc[(df[x] <'06:00')]
    print("There are " + str(table.shape[0])+ " items found")
    print ("Journals with items before 6 am")
    print("Do you want to save it as excel file? Yes or No")
    p = str(raw_input())
    if p == "Yes":
        table.to_excel('summary_by_specific_account.xlsx')
        print('Excel file was saved')
    else:
        print('No Excel file was saved')
    return table


# In[ ]:

def summary_by_amount(df):
print("Select the name of the Amount column:")
x = raw_input()
table = df.loc[df[x]>=150000]
print("There are " + str(table.shape[0])+ " items found")
print ("Items with amount > 150000")
print("Do you want to save it as excel file? Yes or No")
p = str(raw_input())
if p == "Yes":
    table.to_excel('summary_by_specific_account.xlsx')
    print('Excel file was saved')
else:
    print('No Excel file was saved')
return table


# In[ ]:

def summary_by_period(df):
    print("Select the name of the Period column:")
    x = raw_input()
    table = df.groupby([x]).sum().round(2)
    print("There are " + str(table.shape[0])+ " items found")
    print ("Summary by period")
    print("Do you want to save it as excel file? Yes or No")
    p = str(raw_input())
    if p == "Yes":
        table.to_excel('summary_by_specific_account.xlsx')
        print('Excel file was saved')
    else:
        print('No Excel file was saved')
    return table


# In[ ]:

def summary_by_journal_type(df):
    print("Select the name of the Journal type column:")
    x = raw_input()
    table = df.groupby([x]).sum()
    print("There are " + str(table.shape[0])+ " items found")
    print ("Summary by journals")
    print("Do you want to save it as excel file? Yes or No")
    p = str(raw_input())
    if p == "Yes":
        table.to_excel('summary_by_specific_account.xlsx')
        print('Excel file was saved')
    else:
        print('No Excel file was saved')
    return table


# In[ ]:

def summary_by_journal_perfomance(df):
    print("Select the name of the Amount regarding the perofomance column:")
    x = raw_input()
    table = df.loc[df[x]>=150000]
    print("There are " + str(table.shape[0])+ " items found")
    print ("Summary by perfomance")
    print("Do you want to save it as excel file? Yes or No")
    p = str(raw_input())
    if p == "Yes":
        table.to_excel('summary_by_specific_account.xlsx')
        print('Excel file was saved')
    else:
        print('No Excel file was saved')
    return table


# In[ ]:

def summary_by_user(df):
    print("Select the name of the user/JnlPrep regarding column:")
    x = raw_input()
    table = df.groupby([x]).sum()
    print("There are " + str(table.shape[0])+ " items found")
    print ("Summary by JnlPrep")
    print("Do you want to save it as excel file? Yes or No")
    p = str(raw_input())
    if p == "Yes":
        table.to_excel('summary_by_specific_account.xlsx')
        print('Excel file was saved')
    else:
        print('No Excel file was saved')
    return table


# In[ ]:

def summary_by_authoriser(df):
    print("Select the name of the user/JnlAuth regarding column:")
    x = raw_input()
    table = df.groupby(['JnlAuth']).sum()
    print("There are " + str(table.shape[0])+ " items found")
    print ("Summary by JnlPrep")
    print("Do you want to save it as excel file? Yes or No")
    p = str(raw_input())
    if p == "Yes":
        table.to_excel('summary_by_specific_account.xlsx')
        print('Excel file was saved')
    else:
        print('No Excel file was saved')
    return table


# In[ ]:

def summary_by_authoriser_user(df):
    print("Select the name of the JnlPrep regarding column:")
    x = raw_input()
    print("Select the name of the JnlAuth regarding column:")
    y = raw_input()
    table = df.groupby([y,x]).sum().round(2)
    print("There are " + str(table.shape[0])+ " items found")
    print ("Summary by JnlPrep")
    print("Do you want to save it as excel file? Yes or No")
    p = str(raw_input())
    if p == "Yes":
        table.to_excel('summary_by_specific_account.xlsx')
        print('Excel file was saved')
    else:
        print('No Excel file was saved')
    return table
        


# In[ ]:

def summary_by_authoriser_user_equal(df):
    print("Select the name of the JnlPrep regarding column:")
    x = raw_input()
    print("Select the name of the JnlAuth regarding column:")
    y = raw_input()
    table = df.loc[df['JnlAuth'] == df['JnlPrep']].groupby(['JnlAuth','JnlPrep']).sum().round(2)
    print("There are " + str(table.shape[0])+ " items found")
    print ("Summary by JnlPrep")
    print("Do you want to save it as excel file? Yes or No")
    p = str(raw_input())
    if p == "Yes":
        table.to_excel('summary_by_specific_account.xlsx')
        print('Excel file was saved')
    else:
        print('No Excel file was saved')
    return table


# In[ ]:

def Items_no_description(df):
    print("Select the name of the AccountDesc regarding column:")
    x = raw_input()
    table = df[df[x] == '']
    print("There are " + str(table.shape[0])+ " items found")
    print ("Summary by items with no description")
    print("Do you want to save it as excel file? Yes or No")
    p = str(raw_input())
    if p == "Yes":
        table.to_excel('summary_by_specific_account.xlsx')
        print('Excel file was saved')
    else:
        print('No Excel file was saved')
    return table


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




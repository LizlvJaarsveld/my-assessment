#Title: SQL Questions
#Updated By: Lizl van Jaarsveld

#Questions:
def question_1():
    #ABOUT THIS QUERY
    #This query will use the customers table to find all the duplicate name-surname combinations in the dataset.
    #It will Select the 'Name' and 'Surname' columns from the table for display.
    #The query will group the name-surname combinations and count how many times they occur.
    
    qry = """SELECT Name, Surname FROM customers GROUP BY Name, Surname HAVING (COUNT(*)>1)"""

    return qry



def question_2():    
    #ABOUT THIS QUERY
    #This query will use the customers table to find all the female customers and display them in descending order of income.
    #It will return the Name, Surname and Income columns from the customers dataset.

    qry = """SELECT Name, Surname, Income FROM customers WHERE Gender ='Female' ORDER BY Income DESC"""

    return qry




def question_3():    
    #ABOUT THIS QUERY
    #This query will determine the approval percentage of loans by loanterm.
    #It will create a column called `ApprovalPercentage` and use the existing column 'LoanTerm' from the loans table.

    qry = """SELECT LoanTerm, ROUND(SUM(case when ApprovalStatus = 'Approved' then 1 else 0 end)*100/COUNT(*),2) as ApprovalPercentage FROM loans 
    Group By LoanTerm"""

    return qry




def question_4():    
    #ABOUT THIS QUERY
    #This query will return a breakdown of the number of customers per 'CustomerClass' in the credit table dataset.
    #It will count all the customers in each 'CustomerClass' and return it in the created 'Count' column.

    qry = """SELECT CustomerClass, COUNT(*) as Count FROM credit GROUP BY CustomerClass"""

    return qry




def question_5():    
    #ABOUT THIS QUERY
    #This query will update the credit table dataset to transform the 'CustomerClass' column for 'CreditScore' values between 600 and 650.
    #It will update the 'CustomerClass' column to be of the value 'C'
    
    qry = """UPDATE credit SET CustomerClass = 'C' WHERE CreditScore BETWEEN 600 AND 650"""
    
    return qry


#Title: Advanced SQL Questions
#Updated By: Lizl van Jaarsveld


def question_1():    
    #ABOUT THIS QUERY
    #This query will return the average income per 'CustomerClass' from the customers and credit datasets.
    #It will make use of the JOIN function on the customers and credit datasets to return the 'CustomerClass' and created 'AverageIncome' columns.

    qry = """SELECT ROUND(SUM(c.Income)/COUNT(*), 2) as AverageIncome, cr.CustomerClass, 
    FROM customers c JOIN credit cr ON c.CustomerID = cr.CustomerID GROUP BY cr.CustomerClass"""
    
    return qry


def question_2():    
    #ABOUT THIS QUERY
    #This query will return a breakdown for the number of rejected applications per province.
    #It makes use of a JOIN on the customers and loans datasets and will return the 'RejectedApplications' and 'Province' columns.
    
    qry = """SELECT SUM(case when l.ApprovalStatus = 'Rejected' then 1 else 0 end) as RejectedApplications, 
    CASE
        WHEN c.Region = 'EC' or c.Region ='EasternCape' then 'Eastern Cape'
        WHEN c.Region = 'WC' or c.Region ='WesternCape' then 'Western Cape'
        WHEN c.Region = 'NC' or c.Region ='NorthernCape' then 'Northern Cape'
        WHEN c.Region = 'FS' or c.Region ='FreeState' then 'Free State'
        WHEN c.Region = 'NW' or c.Region ='NorthWest' then 'North West'
        WHEN c.Region = 'GT' or c.Region ='Gauteng' then 'Gauteng'
        WHEN c.Region = 'NL' or c.Region ='Natal' then 'Kwazulu Natal'
        WHEN c.Region = 'MP' or c.Region ='Mpumalanga' then 'Mpumalanga'
        WHEN c.Region = 'LP' or c.Region ='Limpopo' then 'Limpopo'
        END AS Province
    FROM customers c JOIN loans l ON c.CustomerID = l.CustomerID GROUP BY Province """

    return qry


def question_3():    
    #ABOUT THIS QUERY
    #This query will create a new table called 'financing'.
    #It will include all the columns from the loans dataset and the columns 'Income' from customers and 'CreditScore' from credit.

    qry = """CREATE TABLE financing AS
    SELECT l.*, c.Income, cr.CreditScore
    FROM customers c
    JOIN loans l ON c.CustomerID = l.CustomerID
    JOIN credit cr ON c.CustomerID = cr.CustomerID"""

    return qry


def question_4():
    #ABOUT THIS QUERY
    #This query will create a new table called timeline that sumarizes repayments per customer per month.
    #It will use the CROSS JOIN function to join the repayments data set with the months dataset.
    #The table created will only contain repayments made between 6am and 6pm GMT time.
    #It will have the columns 'CustomerID', 'MonthName', 'AmountTotal' and 'NumberOfRepayments'.

    qry = """CREATE TABLE timeline AS
    SELECT CustomerID, MonthName, SUM(Amount) as  AmountTotal, COUNT(CASE WHEN Amount > 0 THEN 1 END) as NumberOfRepayments
    FROM (SELECT r.CustomerID, m.MonthName,
        CASE
        WHEN MONTH(r.RepaymentDate) != m.MonthID THEN 0
        WHEN MONTH(r.RepaymentDate) == m.MonthID THEN r.AMOUNT
        END AS Amount 
    FROM repayments r CROSS JOIN months m 
    WHERE (HOUR(r.RepaymentDate) BETWEEN 6 AND 18) AND r.TimeZone = 'GMT') 
    GROUP BY CustomerID, MonthName
    ORDER BY CustomerID
    """
    return qry
    

def question_5():

    # Make use of conditional aggregation to pivot the `timeline` table such that the columns are as follows:
        # CustomerID, JanuaryRepayments, JanuaryTotal,...,DecemberRepayments, DecemberTotal,...etc
    # MonthRepayments columns (e.g JanuaryRepayments) should be integers
    # Hint: there should be 1x CustomerID = 1

    qry = """____________________"""

    return qry


#QUESTION 6 and 7 are linked

def question_6():

    # The `customers` table was created by merging two separate tables: one containing data for male customers and the other for female customers.
    # Due to an error, the data in the age columns were misaligned in both original tables, resulting in a shift of two places upwards in
    # relation to the corresponding CustomerID.

    # Utilize a window function to correct this mistake in a new `CorrectedAge` column.
    # Create a table called `corrected_customers` with columns: `CustomerID`, `Age`, `CorrectedAge`, `Gender` 
    # Also return a result set for this table
    # Null values can be input manually

    qry = """____________________"""

    return qry


def question_7():

    # Create a column called 'AgeCategory' that categorizes customers by age 
    # Age categories should be as follows:
        # Teen: x < 20
        # Young Adult: 20 <= x < 30
        # Adult: 30 <= x < 60
        # Pensioner: x >= 60
    # Make use of a windows function to assign a rank to each customer based on the total number of repayments per age group. Add this into a "Rank" column.
    # The ranking should not skip numbers in the sequence, even when there are ties, i.e. 1,2,2,2,3,4 not 1,2,2,2,5,6 
    # Customers with no repayments should be included as 0 in the result.

    qry = """____________________"""

    return qry

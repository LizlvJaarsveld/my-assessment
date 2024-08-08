import pandas as pd
import numpy as np
import os

"""
To answer the following questions, make use of datasets: 
    'scheduled_loan_repayments.csv'
    'actual_loan_repayments.csv'
These files are located in the 'data' folder. 

All loans have a loan term of 2 years with an annual interest rate of 10%. Repayments are scheduled monthly.
A type 1 default will occur on a loan when a repayment is missed.
A type 2 default will occur on a loan when more than 15% of the expected total payments are unpaid for the year.

"""


def calculate_df_balances(df_scheduled,df_actual):
    df_merged = pd.merge(df_actual, df_scheduled, on="LoanID")
    """ 
        This is a utility function that creates a merged dataframe that will be used in the following questions. 
        This function will not be graded directly.

        Args:
            df_scheduled (DataFrame): Dataframe created from the 'scheduled_loan_repayments.csv' dataset
            df_actual (DataFrame): Dataframe created from the 'actual_loan_repayments.csv' dataset
        
        Returns:
            DataFrame: A merged Dataframe 

            Columns after the merge should be: 
            ['RepaymentID', 'LoanID', 'Month', 'ActualRepayment', 'LoanAmount', 'ScheduledRepayment']

            Additional columns to be used in later questions should include: 
            ['UnscheduledPrincipal', 'LoanBalanceStart, 'LoanBalanceEnd'] 
            Note: 'LoanBalanceStart' for the first month of each loan should equal the 'LoanAmount'

            You may create other columns to assist you in your calculations. e.g:
            ['InterestPayment']

    """


    return df_merged



#Do not edit these directories
root = os.getcwd()

if 'Task_2' in root:
    df_scheduled = pd.read_csv('data/scheduled_loan_repayments.csv')
    df_actual = pd.read_csv('data/actual_loan_repayments.csv')
else:
    df_scheduled = pd.read_csv('Task_2/data/scheduled_loan_repayments.csv')
    df_actual = pd.read_csv('Task_2/data/actual_loan_repayments.csv')



def question_1(df_balances):
    #ABOUT THIS FUNCTION
    #This function will determine how many loans have defaulted to type 1 out of all the loans present
    #It achieves this by sorting the table according to LoanID and iterrating through the table with conditions
    #These conditions check for missed payments on each loan and adds a missed payment on a loan to a counter variable
    #The counter is then dived by the total number of loans to give you the default rate percentage

    default_rate_percent = 0
    #Sort the table according to LoanID
    newTable = df_balances.sort_values(by=['LoanID'], ascending= True)
    #to determine number of missed repayments per loan a count variable is used
    count = 0
    #to determine the number of loans that have a repayment missed a totalMissed variable is used
    totalMissed = 0

    #Start with the totalLouns at 1 and the loanID as the first row LoanID value
    totalLoans = 1
    loanID =  float(newTable.loc[newTable.index[0], 'LoanID'])
    for index,row in newTable.iterrows():   
        #if the loanID changes it means we are at a new loan
        if loanID != row['LoanID']:
            if count>0:
                totalMissed += 1
            loanID = row['LoanID']
            count = 0
            totalLoans +=1
        else:
            if row['ActualRepayment'] == 0.0:
                count += 1
    default_rate_percent = (totalMissed*100/totalLoans)
    return default_rate_percent






def question_2(df_scheduled, df_balances):
    #ABOUT THIS FUNCTION
    #This function will determine how many loans have defaulted to type 2 out of all the loans present
    #It achieves this by sorting the table according to LoanID and iterrating through the table with conditions
    #These conditions check for missed payments on each loan
    #It proceeds to check what the percentage of missed payments is for a loan.
    #If more than 15% of payments were missed, the counter for total defaulted payments gets increased
    #The counter is then dived by the total number of loans to give you the default rate percentage
    
    default_rate_percent = 0
    #Sort the table according to LoanID
    newTable = df_balances.sort_values(by=['LoanID'], ascending= True)
    #to determine number of missed repayments per loan a count variable is used
    count = 0
    #to determine the number of repayments per loan a count variable is used
    countRepayments = 0
    #the total number of loans that defaulted is indicated by the variabe totalDefaulted
    totalDefaulted = 0
    #Start with the totalLouns at 1 and the loanID as the first row LoanID value
    totalLoans = 1
    loanID =  float(newTable.loc[newTable.index[0], 'LoanID'])
    for index,row in newTable.iterrows():   
        #if the loanID changes it means we are at a new loan
        if loanID != row['LoanID']:
            if(count/countRepayments)>=0.15:
                 totalDefaulted += 1
            loanID = row['LoanID']
            count = 0
            countRepayments = 0
            totalLoans +=1
        else:
            if row['ActualRepayment'] == 0.0:
                count += 1
        countRepayments += 1
    default_rate_percent = (totalDefaulted*100/totalLoans)
    return default_rate_percent






def question_3(df_balances):
    """ 
        Calculate the anualized CPR (As a %) from the geometric mean SMM.
        SMM is calculated as: (Unscheduled Principal)/(Start of Month Loan Balance)
        CPR is calcualted as: 1 - (1- SMM_mean)^12  

        Args:
            df_balances (DataFrame): Dataframe created from the 'calculate_df_balances()' function

        Returns:
            float: The anualized CPR of the loan portfolio as a percent.
            
    """

    return cpr_percent






def question_4(df_balances):
    """ 
        Calculate the predicted total loss for the second year in the loan term.
        Use the equation: probability_of_default * total_loan_balance * (1 - recovery_rate).
        The probability_of_default value must be taken from either your question_1 or question_2 answer. 
        Decide between the two answers based on which default definition you believe to be the more useful metric.
        Assume a recovery rate of 80% 
        
        Args:
            df_balances (DataFrame): Dataframe created from the 'calculate_df_balances()' function
        
        Returns:
            float: The predicted total loss for the second year in the loan term.
            
    """
    
    

    return total_loss
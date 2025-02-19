## 6.100A PSet 1: Part A
## Name:
## Time Spent:
## Collaborators:

##################################################################################
## Get user input for yearly_salary, portion_saved and cost_of_dream_home below ##
##################################################################################
yearly_salary = float(input("Enter your starting yearly salary: "))
portion_saved = float(input("Enter the portion of your salary to be saved: "))
cost_of_dream_home = float(input("Enter the cost of your dream home: "))
down_payment = cost_of_dream_home * .25

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
monthly_salary = yearly_salary / 12.0
monthly_save = monthly_salary * portion_saved
amount_saved = 0

###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ## 
###############################################################################################
months = 0
while amount_saved < cost_of_dream_home:
    additional_savings = amount_saved * (.05 / 12.0)
    amount_saved = amount_saved + (monthly_save + additional_savings)
    months += 1
print(f"Number of months: {months}")
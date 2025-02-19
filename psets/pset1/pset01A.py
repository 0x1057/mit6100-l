# You have just graduated from MIT and have a job! You move to the Bay Area and decide that you want to start saving for a home. Houses are fairly
# expensive, so you start saving up for the down payment on your dream home.

# ***Your goal is to find the number of months it takes to save up for a down payment. The cost of your down payment is calculated by multiplying the
# total cost of your dream house by the down payment percentage.***

# User Inputs. Ask the user to enter the following variables and cast them as floats. They must be initialized in the following order at the beginning of
# your program, before declaring other variables.
# 1. The starting yearly salary ( yearly_salary)
# 2. The portion of salary to be saved ( portion_saved). This variable should be in decimal form (e.g. 0.1 for 10%).
# 3. The cost of your dream home ( cost_of_dream_home)

# Writing the Program. You will need to determine how many months it will take given the following information:
# 1. yearly_salary, as described above.
# 2. portion_saved, as described above.
# 3. cost_of_dream_home, as described above.
# 4. portion_down_payment, the percentage of the total cost needed for a down payment. Assume portion_down_payment = 0.25 (25%).
# 5. The amount that you have saved thus far is amount_saved, which starts at $0.
# 6. You get an annual rate of return r. In other words, at the end of each month, you receive an additional amount_saved * (r/12) funds for your
# savings (the 12 is because r is an annual rate). Assume r = 0.05 (5%).
# 7. At the end of each month, your savings increase by (1) a percentage of your monthly salary and (2) the monthly return on your investment. (Note:
# The investment amount used to calculate the monthly return is the amount you had saved at the start of each month.)

# Output.
# 1. Your program should store the number of months required to save for the down payment using a variable called months.
# Notes
# Be careful about values that represent annual amounts versus monthly amounts.
# If the number of months your program returns is off by one, reread the highlighted text above.
# Assume that users enter valid inputs (e.g. no string inputs when expecting a float).
# Your program should print outputs in the same format as the test cases below. If you're using Spyder, you might see extra lines in between
# outputs. Don't worry about them!



portion_down_payment = cost_of_dream_home * .25
to_save = cost_of_dream_home - portion_down_payment
monthly_salary = yearly_salary / 12.0

# must make below go up by amount saved each month, each month - must do without iteration
amount_saved = monthly_salary * portion_saved # <~~~incorrect
monthly_additional_save = amount_saved * (.05/12)
months = to_save / (amount_saved + monthly_additional_save)

print(f"It will take {months:.1f} months to save for your home")


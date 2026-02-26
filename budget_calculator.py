# budget_calculator.py - Personal Finance Calculator
# Starter code for e002-exercise-python-intro

"""
Personal Finance Calculator
---------------------------
This program helps users understand their monthly budget by collecting
income and expense information and displaying a formatted summary.

Complete the TODO sections below to finish the program.
"""

print("=" * 44)
print("       PERSONAL FINANCE CALCULATOR")
print("=" * 44)
print()


# =============================================================================
# TODO: Task 1 - Collect User Information
# =============================================================================
# Get the user's name
# Example: name = input("Enter your name: ")

name = input("Enter your Name: ")
# Get monthly income (as a float)
# Remember to convert the input to a float!

income = float(input("Enter your monthly income: "))
if income <= 0:
    print("Income is less than 0, exiting program.")
else:
# Get expenses for at least 4 categories:
# - rent: Rent/Housing
# - utilities: Utilities (electric, water, internet)
# - food: Food/Groceries
# - transportation: Transportation (gas, public transit)
    rent = round(float(input("Enter rent: ")), 2)


    utilities = round(float(input("Enter utility costs: ")), 2)


    food = round(float(input("Enter food expenses: ")), 2)
    transportation = round(float(input("Enter transportation costs: ")))


# =============================================================================
# TODO: Task 2 - Perform Calculations
# =============================================================================
# Calculate total expenses

    total_expenses = rent + utilities + food + transportation

# Calculate remaining balance (income - expenses)
    total_balance = income - total_expenses


# Calculate savings rate as a percentage
# Formula: (balance / income) * 100
    savings_percentage = total_balance / income * 100


# Determine financial status
# - If balance > 0: status = "in the green"
# - If balance < 0: status = "in the red"
# - If balance == 0: status = "breaking even"
    status = "not determined"
    if total_balance > 0: status = "in the green"
    elif total_balance < 0: status = "in the red"
    elif total_balance == 0: status = "breaking even"



# =============================================================================
# TODO: Task 3 - Display Results
# =============================================================================
# Create a formatted budget report
# Use f-strings for formatting
# Dollar amounts should show 2 decimal places: f"${amount:.2f}"
# Percentages should show 1 decimal place: f"{rate:.1f}%"

# Example structure:
# print("=" * 44)
# print("       MONTHLY BUDGET REPORT")
# print("=" * 44)
# print(f"Name: {name}")
# ... continue building the report ...
    if(name):
        print(f"Name: {name}")
    else: print("Anonymous")
    print(f"Income: ${income:.2f}")
    print(f"Rent: $A{rent:.2f}")
    print(f"Utilities: ${utilities:.2f}")
    print(f"Transportation: ${transportation:.2f}")
    print(f"Food: ${food:.2f}")
    print("-" * 44)
    print("Percentage Breakdown: ")
    print(f"Rent: {rent/income*100:.1f}%")
    print(f"Utilities: {utilities/income*100:.1f}%")
    print(f"Transportation: {transportation/income*100:.1f}%")
    print(f"Food: {food/income*100:.1f}%")
    print("-" * 44)
    print(f"Your balance: ${total_balance:.2f}")
    print(f"total expenses: ${total_balance:.2f}")
    print(f"Savings: {savings_percentage:.1f}%")
    print(f"Financial Status: {status}")
# =============================================================================
# TODO: Task 4 - Add Validation (Optional Enhancement)
# =============================================================================
# Add these validations before calculations:
# - If name is empty, use "Anonymous"
# - If income is <= 0, print error and exit
# - If any expense is negative, treat as 0


# =============================================================================
# STRETCH GOAL: Category Percentages
# =============================================================================
# Add a section showing what percentage each expense is of total income
# Example: print(f"  - Rent/Housing:    {(rent/income)*100:.1f}% of income")

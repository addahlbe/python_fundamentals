# Functions for Exercise 45 Project
income = 0
def big_increase():
    global income
    income = income + 10000
    return income
def small_increase():
    global income
    income = income + 5000
    return income

def big_decrease():
    global income
    income = income - 10000
    return income

def small_decrease():
    global income
    income = income - 5000
    return income


"""
    This program can be used to calculate loan costs and to print schedule
"""
def equal_payments(loanAmount, loanTerm, interestRate, downPayment):
    totalInterestPaid = 0
    i = interestRate / 12   # i = Interest rate per period assuming 12 periods per year (monthly payment)
    loanAmount += loanAmount * downPayment
    ratePerPeriod = ((loanAmount * i * (1 + i)**loanTerm) / ((1 + i)**loanTerm - 1))

    for n in reversed(range(1, loanTerm + 1)):
        capital = ratePerPeriod / (1 + i)**n
        interest = ratePerPeriod - capital
        totalInterestPaid += interest

    print("Rate per period:", ratePerPeriod)
    print("Total interest paid:", totalInterestPaid)
    print("Total cost of all payments:", loanAmount + totalInterestPaid)

def decreasing_payments(loanAmount, loanTerm, interestRate, downPayment):
    totalInterestPaid = 0
    i = interestRate / 12   # i = Interest rate per period assuming 12 periods per year (monthly payment)
    loanAmount += loanAmount * downPayment

    for n in range(loanTerm):
        capital = loanAmount / loanTerm
        interest = (loanAmount - (capital * n)) * i
        totalInterestPaid += interest

    print("Total interest paid:", totalInterestPaid)
    print("Total cost of all payments:", loanAmount + totalInterestPaid)


equal_payments(200000, 24, 0.05, 0.1)
decreasing_payments(200000, 24, 0.05, 0.1)
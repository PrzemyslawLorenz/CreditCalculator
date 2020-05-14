"""
    This program can be used to calculate loan costs and to print schedule
"""
def checking_value():
    while True:
        try:
            value = int(input())
            break
        except ValueError:
            print("Your value must be integer type")

    return value


def equal_payments(loanAmount, loanTerm, interestRate, downPayment):
    totalInterestPaid = 0
    i = interestRate / 12   # i = Interest rate per period assuming 12 periods per year (monthly payment)
    loanAmount += loanAmount * downPayment
    ratePerPeriod = ((loanAmount * i * (1 + i)**loanTerm) / ((1 + i)**loanTerm - 1))

    print("\n\tSCHEDULE OF EQUAL PAYMENTS\n")
    print("-" * 77)
    print("|  {:14}  |  {:14}  |  {:14}  |  {:14}  |" .format("Payment nr.", "Capital", "Interest", "Total"))
    print("-" * 77)

    for n in range(loanTerm):
        capital = ratePerPeriod / (1 + i)**loanTerm
        interest = ratePerPeriod - capital
        totalInterestPaid += interest
        loanTerm -= 1
        print("|  {:14}  |  {:14.2f}  |  {:14.2f}  |  {:14.2f}  |" .format(n+1, round(capital, 2), round(interest, 2), round(ratePerPeriod, 2)))

    print("-" * 77)
    print("|  {:14}  |  {:14}  |  {:14}  |  {:14}  |" .format("Loan Term", "Loan Amount", "Total interest", "Total costs"))
    print("-" * 77)
    print("|  {:14}  |  {:14.2f}  |  {:14.2f}  |  {:14.2f}  |" .format(n+1, round(loanAmount, 2), round(totalInterestPaid, 2), round(loanAmount + totalInterestPaid, 2)))
    print("-" * 77)


def decreasing_payments(loanAmount, loanTerm, interestRate, downPayment):
    totalInterestPaid = 0
    i = interestRate / 12   # i = Interest rate per period assuming 12 periods per year (monthly payment)
    loanAmount += loanAmount * downPayment

    print("\n\tSCHEDULE OF DECREASING PAYMENTS\n")
    print("-" * 77)
    print("|  {:14}  |  {:14}  |  {:14}  |  {:14}  |" .format("Payment nr.", "Capital", "Interest", "Total"))
    print("-" * 77)

    for n in range(loanTerm):
        capital = loanAmount / loanTerm
        interest = (loanAmount - (capital * n)) * i
        totalInterestPaid += interest
        print("|  {:14}  |  {:14.2f}  |  {:14.2f}  |  {:14.2f}  |" .format(n+1, round(capital, 2), round(interest, 2), round(capital + interest, 2)))

    print("-" * 77)
    print("|  {:14}  |  {:14}  |  {:14}  |  {:14}  |" .format("Loan Term", "Loan Amount", "Total interest", "Total costs"))
    print("-" * 77)
    print("|  {:14}  |  {:14.2f}  |  {:14.2f}  |  {:14.2f}  |" .format(n+1, round(loanAmount, 2), round(totalInterestPaid, 2), round(loanAmount + totalInterestPaid, 2)))
    print("-" * 77)


print("How big loan you want? ")
loanAmount = checking_value()
print("For how long you want this loan (in months)? ")
loanTerm = checking_value()
print("How big is interest rate in your bank (in %)? ")
interestRate = checking_value()
print("How big is down payment in your bank (in %)? ")
downPayment = checking_value()


equal_payments(loanAmount, loanTerm, interestRate / 100, downPayment / 100)
decreasing_payments(loanAmount, loanTerm, interestRate / 100, downPayment / 100)
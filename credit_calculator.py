"""
    This program can be used to calculate loan costs and to print schedule
"""
def checking_value():
    """This module is used for getting user value,
     and to check if it is a int type value.

    Returns:
        value --> [int]
    """
    while True:
        try:
            value = int(input())
            break
        except ValueError:
            print("Your value must be integer type")

    return value


def equal_payments(loanAmount, loanTerm, interestRate, downPayment):
    """This module is used for calculate equal payments.

    Prints:
        SCHEDULE OF EQUAL PAYMENTS
    """
    totalInterestPaid = 0
    ratePerPeriod = ((loanAmount * i * (1 + i)**loanTerm) / ((1 + i)**loanTerm - 1))

    print("\n\tSCHEDULE OF EQUAL PAYMENTS\n")
    print("-" * 77)
    print("|  {:14}  |  {:14}  |  {:14}  |  {:14}  |" .format("Payment nr.", "Capital", "Interest", "Total"))
    print("-" * 77)

    for n in reversed(range(loanTerm)):
        capital = ratePerPeriod / (1 + i)**(n + 1)
        interest = ratePerPeriod - capital
        totalInterestPaid += interest
        print("|  {:14}  |  {:14.2f}  |  {:14.2f}  |  {:14.2f}  |" .format(loanTerm - n, round(capital, 2), round(interest, 2), round(ratePerPeriod, 2)))

    print("-" * 77)
    print("|  {:14}  |  {:14}  |  {:14}  |  {:14}  |" .format("Loan term", "Loan amount", "Total interest", "Total costs"))
    print("-" * 77)
    print("|  {:14}  |  {:14.2f}  |  {:14.2f}  |  {:14.2f}  |" .format(loanTerm, round(loanAmount, 2), round(totalInterestPaid, 2), round(loanAmount + totalInterestPaid, 2)))
    print("-" * 77)


def decreasing_payments(loanAmount, loanTerm, interestRate, downPayment):
    """This module is used for calculate decreasing payments.

    Prints:
        SCHEDULE OF DECREASING PAYMENTS
    """
    totalInterestPaid = 0

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
    print("|  {:14}  |  {:14}  |  {:14}  |  {:14}  |" .format("Loan term", "Loan amount", "Total interest", "Total costs"))
    print("-" * 77)
    print("|  {:14}  |  {:14.2f}  |  {:14.2f}  |  {:14.2f}  |" .format(loanTerm, round(loanAmount, 2), round(totalInterestPaid, 2), round(loanAmount + totalInterestPaid, 2)))
    print("-" * 77)

while True:
    """This is our start of program (looped).
    Here we are asked for the details of our loan.

    Redirection to appropriate modules.
    """

    print("How big loan you want? ")
    loanAmount = checking_value()
    print("For how long you want this loan (in months)? ")
    loanTerm = checking_value()
    print("How big is interest rate in your bank (in %)? ")
    interestRate = checking_value()
    print("How big is down payment in your bank (in %)? ")
    downPayment = checking_value()

    interestRate = interestRate / 100
    downPayment = downPayment / 100
    loanAmount += loanAmount * downPayment
    i = interestRate / 12   # i = Interest rate per period assuming 12 periods per year (monthly payment)

    equal_payments(loanAmount, loanTerm, interestRate, downPayment)
    decreasing_payments(loanAmount, loanTerm, interestRate, downPayment)

    loop = input("\nType 'exit' if you want exit this program\nType anything to start over\n")
    if loop == 'exit':
        break

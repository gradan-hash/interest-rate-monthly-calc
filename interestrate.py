
def main():
  print("This is  monthly payment loan calculator ")
  print("")
  
  
  principal = float(input("input  the loan amount: "))
  apr =float(input("input annual interest rate: "))
  years = int(input("input amount of years: "))
  
  
  monthly_interest_rate = apr/1200
  amount_of_months = years * 12
  monthly_payment =(principal * monthly_interest_rate)/ (1 -(1 + monthly_interest_rate) ** (- amount_of_months))
  
  
  print(f"The monthly repayment for this loan is:   {monthly_payment: .2f}")
  
main()

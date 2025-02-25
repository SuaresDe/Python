cash_balance = 1000
cash_withdrawal = 200
withdrawal_limit = 100

cash_balance >= cash_withdrawal
#True

cash_withdrawal >= withdrawal_limit
#False

cash_balance >= cash_withdrawal and cash_withdrawal >= withdrawal_limit
#False (both have to be True)

cash_balance >= cash_withdrawal or cash_withdrawal >= withdrawal_limit
#True 

emergency_contacts = []

not 1000 > 1500
#True

not emergency_contacts
#True

not "random text"
#False

not ""
#True

#parentheses

cash_balance = 1000
cash_withdrawal = 250
withdrawal_limit = 200
special_check = True

exp = cash_balance >= cash_withdrawal and cash_balance <= withdrawal_limit or special_check and cash_balance >= cash_withdrawal
#True
print(exp)

exp2 = (cash_balance >= cash_withdrawal and cash_balance <= withdrawal_limit) or (cash_balance >= cash_withdrawal and cash_balance <= withdrawal_limit)
#True
print(exp2)

"""
print(True and True)
print(True and False)
print(True or True)
print(True or True)
print(False or False)
print(False and False)
"""
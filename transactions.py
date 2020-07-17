import sys
from bank import (handle_withdrawal, handle_overdraft,
                  get_balance, account_balances)


account_details = {
    'name': 'Damilare Onajole',
    'number': 9027303872
}


def withdraw_funds(value, account):
    import pdb; pdb.set_trace()
    balance = get_balance(account)

    if balance <= 0:
        account = 'overdraft'
        new_balance = handle_overdraft(value)
    else:
        new_balance = handle_withdrawal(account, value)

    print("\t\tYou new {account} balance is {new_balance}\n".format(
        account=account,
        new_balance=new_balance
        )
    )


print("\nWelcome {}\n".format(account_details['name']))

# check account balance
if len(sys.argv) == 1:
    print("\t\tYou account balance is {account_balance} \n".format(
        account_balance=account_balances
    ))

else:
# or withdraw funds
    withdraw_funds(int(sys.argv[1]), sys.argv[2])

account_balances = {
    'current': 2000,
    'savings': 0,
    'overdraft': -70
}


def get_balance(account):
    return account_balances[account]


def handle_overdraft(value):
    return account_balances['overdraft'] - value


def handle_withdrawal(account, value):
    return account_balances[account] - value

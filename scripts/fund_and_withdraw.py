from brownie import FundMe
from scripts.utils import getAccount


def fund():
    fund_me = FundMe[-1]
    account = getAccount()
    print(fund_me.getEntranceFee())
    fund_me.fund({"from": account, "value": fund_me.getEntranceFee()})


def withdraw():
    fund_me = FundMe[-1]
    account = getAccount()
    fund_me.withdraw({"from": account})


def main():
    fund()
    withdraw()

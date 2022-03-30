from brownie import FundMe, config, network, MockV3Aggregator
from scripts.utils import getAccount, LOCAL_BLOCKCHAIN_ENV


def deploy_fundme():
    account = getAccount()
    print(account)

    if network.show_active() not in LOCAL_BLOCKCHAIN_ENV:
        pricefeed_address = config["networks"][network.show_active()][
            "eth_usd_pricefeed_address"
        ]
    else:
        pricefeed_address = MockV3Aggregator.deploy(
            18, 2_000_000_000_000_000_000, {"from": account}
        ).address

    fundme = FundMe.deploy(
        pricefeed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()]["verify"],
    ).address
    print(fundme)


def main():
    deploy_fundme()

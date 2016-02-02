# coding: utf-8
__author__ = 'huiyu'

import time
from swagger_client.apis import account_api
from swagger_client.apis import vpnclient_api
from zooClient import zk_client
from swagger_client.apis import vm_api
import traceback


def full_sync():
    try:
        dso_account_client = account_api.AccountApi()
        dso_vpn_client = vpnclient_api.VpnclientApi()
        dso_vm_client = vm_api.VmApi()

        # get 1 page count 100 for now, must for page request long term
        rtn = dso_account_client.accounts_get(1, 100)
        accounts = rtn.results.item

        client = zk_client.ZookClient("localhost:2181")

        # client.create_mapping_accounts(accounts.item)

        account_info_map = {}
        vpn_client_map = {}
        # get account info for pre account
        for account in accounts:
            account_info = dso_account_client.accounts_account_id_get(account.id)
            vpn_info = dso_vpn_client.vpn_account_id_get(account.id, 1, 1000)
            vpn_clients = vpn_info.results.item

            # client.create_accountinfo_path(account_info)
            account_info_map[account.id] = account_info
            vpn_client_map[account.id] = vpn_clients

            # client.gen_mapping_pre_account(account_info, vpn_clients)

            # vm_info = dso_vm_client.vm_account_id_get(account.id)
            # client.gen_vm_path(vm_info)

        client.delete_dso_path()
        client.create_accounts_path(accounts)

        for account in accounts:
            client.create_accountinfo_path(account_info_map[account.id])
            client.gen_mapping_pre_account(account_info_map[account.id], vpn_client_map[account.id])

        client.stopZooK()

    except Exception as exp:
        print exp.message
        traceback.print_exc()


if __name__ == "__main__":
    while True:
        full_sync()
        time.sleep(120)

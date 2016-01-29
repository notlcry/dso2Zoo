# coding: utf-8

from kazoo.client import KazooClient
import logging
import json


class ZookClient(object):
    def __init__(self, zookeeper_host=None):
        logging.basicConfig()
        # Create a client and start it
        if zookeeper_host is None:
            zookeeper_host = "localhost:2181"
        self.zk = KazooClient(zookeeper_host)
        self.zk.start()

        self.CONST_BASE_PATH = "/dso/"
        self.CONST_ACCOUNTS_PATH = "accounts/"
        self.CONST_GROUPS_PATH = "groups/"
        self.CONST_USERS_PATH = "users/"
        self.CONST_HOSTS_PATH = "hosts/"
        self.CONST_SERVERS_PATH = "servers/"
        self.CONST_SERVICES_PATH = "services/"
        self.CONST_INSTANCES_PATH = "instances/"

        self.CONST_MAPPING_PATH = "Mapping/"
        self.CONST_IP2USER_PATH = "Ip2User/"
        self.CONST_USER2ACCOUNT_PATH = "User2Account/"
        self.CONST_AID2ANAME_PATH = "Aid2Aname/"

    def create_accounts_path(self, accounts, **kwargs):
        # create accounts path
        accounts_path = self.CONST_BASE_PATH + self.CONST_ACCOUNTS_PATH
        self.zk.ensure_path(accounts_path)

        for account in accounts:
            # path = accounts_path + account.account_name
            path = accounts_path + account.id
            account_val = account.to_str()
            self.zk.ensure_path(path)
            self.zk.set(path, b"" + account_val.encode('utf8'))

    def create_accountinfo_path(self, account_info, **kwargs):
        account_path = self.CONST_BASE_PATH + self.CONST_ACCOUNTS_PATH + account_info.id + "/"
        if not self.zk.exists(account_path):
            print "Path" + account_path + " does not exist."

        # create groups path
        groups_path = account_path + self.CONST_GROUPS_PATH
        self.zk.ensure_path(groups_path)

        # set each group
        for group_item in account_info.groups:
            self.create_usergroup_path(groups_path, group_item)

        # create service path
        services_path = account_path + self.CONST_SERVICES_PATH
        self.zk.ensure_path(services_path)

        # set each service
        for service_item in account_info.services:
            self.create_service_path(services_path, service_item)

    def create_service_path(self, parent_path, service):
        service_path = parent_path + service.servicename + "/"
        service_data = "id: " + service.id + "\nservicename: " + \
                       service.servicename + "\ndescription: " + \
                       ("None" if service.description is None else service.description)
        self.zk.ensure_path(service_path)
        self.zk.set(service_path, b"" + service_data.encode('utf8'))

        # create instances path
        instances_path = service_path + self.CONST_INSTANCES_PATH
        self.zk.ensure_path(instances_path)

        # set each instance
        for instance_item in service.instances:
            self.create_instance_path(instances_path, instance_item)

    def create_instance_path(self, parent_path, instance):
        instance_path = parent_path + instance.id
        instance_data = "id: " + instance.id + \
                        "\nmac: " + self.check_none(instance.mac) + \
                        "\nmanageip: " + self.check_none(instance.manageip) + \
                        "\npublicip: " + self.check_none(instance.publicip) + \
                        "\npublicgateway: " + self.check_none(instance.publicgateway) + \
                        "\npublicnetmask: " + self.check_none(instance.publicnetmask) + \
                        "\nserviceip: " + self.check_none(instance.serviceip) + \
                        "\nstatus: " + self.check_none(instance.status)

        self.zk.ensure_path(instance_path)
        self.zk.set(instance_path, b"" + instance_data.encode('utf8'))
        return instance_path

    def create_usergroup_path(self, parent_path, group):
        group_path = parent_path + group.groupname + "/"
        group_data = "id: " + group.id + "\ngroupname: " + \
                     group.groupname + "\ndescription: " + \
                     ("None" if group.description is None else group.description)

        self.zk.ensure_path(group_path)
        self.zk.set(group_path, b"" + group_data.encode('utf8'))

        # create users path
        users_path = group_path + self.CONST_USERS_PATH
        self.zk.ensure_path(users_path)

        # set each user
        for user_item in group.users:
            self.create_user_path(users_path, user_item)

        # create servers path
        servers_path = group_path + self.CONST_SERVERS_PATH
        self.zk.ensure_path(servers_path)

        # set each server/host
        for server in group.servers:
            self.create_host_path(servers_path, server)

    def create_user_path(self, parent_path, user):
        user_path = parent_path + user.name + "/"
        user_data = "id: " + user.id + "\nname: " + \
                    user.name + "\nemail: " + \
                    ("None" if user.email is None else user.email)
        self.zk.ensure_path(user_path)
        self.zk.set(user_path, b"" + user_data.encode('utf8'))

        # create hosts path
        hosts_path = user_path + self.CONST_HOSTS_PATH
        self.zk.ensure_path(hosts_path)

        # set each hosts
        for host_item in user.hosts:
            self.create_host_path(hosts_path, host_item)

    def create_host_path(self, parent_path, host):
        host_path = parent_path + host.mac

        host_data = "ip: " + host.ip + "\nmac: " + \
                    host.mac + "\nhost_name: " + \
                    ("None" if host.host_name is None else host.host_name) + \
                    "\ndomain: " + ("None" if host.domain is None else host.domain)

        self.zk.ensure_path(host_path)
        self.zk.set(host_path, b"" + host_data.encode('utf8'))
        return host_path

    def delete_dso_path(self):
        self.zk.delete("/dso", recursive=True)
        self.zk.ensure_path("/dso")

    def check_none(self, data):
        return "None" if data is None else data

    def create_user2account_path(self, user2account):
        path = self.CONST_BASE_PATH + self.CONST_MAPPING_PATH + self.CONST_USER2ACCOUNT_PATH
        self.zk.ensure_path(path)
        self.zk.set(path, b"" + json.dumps(user2account).encode('utf8'))

    def create_aid2aname_path(self, aid2aname):
        if not self.zk.exists(self.CONST_BASE_PATH + self.CONST_MAPPING_PATH):
            self.zk.ensure_path(self.CONST_BASE_PATH + self.CONST_MAPPING_PATH)
        path = self.CONST_BASE_PATH + self.CONST_MAPPING_PATH + self.CONST_AID2ANAME_PATH
        self.zk.ensure_path(path)
        self.zk.set(path, b"" + json.dumps(aid2aname).encode('utf8'))

    def create_ip2user_path(self, account_info, ip2user):

        if not self.zk.exists(self.CONST_BASE_PATH + self.CONST_MAPPING_PATH):
            self.zk.ensure_path(self.CONST_BASE_PATH + self.CONST_MAPPING_PATH)

        ip2user_path = self.CONST_BASE_PATH + self.CONST_MAPPING_PATH + self.CONST_IP2USER_PATH
        self.zk.ensure_path(ip2user_path)

        account_path = ip2user_path + account_info.id + "/"
        self.zk.ensure_path(account_path)
        account_data = {"account_name": account_info.account_name}
        self.zk.set(account_path, b"" + json.dumps(account_data).encode('utf8'))

        for ip in ip2user.keys():
            ip_path = account_path + ip

            self.zk.ensure_path(ip_path)
            self.zk.set(ip_path, b"" + json.dumps(ip2user[ip]).encode('utf8'))

    def gen_mapping_pre_account(self, account_info, vpn_clients):
        user2account = {}
        ip2user = {}
        for group in account_info.groups:
            for user in group.users:
                user2account[user.id] = account_info.id
                for host in user.hosts:
                    user_data = dict(userid=user.id, username=user.name, useremail=user.email, groupname=group.groupname)
                    ip2user[host.ip] = user_data

        # add vpn info
        for vpn in vpn_clients:
            vpn_user_data = dict(userid='vpn_user', username=vpn.user_name, useremail='', groupname=vpn.group)
            ip2user[vpn.ip] = vpn_user_data

        # create node
        self.create_ip2user_path(account_info, ip2user)

        # not used now
        # self.create_user2account_path(user2account)


    def create_mapping_accounts(self, accounts):
        aid2aname = {}
        for account in accounts:
            aid2aname[account.id] = account.account_name
        self.create_aid2aname_path(aid2aname)

    def stopZooK(self):
        # In the end, stop it
        self.zk.stop()


if __name__ == "__main__":
    try:
        client = ZookClient()
        client.create_accounts_path()
        print "hold"
    except Exception as exp:
        print exp.message

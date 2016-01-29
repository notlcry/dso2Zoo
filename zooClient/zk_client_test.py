# coding: utf-8

from kazoo.client import KazooClient
import logging



class ZookClient(object):

    def __init__(self, api_client=None):
        logging.basicConfig()
        # Create a client and start it
        self.zk = KazooClient()
        self.zk.start()

    def create_accounts_path(self, name, **kwargs):
        path = "/dso/" + name
        self.zk.ensure_path(path)
        self.zk.set(path, b"id: 7b4235ca-00fb-4dca-ad3e-8b6e3662631a\ngroupname: hr\ndescription: 人力资源")


    def create_accountinfo_path(self, account_id, **kwargs):
        self.zk.ensure_path("/app/someservice")

    def stop(self):
        # In the end, stop it
        self.zk.stop()

if __name__ == "__main__":
    try:
        client = ZookClient()
        client.create_accounts_path(u'于'.encode('utf8'))
        print "hold"
    except Exception as exp:
        print exp.message





